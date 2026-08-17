import Link from "next/link";
import { getSolutionIndex, getVisualized } from "@/lib/content";

const patternOrder = (p: string) => p; // groups arrive sorted by file count

export default function Home() {
  const visualized = getVisualized();
  const byPattern = new Map<string, typeof visualized>();
  for (const p of visualized) {
    byPattern.set(p.pattern, [...(byPattern.get(p.pattern) ?? []), p]);
  }
  const solutions = getSolutionIndex(new Set(visualized.map((p) => p.id)));

  return (
    <main>
      <h1 className="mb-2 text-2xl font-bold">Learn by watching the algorithm run</h1>
      <p className="mb-10 text-sm text-slate-400">
        Each visualized problem is a recorded run of its solution: one frame per decision,
        with pointers, windows, and DP cells highlighted. Every solution lives in{" "}
        <a href="https://github.com/thanhtoantnt/leetcode" className="text-sky-400 hover:underline">
          the repo
        </a>{" "}
        next to its explanation.
      </p>

      <section className="mb-14">
        <h2 className="mb-4 text-lg font-semibold">Visualized · {visualized.length}</h2>
        <div className="grid gap-4 sm:grid-cols-2">
          {[...byPattern.entries()].map(([pattern, probs]) =>
            probs.map((p) => (
              <Link
                key={p.id}
                href={`/problems/${p.id}`}
                className="group rounded-xl border border-[var(--card-border)] bg-[var(--card-bg)] p-5 transition-colors hover:border-sky-500/50"
              >
                <div className="mb-1 flex items-center justify-between">
                  <span className="font-mono text-xs text-slate-500">#{p.num}</span>
                  <span className="rounded bg-sky-500/15 px-2 py-0.5 text-[10px] font-medium uppercase tracking-wide text-sky-300">
                    {p.pattern.replace(/_/g, " ")}
                  </span>
                </div>
                <div className="font-semibold group-hover:text-sky-300">{p.title}</div>
                <div className="mt-2 text-xs text-slate-500">{p.steps.length} steps · {p.mode === "array" ? "animated cells" : "frame flipbook"}</div>
              </Link>
            )),
          )}
        </div>
      </section>

      <section>
        <h2 className="mb-4 text-lg font-semibold">All solutions · {solutions.reduce((n, s) => n + s.files.length, 0)}</h2>
        <div className="space-y-4">
          {solutions.map((s) => (
            <details key={s.pattern} className="rounded-xl border border-[var(--card-border)] bg-[var(--card-bg)] p-4">
              <summary className="cursor-pointer text-sm font-medium">
                {patternOrder(s.pattern).replace(/_/g, " ")}{" "}
                <span className="text-slate-500">({s.files.length})</span>
              </summary>
              <ul className="mt-3 grid gap-1 sm:grid-cols-2">
                {s.files.map((f) => (
                  <li key={f.name} className="truncate text-xs">
                    {f.visualized ? "★ " : ""}
                    <a href={f.url} className="font-mono text-slate-400 hover:text-sky-400">
                      {f.name}
                    </a>
                  </li>
                ))}
              </ul>
            </details>
          ))}
        </div>
      </section>
    </main>
  );
}
