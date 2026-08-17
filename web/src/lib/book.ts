import fs from "fs";
import path from "path";

export interface Section {
  id: string;
  title: string;
  pdf: number;
}

export interface Chapter {
  id: string;
  title: string;
  pdf: number;
  related?: { href: string; label: string }[];
}

export interface Part {
  id: string;
  title: string;
  chapters: Chapter[];
}

export const PARTS: Part[] = [
  {
    id: "I",
    title: "Foundations",
    chapters: [
      { id: "1", title: "The Role of Algorithms in Computing", pdf: 26 },
      { id: "2", title: "Getting Started", pdf: 37 },
      { id: "3", title: "Growth of Functions", pdf: 64 },
      { id: "4", title: "Divide-and-Conquer", pdf: 86, related: [{ href: "/problems", label: "dynamic/0053_maximum-subarray.py" }] },
      { id: "5", title: "Probabilistic Analysis and Randomized Algorithms", pdf: 135 },
    ],
  },
  {
    id: "II",
    title: "Sorting and Order Statistics",
    chapters: [
      { id: "6", title: "Heapsort", pdf: 172, related: [{ href: "/problems", label: "queue/ — 0215, 0703, 0973, 1046 are heap problems" }] },
      { id: "7", title: "Quicksort", pdf: 191 },
      { id: "8", title: "Sorting in Linear Time", pdf: 212 },
      { id: "9", title: "Medians and Order Statistics", pdf: 234, related: [{ href: "/problems", label: "queue/0215 — k-th largest via heap (quickselect's cousin)" }] },
    ],
  },
  {
    id: "III",
    title: "Data Structures",
    chapters: [
      { id: "10", title: "Elementary Data Structures", pdf: 253, related: [{ href: "/problems", label: "stacks/, queue/, linked_list/" }] },
      { id: "11", title: "Hash Tables", pdf: 274, related: [{ href: "/problems/0003", label: "#3 Longest Substring" }] },
      { id: "12", title: "Binary Search Trees", pdf: 307, related: [{ href: "/problems", label: "trees/" }] },
      { id: "13", title: "Red-Black Trees", pdf: 329 },
      { id: "14", title: "Augmenting Data Structures", pdf: 360 },
    ],
  },
  {
    id: "IV",
    title: "Advanced Design and Analysis Techniques",
    chapters: [
      { id: "15", title: "Dynamic Programming", pdf: 380, related: [{ href: "/problems/0198", label: "#198 House Robber" }] },
      { id: "16", title: "Greedy Algorithms", pdf: 435, related: [{ href: "/problems", label: "greedy/, intervals/" }] },
      { id: "17", title: "Amortized Analysis", pdf: 472 },
    ],
  },
  {
    id: "V",
    title: "Advanced Data Structures",
    chapters: [
      { id: "18", title: "B-Trees", pdf: 505 },
      { id: "19", title: "Fibonacci Heaps", pdf: 526 },
      { id: "20", title: "van Emde Boas Trees", pdf: 552 },
      { id: "21", title: "Data Structures for Disjoint Sets", pdf: 582, related: [{ href: "/problems", label: "union-find/" }] },
    ],
  },
  {
    id: "VI",
    title: "Graph Algorithms",
    chapters: [
      { id: "22", title: "Elementary Graph Algorithms", pdf: 610, related: [{ href: "/problems/0542", label: "#542 01 Matrix (BFS)" }] },
      { id: "23", title: "Minimum Spanning Trees", pdf: 645 },
      { id: "24", title: "Single-Source Shortest Paths", pdf: 664, related: [{ href: "/problems", label: "graphs/" }] },
      { id: "25", title: "All-Pairs Shortest Paths", pdf: 705 },
      { id: "26", title: "Maximum Flow", pdf: 729 },
    ],
  },
  {
    id: "VII",
    title: "Selected Topics",
    chapters: [
      { id: "27", title: "Multithreaded Algorithms", pdf: 793 },
      { id: "28", title: "Matrix Operations", pdf: 834 },
      { id: "29", title: "Linear Programming", pdf: 864 },
      { id: "30", title: "Polynomials and the FFT", pdf: 919 },
      { id: "31", title: "Number-Theoretic Algorithms", pdf: 947, related: [{ href: "/problems", label: "maths/" }] },
      { id: "32", title: "String Matching", pdf: 1006, related: [{ href: "/problems/0003", label: "strings/, sliding_windows/" }] },
      { id: "33", title: "Computational Geometry", pdf: 1035 },
      { id: "34", title: "NP-Completeness", pdf: 1069 },
      { id: "35", title: "Approximation Algorithms", pdf: 1127 },
    ],
  },
  {
    id: "VIII",
    title: "Appendix: Mathematical Background",
    chapters: [
      { id: "A", title: "Summations", pdf: 1166 },
      { id: "B", title: "Sets, Etc.", pdf: 1179 },
      { id: "C", title: "Counting and Probability", pdf: 1204 },
      { id: "D", title: "Matrices", pdf: 1238 },
    ],
  },
];

const NOTES_DIR = path.join(process.cwd(), "content/book");

export function getChapters(): Chapter[] {
  return PARTS.flatMap((p) => p.chapters);
}

export function getChapter(id: string): { chapter: Chapter; part: Part } | undefined {
  for (const part of PARTS) {
    const chapter = part.chapters.find((c) => c.id === id);
    if (chapter) return { chapter, part };
  }
}

const notesFile = (id: string) => (/^\d$/.test(id) ? id.padStart(2, "0") : id) + ".md";

export function getNotes(id: string): string | null {
  const file = path.join(NOTES_DIR, notesFile(id));
  if (!fs.existsSync(file)) return null;
  return fs.readFileSync(file, "utf8");
}

export function hasNotes(id: string): boolean {
  return fs.existsSync(path.join(NOTES_DIR, notesFile(id)));
}

export const PDF_OFFSET = 21; // printed page + 21 = PDF page
