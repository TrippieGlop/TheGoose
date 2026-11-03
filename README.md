# The Goose — website

Static site for The Goosemen deli (102 W. Fourth St, Bethlehem PA). No framework, no trackers.

- `src/build.py` + `src/partials.py` assemble the pages into `site/` (`python3 src/build.py`).
- Menu prices live in `src/assets/js/menu-data.js`.
- Illustrations live in `src/art.py` (each one is an inline SVG).
- Hours, closures, ordering link and secret-menu link live in `CONFIG` at the top of `src/assets/js/main.js`.
- `site/` is the ready-to-deploy output (rebuild it after edits). `vercel.json` serves `site/` and adds security headers (CSP, HSTS, frame/sniff/referrer/permissions policies).

Before launch: confirm hours and prices with the owner, set the ordering URL, have the owner review the
Privacy Policy and Terms, and connect the account forms to the real ordering system (they are preview-only).

## Deploy to Vercel
From this folder: `npx vercel` (preview) then `npx vercel --prod`. When asked, keep the settings from vercel.json.
