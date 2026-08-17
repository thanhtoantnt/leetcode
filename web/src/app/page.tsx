import Link from "next/link";
import { getVisualized, getSolutionIndex } from "@/lib/content";
import { getChapters, hasNotes } from "@/lib/book";

export default function Home() {
  const visualized = getVisualized();
  const nSol = getSolutionIndex(new Set()).reduce((n, s) => n + s.files.length, 0);
  const nNotes = getChapters().filter((c) => hasNotes(c.id)).length;

  return (
    <main>
      <h1 className="mb-2 text-2xl font-bold">Two ways in</h1>
      <p className="mb-10 text-sm text-slate-400">
        Work problems, or read the book. Same algorithms, different door.
      </p>

      <div className="grid gap-4 sm:grid-cols-2">
        <Link
          href="/problems"
          className="group rounded-xl border border-[var(--card-border)] bg-[var(--card-bg)] p-6 transition-colors hover:border-sky-500/50"
        >
          <div className="mb-3 text-xs font-semibold uppercase tracking-wider text-sky-400">LeetCode</div>
          <div className="mb-2 text-xl font-semibold group-hover:text-sky-300">Problems</div>
          <p className="mb-4 text-sm text-slate-400">
            Animated walkthroughs of solutions in this repo. One frame per decision.
          </p>
          <div className="text-xs text-slate-500">
            {visualized.length} visualized · {nSol} solutions
          </div>
        </Link>

        <Link
          href="/book"
          className="group rounded-xl border border-[var(--card-border)] bg-[var(--card-bg)] p-6 transition-colors hover:border-sky-500/50"
        >
          <div className="mb-3 text-xs font-semibold uppercase tracking-wider text-amber-400">CLRS 3rd ed.</div>
          <div className="mb-2 text-xl font-semibold group-hover:text-sky-300">Introduction to Algorithms</div>
          <p className="mb-4 text-sm text-slate-400">
            Chapter notes and a map from the book onto the pattern folders.
          </p>
          <div className="text-xs text-slate-500">
            {getChapters().length} chapters · {nNotes} with notes
          </div>
        </Link>
      </div>
    </main>
  );
}
