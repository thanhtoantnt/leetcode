import Link from "next/link";
import { notFound } from "next/navigation";
import Notes from "@/components/Notes";
import { getChapter, getChapters, getNotes } from "@/lib/book";

export function generateStaticParams() {
  return getChapters().map((c) => ({ id: c.id }));
}

export default async function ChapterPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const found = getChapter(id);
  if (!found) notFound();
  const { chapter, part } = found;
  const notes = getNotes(id);
  const all = getChapters();
  const idx = all.findIndex((c) => c.id === id);
  const prev = idx > 0 ? all[idx - 1] : null;
  const next = idx < all.length - 1 ? all[idx + 1] : null;

  return (
    <main>
      <div className="mb-1 flex items-center justify-between text-sm">
        <Link href="/book" className="text-slate-400 hover:text-sky-400">
          ← all chapters
        </Link>
        <span className="text-xs uppercase tracking-wider text-slate-500">
          Part {part.id} — {part.title}
        </span>
      </div>
      <h1 className="mb-1 text-2xl font-bold">
        <span className="font-mono text-slate-500">{chapter.id}.</span> {chapter.title}
      </h1>
      <p className="mb-8 text-sm text-slate-500">PDF page {chapter.pdf} of the local 3rd-edition file (printed page + 21).</p>

      {notes ? (
        <Notes text={notes} />
      ) : (
        <div className="rounded-xl border border-[var(--card-border)] bg-[var(--card-bg)] p-5 text-sm text-slate-400">
          No notes yet. Add{" "}
          <code className="rounded bg-white/10 px-1 font-mono text-xs">
            web/content/book/{id.padStart(2, "0")}.md
          </code>{" "}
          and this page fills itself.
        </div>
      )}

      {chapter.related && chapter.related.length > 0 && (
        <section className="mt-10">
          <h2 className="mb-3 text-xs font-semibold uppercase tracking-wider text-slate-500">In this repo</h2>
          <ul className="space-y-1 text-sm">
            {chapter.related.map((r) => (
              <li key={r.href}>
                <Link href={r.href} className="text-sky-400 hover:underline">
                  {r.label}
                </Link>
              </li>
            ))}
          </ul>
        </section>
      )}

      <nav className="mt-12 flex justify-between border-t border-[var(--card-border)] pt-6 text-sm">
        {prev ? (
          <Link href={`/book/${prev.id}`} className="text-slate-400 hover:text-sky-400">
            ← {prev.id}. {prev.title}
          </Link>
        ) : (
          <span />
        )}
        {next && (
          <Link href={`/book/${next.id}`} className="text-slate-400 hover:text-sky-400">
            {next.id}. {next.title} →
          </Link>
        )}
      </nav>
    </main>
  );
}
