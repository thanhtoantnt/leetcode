import Link from "next/link";
import { PARTS, hasNotes } from "@/lib/book";

export default function BookPage() {
  return (
    <main>
      <h1 className="mb-10 text-2xl font-bold">Introduction to Algorithms</h1>

      <div className="space-y-10">
        {PARTS.map((part) => (
          <section key={part.id}>
            <h2 className="mb-3 text-xs font-semibold uppercase tracking-wider text-slate-500">
              Part {part.id} — {part.title}
            </h2>
            <ul className="divide-y divide-[var(--card-border)] overflow-hidden rounded-xl border border-[var(--card-border)] bg-[var(--card-bg)]">
              {part.chapters.map((ch) => {
                const notes = hasNotes(ch.id);
                return (
                  <li key={ch.id}>
                    <Link
                      href={`/book/${ch.id}`}
                      className="flex items-center justify-between gap-4 px-4 py-3 hover:bg-white/5"
                    >
                      <div>
                        <span className="mr-3 font-mono text-xs text-slate-500">{ch.id}</span>
                        <span className={notes ? "text-slate-100" : "text-slate-400"}>{ch.title}</span>
                      </div>
                      <span className="shrink-0 text-xs text-slate-500">
                        {notes ? "notes" : `p.${ch.pdf}`}
                      </span>
                    </Link>
                  </li>
                );
              })}
            </ul>
          </section>
        ))}
      </div>
    </main>
  );
}
