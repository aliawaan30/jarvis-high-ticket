# The films' music bed — clean and unobtrusive: a slow warm chord bed, nothing on top.
#   76 bpm, F major: Fmaj9 · Dm9 · B♭maj9 · Csus–C, one bar each, four times round = 16 bars (≈50.5s).
#   Soft electric-piano chords (sine + a touch of tine) over a slow pad and a round sine bass. No melody, no drums.
#   The file is a seamless loop (its tail is wrapped onto its head), so the films can loop it under any length.
# Pure Python (no numpy):  python3 build/gen_music.py  → assets/film-music.wav → ffmpeg (light room + mp3) → assets/film-music.mp3
import math, os, random, struct, subprocess, wave

SR = 32000
BPM = 76
BEAT = 60 / BPM
BAR = 4 * BEAT
BARS = 16
N = int(SR * BAR * BARS)                      # exactly 16 bars: the loop length
L = [0.0] * N; R = [0.0] * N
mtof = lambda m: 440 * 2 ** ((m - 69) / 12)
rnd = random.Random(3)

def add(t0, dur, fn, pan=0.0, gain=1.0):
    """render fn(t) for dur seconds from t0, wrapping round the loop"""
    i0 = int(t0 * SR); n = int(dur * SR)
    gl, gr = gain * math.cos((pan + 1) * math.pi / 4), gain * math.sin((pan + 1) * math.pi / 4)
    for k in range(n):
        v = fn(k / SR)
        j = (i0 + k) % N
        L[j] += v * gl; R[j] += v * gr

def keys(m, hold, vel):
    """a soft Rhodes-like voice: sine body, a little bell on the attack, gentle decay and release"""
    f = mtof(m); w = 2 * math.pi * f
    def fn(t):
        env = min(1, t / .006) * math.exp(-t * 1.1)
        if t > hold: env *= max(0, 1 - (t - hold) / 1.4)
        bell = .28 * math.exp(-t * 6) * math.sin(w * t + 1.1 * math.exp(-t * 8) * math.sin(w * 7 * t))
        return (math.sin(w * t) + .16 * math.sin(2 * w * t) * math.exp(-t * 2.5) + bell) * env * vel
    return fn, hold + 1.4

def pad(m, dur, vel):
    """a slow, warm pad: two slightly detuned sines, long swell in and out"""
    f = mtof(m); w1, w2 = 2 * math.pi * f * 1.002, 2 * math.pi * f * .998
    def fn(t):
        env = min(1, t / 1.6) * min(1, max(0, (dur - t) / 1.6))
        return (math.sin(w1 * t) + math.sin(w2 * t) + .12 * math.sin(2 * w1 * t)) * .5 * env * vel
    return fn, dur

def bass(m, dur, vel):
    f = mtof(m); w = 2 * math.pi * f
    def fn(t):
        env = min(1, t / .03) * math.exp(-t * .55) * min(1, max(0, (dur - t) / .4))
        return (math.sin(w * t) + .08 * math.sin(2 * w * t)) * env * vel
    return fn, dur

# chords as voiced on a piano (left hand low, right hand open), bass roots underneath
CH = [[57, 60, 64, 67], [57, 60, 64, 65], [57, 58, 62, 65], [55, 60, 62, 67]]     # Fmaj9 · Dm9 · B♭maj9 · Csus
LAST = [55, 60, 64, 67]                                                            # … resolving to C on beat 3 of bar four
BS = [41, 38, 46, 36]

for bar in range(BARS):
    t0 = bar * BAR; k = bar % 4
    ch = CH[k]
    # the pad holds the whole bar, overlapping into the next for a seamless bed
    for j, m in enumerate(ch[1:]):
        fn, d = pad(m - 12, BAR + 1.6, .085); add(t0 - .2, d, fn, pan=(-.4 + j * .4))
    # keys: a full chord on beat one, a lighter re-strike on beat three, rolled slightly like a real hand
    for j, m in enumerate(ch):
        fn, d = keys(m, BEAT * 1.8, .16); add(t0 + j * .018, d, fn, pan=(-.3 + j * .2))
    second = LAST if k == 3 else ch
    for j, m in enumerate(second[1:]):
        fn, d = keys(m, BEAT * 1.6, .09); add(t0 + 2 * BEAT + .01 + j * .014, d, fn, pan=(.3 - j * .2))
    # bass: root on one, a quiet fifth on three
    fn, d = bass(BS[k], BEAT * 2.2, .26); add(t0, d, fn)
    fn, d = bass(BS[k] + 7 if k != 3 else 43, BEAT * 1.8, .14); add(t0 + 2 * BEAT, d, fn)

peak = max(max(abs(x) for x in L), max(abs(x) for x in R))
g = .7 / peak
here = os.path.dirname(os.path.abspath(__file__))
wav = os.path.join(here, '..', 'assets', 'film-music.wav')
mp3 = os.path.join(here, '..', 'assets', 'film-music.mp3')
with wave.open(wav, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(b''.join(struct.pack('<hh', int(math.tanh(L[i] * g) * 30000), int(math.tanh(R[i] * g) * 30000)) for i in range(N)))
# a light room and a gentle top-end roll-off; loudness kept well below the deck's voice
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', wav, '-af',
                'aecho=0.8:0.6:60|110:0.18|0.12,lowpass=f=5200,loudnorm=I=-23:TP=-3:LRA=7',
                '-ar', '44100', '-b:a', '128k', mp3], check=True)
os.remove(wav)
print('wrote', mp3, round(N / SR, 2), 's')
