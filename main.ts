// news-image-20261125 entry: a one-day world-news image for 25 November 2026.
// The image itself (entry.png, 1024x1024, drawn before submission from the
// day's verified stories) is the entry; this program only places it where
// the grader looks for it, at /output/entry.png, with no network access.
import { copyFileSync, existsSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const target = join(outDir, "entry.png");

if (!existsSync(outDir)) {
  mkdirSync(outDir, { recursive: true });
}

const source = join(here, "entry.png");
if (!existsSync(source)) {
  throw new Error(`missing entry image: ${source}`);
}

copyFileSync(source, target);
console.log(`wrote ${target}`);
