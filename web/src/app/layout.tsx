import type { Metadata } from "next";
import Link from "next/link";
import "./globals.css";

export const metadata: Metadata = {
  title: "LeetCode Visualized",
  description: "Animated step-by-step explanations of LeetCode problems and solutions.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="mx-auto max-w-4xl px-6 py-10 antialiased">
        <header className="mb-10 flex items-center justify-between">
          <Link href="/" className="text-xl font-bold hover:text-sky-400">
            LeetCode <span className="text-sky-400">Visualized</span>
          </Link>
          <a
            href="https://github.com/thanhtoantnt/leetcode"
            className="text-sm text-slate-400 hover:text-sky-400"
          >
            GitHub ↗
          </a>
        </header>
        {children}
        <footer className="mt-16 border-t border-[var(--card-border)] pt-6 text-center text-xs text-slate-600">
          Own explanations &amp; solutions only — problem links go to leetcode.com
        </footer>
      </body>
    </html>
  );
}
