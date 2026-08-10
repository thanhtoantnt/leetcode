# 🎓 LeetCode Tutor — Interactive Learning Website

A self-contained, locally-run interactive website that teaches **every LeetCode problem**.

## What's inside

- **4,017 problems** cataloged (every LeetCode problem) with full search & filtering
- **3,240 full lessons** — complete problem statements, examples, constraints, topic tags
- **Progressive hints** for each problem (revealed one at a time, like a real tutor)
- **Learning Roadmap** — NeetCode 150 curriculum organized by pattern
- **Built-in Python editor** — write and run code in the browser (via Pyodide)
- **Your own solutions** — the 100+ solutions already in this repo are integrated
- **Progress tracking** — solved marks, viewed history, and notes (saved in your browser)
- **Dark / light theme**

## Run it

```bash
cd site
./run.sh          # serves on http://localhost:8765
# or pick a port:
./run.sh 3000     # serves on http://localhost:3000
```

Then open **http://localhost:8765** in your browser.

> Requires only Python 3 (for the built-in HTTP server). No build step, no dependencies.
> The in-browser code runner downloads Pyodide from a CDN on first use (needs internet once).

## How to learn

1. **Roadmap** — start with *Arrays & Hashing* and work down; each topic groups problems by pattern
2. Open a problem → read the **Problem** tab
3. Stuck? Open the **Hints** tab and reveal hints one at a time
4. Check the **Approach** tab for a step-by-step solving strategy
5. Code it up in the **Practice** tab and hit **Run**
6. Mark it solved ✅

## Data sources

- Problem list & metadata: LeetCode public API (`/api/problems/all`)
- Full statements, hints, tags, starter code: LeetCode GraphQL API
- Curriculum: NeetCode 150 roadmap

All data is fetched at build time and bundled in `data/` so the site runs fully offline
(except the optional Pyodide code runner).
