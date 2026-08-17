import Link from "next/link";
import { notFound } from "next/navigation";
import StepPlayer from "@/components/StepPlayer";
import { getProblem, getSolutionCode, getVisualized } from "@/lib/content";

export function generateStaticParams() {
  return getVisualized().map((p) => ({ id: p.id }));
}

export default async function ProblemPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const p = getProblem(id);
  if (!p) notFound();

  const code = p.pyFile ? getSolutionCode(p) : null;

  return (
    <main>
      <div className="mb-1 flex items-center justify-between text-sm">
        <Link href="/" className="text-slate-400 hover:text-sky-400">← all problems</Link>
        <span className="rounded bg-sky-500/15 px-2 py-0.5 text-xs uppercase tracking-wide text-sky-300">
          {p.pattern.replace(/_/g, " ")}
        </span>
      </div>
      <h1 className="mb-1 text-2xl font-bold">
        <span className="font-mono text-slate-500">#{p.num}</span> {p.title}
      </h1>
      <a
        href={`https://leetcode.com/problems/${p.slug}/`}
        className="mb-6 inline-block text-sm text-slate-400 hover:text-sky-400"
      >
        leetcode.com/problems/{p.slug} ↗
      </a>

      {p.intro && <p className="mb-6 whitespace-pre-line text-sm leading-relaxed text-slate-300">{p.intro}</p>}

      <StepPlayer steps={p.steps} mode={p.mode} />

      {p.notes && (
        <div className="mt-6 rounded-xl border border-[var(--card-border)] bg-[var(--card-bg)] p-5 text-sm leading-relaxed text-slate-300 whitespace-pre-line">
          {p.notes}
        </div>
      )}

      {code && (
        <details className="mt-6 rounded-xl border border-[var(--card-border)] bg-[var(--card-bg)] p-5">
          <summary className="cursor-pointer text-sm font-medium">
            Solution source ({p.pyFile})
          </summary>
          <pre className="mt-4 overflow-x-auto rounded-lg bg-black/40 p-4 font-mono text-xs leading-relaxed text-slate-300">
            {code}
          </pre>
        </details>
      )}
    </main>
  );
}
