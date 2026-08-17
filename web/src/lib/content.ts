import fs from "fs";
import path from "path";

const REPO_ROOT = path.join(process.cwd(), "..");
const SKIP_DIRS = new Set(["site", "web", ".git", ".website_cache", ".next", "node_modules"]);

export interface Step {
  n: number;
  caption: string;
  frame: string;
}

export interface Problem {
  id: string;
  num: number;
  slug: string;
  title: string;
  pattern: string;
  mode: "array" | "mono";
  steps: Step[];
  intro: string;
  notes: string;
  pyFile?: string;
}

const GH_BASE = "https://github.com/thanhtoantnt/leetcode/blob/main";

const STEP_RE = /\*\*\[(\d+)\]\s*([^\n]*)\n+```[a-z]*\n([\s\S]*?)```/g;

function titleFromSlug(slug: string): string {
  return slug
    .split("-")
    .map((w) => w.charAt(0).toUpperCase() + w.slice(1))
    .join(" ");
}

function parseFlipbook(md: string, slug: string): Omit<Problem, "id" | "num" | "slug" | "pattern" | "pyFile"> {
  const steps: Step[] = [];
  let m: RegExpExecArray | null;
  let lastEnd = 0;
  let firstStart = md.length;
  STEP_RE.lastIndex = 0;
  while ((m = STEP_RE.exec(md))) {
    if (steps.length === 0) firstStart = m.index;
    lastEnd = STEP_RE.lastIndex;
    steps.push({ n: parseInt(m[1], 10), caption: m[2].trim(), frame: m[3].replace(/\n$/, "") });
  }
  const heading = md.match(/^#\s+(.+)$/m)?.[1] ?? titleFromSlug(slug);
  const title = heading.replace(/,?\s*visualized\.?$/i, "").replace(/^\d+\s*[—-]\s*/, "");
  const intro = md
    .slice(md.indexOf("\n"), firstStart)
    .trim();
  const notes = md.slice(lastEnd).trim();
  const firstFrameLine = steps[0]?.frame.split("\n").find((l) => l.trim()) ?? "";
  const mode: "array" | "mono" = firstFrameLine.trim().startsWith("[") ? "array" : "mono";
  return { title, mode, steps, intro, notes };
}

export function getVisualized(): Problem[] {
  const problems: Problem[] = [];
  for (const d of fs.readdirSync(REPO_ROOT, { withFileTypes: true })) {
    if (!d.isDirectory() || SKIP_DIRS.has(d.name)) continue;
    const dir = path.join(REPO_ROOT, d.name);
    for (const f of fs.readdirSync(dir)) {
      const m = f.match(/^(\d{4})_([a-z0-9-]+)\.md$/);
      if (!m) continue;
      const md = fs.readFileSync(path.join(dir, f), "utf8");
      const pyFile = f.replace(/\.md$/, ".py");
      problems.push({
        id: m[1],
        num: parseInt(m[1], 10),
        slug: m[2],
        pattern: d.name,
        pyFile: fs.existsSync(path.join(dir, pyFile)) ? `${d.name}/${pyFile}` : undefined,
        ...parseFlipbook(md, m[2]),
      });
    }
  }
  return problems.sort((a, b) => a.num - b.num);
}

export interface SolutionIndex {
  pattern: string;
  files: { name: string; url: string; visualized: boolean }[];
}

export function getSolutionIndex(visualizedIds: Set<string>): SolutionIndex[] {
  const index: SolutionIndex[] = [];
  for (const d of fs.readdirSync(REPO_ROOT, { withFileTypes: true })) {
    if (!d.isDirectory() || SKIP_DIRS.has(d.name)) continue;
    const files = fs
      .readdirSync(path.join(REPO_ROOT, d.name))
      .filter((f) => f.endsWith(".py"))
      .sort()
      .map((f) => ({
        name: f,
        url: `${GH_BASE}/${d.name}/${f}`,
        visualized: visualizedIds.has(f.slice(0, 4)),
      }));
    if (files.length) index.push({ pattern: d.name, files });
  }
  return index.sort((a, b) => b.files.length - a.files.length);
}

export function getProblem(id: string): Problem | undefined {
  return getVisualized().find((p) => p.id === id);
}

export function getSolutionCode(p: Problem): string | null {
  if (!p.pyFile) return null;
  return fs.readFileSync(path.join(REPO_ROOT, p.pyFile), "utf8");
}
