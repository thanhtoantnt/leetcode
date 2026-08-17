import type { Metadata } from "next";
import Link from "next/link";
import "./globals.css";

export const metadata: Metadata = {
  title: "Algorithms — LeetCode + CLRS",
  description: "Animated LeetCode walkthroughs and notes on Introduction to Algorithms.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="antialiased">
        <nav className="sticky top-0 z-50 border-b border-[var(--card-border)] bg-[var(--background)]/80 backdrop-blur-sm">
          <div className="mx-auto flex h-14 max-w-4xl items-center justify-between px-6">
            <div className="flex items-center gap-6">
              <Link href="/" className="text-lg font-bold tracking-tight">
                <span className="text-sky-500">◆</span> Algorithms
              </Link>
              <div className="hidden gap-1 sm:flex">
                <Link href="/problems" className="rounded-md px-3 py-1.5 text-sm text-slate-400 hover:bg-white/5 hover:text-white">
                  Problems
                </Link>
                <Link href="/book" className="rounded-md px-3 py-1.5 text-sm text-slate-400 hover:bg-white/5 hover:text-white">
                  Book
                </Link>
              </div>
            </div>
            <a
              href="https://github.com/thanhtoantnt/leetcode"
              className="text-sm text-slate-400 hover:text-white"
            >
              GitHub
            </a>
          </div>
        </nav>
        <div className="mx-auto max-w-4xl px-6 py-10">{children}</div>
        <footer className="mx-auto max-w-4xl border-t border-[var(--card-border)] px-6 py-6 text-center text-xs text-slate-600">
          Own explanations &amp; solutions only — problem links go to leetcode.com
        </footer>
      </body>
    </html>
  );
}
