"use client";

import { useCallback, useEffect, useMemo, useState } from "react";

export interface Step {
  n: number;
  caption: string;
  frame: string;
}

function parseArrayFrame(frame: string) {
  const lines = frame.split("\n");
  const cellIdx = lines.findIndex((l) => l.trim().startsWith("["));
  if (cellIdx < 0) return null;
  const cellLine = lines[cellIdx];
  const bracket = cellLine.indexOf("[");
  const inner = cellLine.slice(bracket + 1).replace(/\]\s*$/, "");
  const tokens = [...inner.matchAll(/\S+/g)].map((m) => ({
    v: m[0].replace(/,$/, ""),
    start: bracket + 1 + m.index!,
  }));

  const markers: Record<number, string> = {};
  const next = lines[cellIdx + 1] ?? "";
  const isMarkerLine = /^[\sA-Za-z]*$/.test(next) && /[A-Za-z]/.test(next);
  if (isMarkerLine) {
    for (const m of next.matchAll(/[A-Za-z]+/g)) {
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
  }

  const lo = Math.min(...Object.keys(markers).map(Number));
  const hi = Math.max(...Object.keys(markers).map(Number));
  const window = Object.keys(markers).length ? { lo, hi } : null;

  const metaLines = lines
    .slice(cellIdx + 1)
    .filter((l) => !isMarkerLine || l !== next);
  return { cells: tokens.map((t) => t.v), markers, window, meta: parseMeta(metaLines.join(" ")) };
}

function parseMeta(raw: string): { key: string; value: string }[] {
  const pairs: { key: string; value: string }[] = [];
  const re = /([A-Za-z_][\w[\].]*)\s*=\s*(\{[^{}]*\}|\[[^[\]]*\]|"[^"]*"|'[^']*'|\S+)/g;
  let m: RegExpExecArray | null;
  while ((m = re.exec(raw))) pairs.push({ key: m[1], value: m[2] });
  const leftover = raw.replace(re, "").replace(/\s{2,}/g, " ").trim();
  if (leftover) pairs.push({ key: "", value: leftover });
  return pairs;
}

export default function StepPlayer({ steps, mode }: { steps: Step[]; mode: "array" | "mono" }) {
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

  const parsed = useMemo(
    () => (mode === "array" && step ? parseArrayFrame(step.frame) : null),
    [mode, step],
  );

  return (
    <div className="rounded-xl border border-[var(--card-border)] bg-[var(--card-bg)] p-6">
      <p className="text-sm text-slate-200">
        <span className="mr-2 rounded bg-sky-500/20 px-2 py-0.5 font-mono text-xs text-sky-300">
          step {i + 1}/{steps.length}
        </span>
        {step?.caption}
      </p>

      <div className="my-6 min-h-[12rem] flex items-center justify-center">
        {parsed ? (
          <div className="w-full">
            <div className="flex items-end justify-center gap-2 font-mono">
              {parsed.cells.map((c, idx) => {
                const mark = parsed.markers[idx];
                const inWin = parsed.window && idx >= parsed.window.lo && idx <= parsed.window.hi;
                return (
                  <div key={idx} className="flex flex-col items-center gap-1">
                    <span className="text-[10px] text-slate-600">{idx}</span>
                    <div
                      className={`flex h-14 min-w-14 items-center justify-center rounded-lg border-2 px-2 text-xl font-semibold transition-colors duration-300 ${
                        mark
                          ? "border-sky-400 bg-sky-500/30 text-white"
                          : inWin
                            ? "border-sky-400/40 bg-sky-500/10 text-slate-100"
                            : "border-[var(--card-border)] bg-black/30 text-slate-500"
                      }`}
                    >
                      {c}
                    </div>
                    <div className="h-5 text-xs font-bold text-sky-300">{mark ?? ""}</div>
                  </div>
                );
              })}
            </div>
            {parsed.meta.length > 0 && (
              <div className="mt-5 flex flex-wrap justify-center gap-2">
                {parsed.meta.map((p, k) =>
                  p.key ? (
                    <span
                      key={k}
                      className="rounded-md border border-[var(--card-border)] bg-black/40 px-2.5 py-1 font-mono text-xs"
                    >
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
            )}
          </div>
        ) : (
          <pre key={i} className="fade-step w-full overflow-x-auto rounded-lg bg-black/40 p-4 font-mono text-sm leading-relaxed text-slate-200">
            {step?.frame}
          </pre>
        )}
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
