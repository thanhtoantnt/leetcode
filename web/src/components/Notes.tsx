import type { ReactNode } from "react";
import Link from "next/link";
import { getVisualized } from "@/lib/content";

const VISIBLE = new Set(getVisualized().map((p) => p.id));

export function problemHref(num: string) {
  const id = num.padStart(4, "0");
  return VISIBLE.has(id) ? `/problems/${id}` : null;
}

function inline(s: string) {
  const parts = s.split(/(`[^`]+`|\*\*[^*]+\*\*|\*[^*]+\*|problems?\s+\d{1,4}|\b0\d{3}\b)/g);
  return parts.map((part, i) => {
    const dirRef = part.match(/`([\w-]+)\/(\d{4})`/);
    if (dirRef && problemHref(dirRef[2])) {
      return (
        <Link key={i} href={problemHref(dirRef[2])!} className="text-sky-400 underline decoration-sky-400/40 hover:text-sky-300">
          {dirRef[1]}/{dirRef[2]}
        </Link>
      );
    }
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
    if (part.startsWith("*") && part.endsWith("*")) {
      return <em key={i}>{part.slice(1, -1)}</em>;
    }
    const probRef = part.match(/problems?\s+(\d{1,4})/);
    if (probRef && problemHref(probRef[1])) {
      return (
        <Link key={i} href={problemHref(probRef[1])!} className="text-sky-400 underline decoration-sky-400/40 hover:text-sky-300">
          {part}
        </Link>
      );
    }
    if (/^0\d{3}$/.test(part) && problemHref(part)) {
      return (
        <Link key={i} href={problemHref(part)!} className="text-sky-400 underline decoration-sky-400/40 hover:text-sky-300">
          {part}
        </Link>
      );
    }
    return part;
  });
}

export default function Notes({ text }: { text: string }) {
  const blocks = text.split(/\n\n+/);
  const out: ReactNode[] = [];
  let i = 0;
  while (i < blocks.length) {
    const block = blocks[i];
    const fence = block.match(/^```(?:\w+)?\n([\s\S]*?)```$/);
    if (fence) {
      out.push(
        <pre key={i} className="my-4 overflow-x-auto rounded-lg bg-black/40 p-4 font-mono text-xs leading-relaxed text-slate-200">
          {fence[1].replace(/\n$/, "")}
        </pre>,
      );
      i++;
      continue;
    }
    const h = block.match(/^(#{2,3})\s+(.+)$/);
    if (h) {
      const Tag = h[1] === "##" ? "h2" : "h3";
      out.push(
        <Tag key={i} className={h[1] === "##" ? "mt-8 mb-3 text-lg font-semibold" : "mt-6 mb-2 text-base font-semibold"}>
          {h[2]}
        </Tag>,
      );
      i++;
      continue;
    }
    if (block.startsWith("|")) {
      const rows = block.split("\n").filter((r) => !/^\|[\s-|]+\|$/.test(r));
      out.push(
        <div key={i} className="my-4 overflow-x-auto">
          <table className="w-full text-left text-sm">
            <thead>
              <tr className="border-b border-[var(--card-border)] text-slate-400">
                {rows[0]
                  .split("|")
                  .slice(1, -1)
                  .map((c, j) => (
                    <th key={j} className="py-2 pr-4 font-medium">
                      {c.trim()}
                    </th>
                  ))}
              </tr>
            </thead>
            <tbody>
              {rows.slice(1).map((r, ri) => (
                <tr key={ri} className="border-b border-[var(--card-border)]/60">
                  {r
                    .split("|")
                    .slice(1, -1)
                    .map((c, j) => (
                      <td key={j} className="py-2 pr-4 text-slate-300">
                        {inline(c.trim())}
                      </td>
                    ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>,
      );
      i++;
      continue;
    }
    if (block.match(/^[-*]\s/m)) {
      out.push(
        <ul key={i} className="my-3 list-disc space-y-1 pl-5 text-sm text-slate-300">
          {block.split("\n").map((li, j) => (
            <li key={j}>{inline(li.replace(/^[-*]\s+/, ""))}</li>
          ))}
        </ul>,
      );
      i++;
      continue;
    }
    out.push(
      <p key={i} className="mb-3 text-sm leading-relaxed text-slate-300">
        {inline(block)}
      </p>,
    );
    i++;
  }
  return <div>{out}</div>;
}
