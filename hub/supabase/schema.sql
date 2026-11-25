-- Jarvis 2.0 onboarding hub. Run once in a NEW Supabase project: SQL Editor, paste, Run.
-- Then: Authentication, Providers, Email on. Authentication, Email Templates, Magic Link:
-- include {{ .Token }} so students can type the 6 digit code.

-- Who is in the programme. Add a row when a deal closes. Only these emails can sign in.
create table if not exists public.members (
  email text primary key check (email = lower(email)),
  name text,
  update_code uuid not null default gen_random_uuid() unique,
  active boolean not null default true,
  notes text,
  created_at timestamptz not null default now()
);
alter table public.members enable row level security;
drop policy if exists "read own member row" on public.members;
create policy "read own member row" on public.members
  for select to authenticated using (email = lower(auth.jwt() ->> 'email'));

create or replace function public.is_member() returns boolean
language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.members where email = lower(auth.jwt() ->> 'email') and active);
$$;

-- Block sign up for anyone not in members.
create or replace function public.only_members_sign_up() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  if not exists (select 1 from public.members where email = lower(new.email) and active) then
    raise exception 'not_a_member';
  end if;
  return new;
end $$;
drop trigger if exists only_members on auth.users;
create trigger only_members before insert on auth.users
  for each row execute function public.only_members_sign_up();

-- Ticks per step, and which pack version each student installed (item = pack:<id>).
create table if not exists public.progress (
  user_id uuid not null default auth.uid() references auth.users on delete cascade,
  item text not null,
  value text,
  updated_at timestamptz not null default now(),
  primary key (user_id, item)
);
alter table public.progress enable row level security;
drop policy if exists "own progress" on public.progress;
create policy "own progress" on public.progress for all to authenticated
  using (user_id = auth.uid() and public.is_member())
  with check (user_id = auth.uid() and public.is_member());

-- "I'm stuck" tickets. Status new, doing, done.
create table if not exists public.tickets (
  id bigint generated always as identity primary key,
  user_id uuid default auth.uid() references auth.users on delete set null,
  email text default lower(auth.jwt() ->> 'email'),
  module text,
  step text,
  message text not null,
  page text,
  status text not null default 'new' check (status in ('new', 'doing', 'done')),
  created_at timestamptz not null default now()
);
alter table public.tickets enable row level security;
drop policy if exists "insert own ticket" on public.tickets;
create policy "insert own ticket" on public.tickets for insert to authenticated
  with check (user_id = auth.uid() and public.is_member());
drop policy if exists "read own tickets" on public.tickets;
create policy "read own tickets" on public.tickets for select to authenticated
  using (user_id = auth.uid());

-- Current pack versions. Written by the build, read by the download function. No public access.
create table if not exists public.pack_versions (
  id text primary key,
  title text,
  module int,
  version text,
  hash text,
  path text,
  file text,
  note text,
  updated_at timestamptz not null default now()
);
alter table public.pack_versions enable row level security;

-- Private storage for the zips.
insert into storage.buckets (id, name, public) values ('packs', 'packs', false)
  on conflict (id) do nothing;

-- Team view: who is where and who is stuck.
create or replace view public.team_progress with (security_invoker = true) as
select m.email, m.name,
  (select count(*) from public.progress p join auth.users u on u.id = p.user_id
     where lower(u.email) = m.email and p.item like 'step:%') as steps_done,
  (select max(p.updated_at) from public.progress p join auth.users u on u.id = p.user_id
     where lower(u.email) = m.email) as last_active,
  (select count(*) from public.tickets t where t.email = m.email and t.status <> 'done') as open_tickets
from public.members m;
revoke all on public.team_progress from anon, authenticated;
