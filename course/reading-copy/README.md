# Reading copy of the High Ticket Course (static site)

Built from the current studio outline, lessons and images. Pure static: index.html plus data/img assets. No backend or login. Google Fonts is an external dependency. noindex is retained.

From the repo root run `python3 scripts/build_reading_copy.py` to produce a complete HTML document. The low-level build.py still emits a fragment for compatibility. The helper resolves the studio relative to this checkout; no Blake-specific filesystem paths are required.

Preview with `python3 -m http.server 4331 --bind 127.0.0.1 --directory course/reading-copy`. The local authoring server is a different tool. Neither has a paid member access gate. Rebuilding here does not deploy to the existing chatgpt.site URL.
