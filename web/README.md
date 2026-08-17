# LeetCode Visualized (web/)

Animated step-by-step explanations for the problems in this repo, deployed to
GitHub Pages: **https://thanhtoantnt.github.io/leetcode/**

## How it works

- Content source = the flipbook markdown files (`<pattern>/NNNN_slug.md`) sitting
  next to each solution `.py`. No database, no scraping — only our own prose.
- `src/lib/content.ts` parses the `**[n]** caption` + fenced-block frames into steps.
- `StepPlayer` renders array frames as animated highlighted cells with
  play/pause/step controls (keyboard: ← → space); non-array frames (trees, grids)
  auto-page as monospace flipbooks.
- Adding an animation = adding one markdown flipbook file. Zero site code.

## Dev

```bash
cd web
npm install
npm run dev     # http://localhost:3000
npm run build   # static export to web/out
```

## Deploy

Push to `main` — `.github/workflows/deploy-pages.yml` builds and publishes.
Requires repo Settings → Pages → Source: **GitHub Actions** (enable once).
