"use client";

import { useCallback, useEffect, useMemo, useState } from "react";

export interface Step {
  n: number;
  caption: string;
  frame: string;
}

type Kind = "array" | "rows" | "grid" | "tree";

interface Meta {
  key: string;
  value: string;
}

interface Parsed {
  kind: Kind;
  rows: { label: string; cells: string[]; markers: Record<number, string> }[];
  window: { lo: number; hi: number } | null;
  meta: Meta[];
  tree: string[];
}

const CELL = /^[.\d-]+$/;

function tokenStarts(prefix: string, rest: string) {
  return [...rest.matchAll(/\S+/g)].map((m) => ({
    v: m[0].replace(/,$/, ""),
    start: prefix.length + m.index!,
  }));
}

function attachMarkers(line: string, tokens: { v: string; start: number }[]) {
  const markers: Record<number, string> = {};
  if (!/^[\sA-Za-z]*$/.test(line) || !/[A-Za-z]/.test(line)) return markers;
  for (const m of line.matchAll(/[A-Za-z]+/g)) {
    const pos = m.index!;
    let best = 0;
    let bestDist = Infinity;
    tokens.forEach((t, i) => {
      const mid = t.start + t.v.length / 2;
      const dist = Math.abs(mid - pos);
      if (dist < bestDist) {
        bestDist = dist;
        best = i;
      }
    });
    markers[best] = (markers[best] ?? "") + m[0];
  }
  return markers;
}

function parseMeta(raw: string): Meta[] {
  const pairs: Meta[] = [];
  const re = /([A-Za-z_][\w[\].]*)=(\{[^{}]*\}|\[[^[\]]*\]|"[^"]*"|'[^']*'|\S+)/g;
  let m: RegExpExecArray | null;
  while ((m = re.exec(raw))) pairs.push({ key: m[1], value: m[2] });
  const leftover = raw.replace(re, "").replace(/\s{2,}/g, " ").trim();
  if (leftover) pairs.push({ key: "", value: leftover });
  return pairs;
}

function parseFrame(frame: string): Parsed {
  const lines = frame.split("\n");
  if (lines.some((l) => /[├└│]/.test(l))) {
    return { kind: "tree", rows: [], window: null, meta: [], tree: lines };
  }

  const arrIdx = lines.findIndex((l) => /\[[^\]]+\]/.test(l.trim()));
  if (arrIdx >= 0) {
    const line = lines[arrIdx];
    const bracket = line.indexOf("[");
    const inner = line.slice(bracket + 1).replace(/\]\s*$/, "");
    const tokens = tokenStarts(line.slice(0, bracket + 1), inner);
    const next = lines[arrIdx + 1] ?? "";
    const markers = attachMarkers(next, tokens);
    const keys = Object.keys(markers).map(Number);
    const metaLines = lines.slice(arrIdx + 1).filter((l) => l !== next || !Object.keys(markers).length);
    return {
      kind: "array",
      rows: [{ label: "", cells: tokens.map((t) => t.v), markers }],
      window: keys.length ? { lo: Math.min(...keys), hi: Math.max(...keys) } : null,
      meta: parseMeta(metaLines.join(" ")),
      tree: [],
    };
  }

  const rows: Parsed["rows"] = [];
  const leftover: string[] = [];
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const labeled = line.match(/^(\w+):\s+(\S.*)$/);
    if (labeled) {
      const tokens = tokenStarts(labeled[0].slice(0, labeled[0].length - labeled[2].length), labeled[2]);
      if (tokens.length && tokens.every((t) => CELL.test(t.v))) {
        const next = lines[i + 1] ?? "";
        const markers = attachMarkers(next, tokens);
        if (Object.keys(markers).length) i++;
        rows.push({ label: labeled[1], cells: tokens.map((t) => t.v), markers });
        continue;
      }
    }
    const grid = line.match(/^(\s*)([\d.](?:\s+[\d.])+)\s*$/);
    if (grid) {
      const tokens = tokenStarts(grid[1], grid[2]);
      rows.push({ label: "", cells: tokens.map((t) => t.v), markers: {} });
      continue;
    }
    if (line.trim()) leftover.push(line);
  }

  if (rows.length) {
    const kind: Kind = rows.some((r) => r.label) ? "rows" : "grid";
    return { kind, rows, window: null, meta: parseMeta(leftover.join(" ")), tree: [] };
  }

  return { kind: "tree", rows: [], window: null, meta: [], tree: lines };
}

function cellClass(opts: { mark?: string; inWin?: boolean; empty?: boolean; fresh?: boolean; source?: boolean }) {
  if (opts.mark) return "border-sky-400 bg-sky-500/30 text-white";
  if (opts.fresh) return "border-amber-400/70 bg-amber-500/20 text-amber-100";
  if (opts.inWin) return "border-sky-400/40 bg-sky-500/10 text-slate-100";
  if (opts.empty) return "border-[var(--card-border)] bg-transparent text-slate-700";
  if (opts.source) return "border-slate-600 bg-slate-800/80 text-slate-300";
  return "border-[var(--card-border)] bg-black/30 text-slate-400";
}

function Cells({
  cells,
  markers,
  window,
  prev,
  showIndex,
}: {
  cells: string[];
  markers: Record<number, string>;
  window?: { lo: number; hi: number } | null;
  prev?: string[];
  showIndex?: boolean;
}) {
  return (
    <div className="flex items-end justify-center gap-2 font-mono">
      {cells.map((c, idx) => {
        const mark = markers[idx];
        const empty = c === ".";
        const fresh = !!prev && prev[idx] !== c;
        const inWin = !!window && idx >= window.lo && idx <= window.hi;
        return (
          <div key={idx} className="flex flex-col items-center gap-1">
            {showIndex && <span className="text-[10px] text-slate-600">{idx}</span>}
            <div
              className={`flex h-12 min-w-12 items-center justify-center rounded-lg border-2 px-2 text-lg font-semibold transition-colors duration-300 ${cellClass({
                mark,
                inWin,
                empty,
                fresh,
                source: c === "0",
              })}`}
            >
              {c}
            </div>
            <div className="h-5 text-xs font-bold text-sky-300">{mark ?? ""}</div>
          </div>
        );
      })}
    </div>
  );
}

function MetaChips({ meta }: { meta: Meta[] }) {
  if (!meta.length) return null;
  return (
    <div className="mt-5 flex flex-wrap justify-center gap-2">
      {meta.map((p, k) =>
        p.key ? (
          <span key={k} className="rounded-md border border-[var(--card-border)] bg-black/40 px-2.5 py-1 font-mono text-xs">
            <span className="text-slate-500">{p.key}</span>
            <span className="mx-1 text-slate-600">=</span>
            <span className="text-sky-200">{p.value}</span>
          </span>
        ) : (
          <span key={k} className="px-1 py-1 font-mono text-xs text-amber-200">
            {p.value}
          </span>
        ),
      )}
    </div>
  );
}

function TreeView({ lines, prev }: { lines: string[]; prev?: string[] }) {
  const seen = new Set(prev ?? []);
  return (
    <div className="w-full overflow-x-auto rounded-lg bg-black/40 p-4 font-mono text-sm leading-6">
      {lines.map((line, i) => {
        const fresh = !seen.has(line);
        const ok = line.includes("✓");
        const bad = /✗|dead/.test(line);
        const color = ok
          ? "text-emerald-300"
          : bad
            ? "text-rose-400/80"
            : fresh
              ? "text-sky-200"
              : "text-slate-500";
        return (
          <div key={i} className={`whitespace-pre ${color} ${fresh && !ok && !bad ? "font-medium" : ""}`}>
            {line || " "}
          </div>
        );
      })}
    </div>
  );
}

export default function StepPlayer({ steps }: { steps: Step[] }) {
  const [i, setI] = useState(0);
  const [playing, setPlaying] = useState(false);
  const step = steps[i];

  const next = useCallback(() => setI((v) => Math.min(v + 1, steps.length - 1)), [steps.length]);
  const prev = useCallback(() => setI((v) => Math.max(v - 1, 0)), []);

  useEffect(() => {
    if (!playing) return;
    if (i >= steps.length - 1) {
      setPlaying(false);
      return;
    }
    const t = setInterval(next, 1800);
    return () => clearInterval(t);
  }, [playing, i, next, steps.length]);

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "ArrowRight") next();
      else if (e.key === "ArrowLeft") prev();
      else if (e.key === " ") {
        e.preventDefault();
        setPlaying((p) => !p);
      }
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [next, prev]);

  const parsed = useMemo(() => (step ? parseFrame(step.frame) : null), [step]);
  const prevParsed = useMemo(() => (i > 0 ? parseFrame(steps[i - 1].frame) : null), [i, steps]);

  return (
    <div className="rounded-xl border border-[var(--card-border)] bg-[var(--card-bg)] p-6">
      <p className="text-sm text-slate-200">
        <span className="mr-2 rounded bg-sky-500/20 px-2 py-0.5 font-mono text-xs text-sky-300">
          step {i + 1}/{steps.length}
        </span>
        {step?.caption}
      </p>

      <div className="my-6 min-h-[12rem] flex items-center justify-center">
        {parsed?.kind === "tree" ? (
          <TreeView lines={parsed.tree} prev={prevParsed?.tree} />
        ) : parsed?.kind === "rows" ? (
          <div className="w-full space-y-3">
            {parsed.rows.map((row, ri) => (
              <div key={ri} className="flex items-center justify-center gap-3">
                <span className="w-16 text-right font-mono text-xs text-slate-500">{row.label}</span>
                <Cells
                  cells={row.cells}
                  markers={row.markers}
                  prev={prevParsed?.rows[ri]?.cells}
                  showIndex={ri === 0}
                />
              </div>
            ))}
            <MetaChips meta={parsed.meta} />
          </div>
        ) : parsed?.kind === "grid" ? (
          <div className="w-full">
            <div className="flex flex-col items-center gap-1">
              {parsed.rows.map((row, ri) => (
                <Cells key={ri} cells={row.cells} markers={row.markers} prev={prevParsed?.rows[ri]?.cells} />
              ))}
            </div>
            <MetaChips meta={parsed.meta} />
          </div>
        ) : parsed?.kind === "array" ? (
          <div className="w-full">
            <Cells
              cells={parsed.rows[0].cells}
              markers={parsed.rows[0].markers}
              window={parsed.window}
              showIndex
            />
            <MetaChips meta={parsed.meta} />
          </div>
        ) : null}
      </div>

      <div className="flex items-center justify-center gap-3">
        <button onClick={prev} disabled={i === 0} className="rounded-lg border border-[var(--card-border)] px-3 py-1.5 text-sm disabled:opacity-30 hover:bg-white/5">
          ◀ back
        </button>
        <button
          onClick={() => {
            if (i === steps.length - 1) setI(0);
            setPlaying((p) => !p);
          }}
          className="rounded-lg bg-sky-600 px-4 py-1.5 text-sm font-medium hover:bg-sky-500"
        >
          {playing ? "⏸ pause" : "▶ play"}
        </button>
        <button onClick={next} disabled={i === steps.length - 1} className="rounded-lg border border-[var(--card-border)] px-3 py-1.5 text-sm disabled:opacity-30 hover:bg-white/5">
          next ▶
        </button>
      </div>

      <div className="mt-4 flex justify-center gap-1.5">
        {steps.map((s, idx) => (
          <button
            key={s.n}
            onClick={() => setI(idx)}
            title={s.caption}
            className={`h-1.5 w-6 rounded-full transition-colors ${idx === i ? "bg-sky-400" : "bg-white/15 hover:bg-white/30"}`}
          />
        ))}
      </div>
      <p className="mt-3 text-center text-xs text-slate-500">← → step · space play/pause</p>
    </div>
  );
}
