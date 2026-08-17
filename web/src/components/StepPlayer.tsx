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
  const cellLine = lines[cellIdx];
  const inner = cellLine.trim().replace(/^\[|\]$/g, "");
  const tokens = [...inner.matchAll(/\S+/g)].map((m) => ({ v: m[0], start: m.index! }));
  const markers: Record<number, string> = {};
  const next = lines[cellIdx + 1] ?? "";
  if (/^[\sA-Za-z]*$/.test(next) && next.trim()) {
    for (const m of next.matchAll(/[A-Za-z]+/g)) {
      const pos = m.index! + Math.floor(m[0].length / 2);
      let best = -1;
      let bestDist = Infinity;
      tokens.forEach((t, i) => {
        const dist = Math.abs(t.start - pos);
        if (dist < bestDist) {
          bestDist = dist;
          best = i;
        }
      });
      if (best >= 0) markers[best] = (markers[best] ?? "") + m[0];
    }
  }
  const meta = lines.slice(cellIdx + 1).filter((l) => l !== next || !/^[\sA-Za-z]*$/.test(l)).join("\n").trim();
  return { cells: tokens.map((t) => t.v), markers, meta };
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

  const parsed = useMemo(() => (mode === "array" && step ? parseArrayFrame(step.frame) : null), [mode, step]);

  return (
    <div className="rounded-xl border border-[var(--card-border)] bg-[var(--card-bg)] p-6">
      <div className="flex items-baseline justify-between gap-4">
        <p className="text-sm text-slate-300">
          <span className="mr-2 rounded bg-sky-500/20 px-2 py-0.5 font-mono text-xs text-sky-300">step {i + 1}/{steps.length}</span>
          {step?.caption}
        </p>
      </div>

      <div className="my-6 min-h-[10rem] flex items-center justify-center">
        {parsed ? (
          <div>
            <div className="flex items-end gap-1.5 font-mono">
              {parsed.cells.map((c, idx) => (
                <div key={idx} className="flex flex-col items-center">
                  <div
                    className={`flex h-12 min-w-12 items-center justify-center rounded-lg border px-2 text-lg transition-colors duration-300 ${
                      parsed.markers[idx]
                        ? "border-sky-400 bg-sky-500/25 text-white"
                        : "border-[var(--card-border)] bg-black/30 text-slate-300"
                    }`}
                  >
                    {c}
                  </div>
                  <div className="h-5 text-xs font-bold text-sky-300">{parsed.markers[idx] ?? ""}</div>
                </div>
              ))}
            </div>
            {parsed.meta && (
              <pre className="mt-3 text-center font-mono text-sm text-slate-400 whitespace-pre-wrap">{parsed.meta}</pre>
            )}
          </div>
        ) : (
          <pre key={i} className="fade-step rounded-lg bg-black/40 p-4 font-mono text-sm leading-relaxed text-slate-200">
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
