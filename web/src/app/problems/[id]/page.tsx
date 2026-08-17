import Link from "next/link";
import { notFound } from "next/navigation";
import StepPlayer from "@/components/StepPlayer";
import { getProblem, getSolutionCode, getVisualized } from "@/lib/content";

export function generateStaticParams() {
  return getVisualized().map((p) => ({ id: p.id }));
}

function Prose({ text }: { text: string }) {
  return (
    <div className="space-y-3 text-sm leading-relaxed text-slate-300">
      {text.split(/\n\n+/).map((block, i) => {
        const fence = block.match(/^```(?:\w+)?\n([\s\S]*?)```$/);
        if (fence) {
          return (
            <pre key={i} className="overflow-x-auto rounded-lg bg-black/40 p-3 font-mono text-xs text-slate-200">
              {fence[1].replace(/\n$/, "")}
            </pre>
          );
        }
        return (
          <p key={i} className="whitespace-pre-line">
            {inline(block)}
          </p>
        );
      })}
    </div>
  );
}

function inline(s: string) {
  const parts = s.split(/(`[^`]+`|\*\*[^*]+\*\*)/g);
  return parts.map((part, i) => {
    if (part.startsWith("`") && part.endsWith("`")) {
      return (
        <code key={i} className="rounded bg-white/10 px-1 py-0.5 font-mono text-[0.85em] text-sky-200">
          {part.slice(1, -1)}
        </code>
      );
    }
    if (part.startsWith("**") && part.endsWith("**")) {
      return (
        <strong key={i} className="font-semibold text-slate-100">
          {part.slice(2, -2)}
        </strong>
      );
    }
    return part;
  });
}

export default async function ProblemPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const p = getProblem(id);
  if (!p) notFound();

  const code = p.pyFile ? getSolutionCode(p) : null;

  return (
    <main>
      <div className="mb-1 flex items-center justify-between text-sm">
        <Link href="/problems" className="text-slate-400 hover:text-sky-400">
          ← all problems
        </Link>
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

      {p.problem && (
        <section className="mb-8 rounded-xl border border-[var(--card-border)] bg-[var(--card-bg)] p-5">
          <h2 className="mb-3 text-xs font-semibold uppercase tracking-wider text-slate-500">Problem</h2>
          <Prose text={p.problem} />
        </section>
      )}

      {p.intro && (
        <p className="mb-4 text-sm leading-relaxed text-slate-400">{inline(p.intro)}</p>
      )}

      <StepPlayer steps={p.steps} />

      {p.notes && (
        <section className="mt-6 rounded-xl border border-[var(--card-border)] bg-[var(--card-bg)] p-5">
          <h2 className="mb-3 text-xs font-semibold uppercase tracking-wider text-slate-500">Takeaway</h2>
          <Prose text={p.notes} />
        </section>
      )}

      {code && (
        <details className="mt-6 rounded-xl border border-[var(--card-border)] bg-[var(--card-bg)] p-5">
          <summary className="cursor-pointer text-sm font-medium">Solution source ({p.pyFile})</summary>
          <pre className="mt-4 overflow-x-auto rounded-lg bg-black/40 p-4 font-mono text-xs leading-relaxed text-slate-300">
            {code}
          </pre>
        </details>
      )}
    </main>
  );
}
