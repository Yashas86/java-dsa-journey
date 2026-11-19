from pathlib import Path
import json
import shutil
import re

ROOT = Path(__file__).resolve().parent
JAVA_DIR = ROOT / "java"
MAPPING_FILE = ROOT / "problem_topics.json"

DEFAULT_TOPICS = {
    "0001-two-sum": "Hashing",
    "0003-longest-substring-without-repeating-characters": "SlidingWindow",
    "0014-longest-common-prefix": "Strings",
    "0143-reorder-list": "LinkedList",
}

def main():
    mapping = DEFAULT_TOPICS.copy()
    if MAPPING_FILE.exists():
        mapping.update(json.loads(MAPPING_FILE.read_text(encoding="utf-8")))

    if not JAVA_DIR.exists():
        print("ERROR: Save this script in the root of java-dsa-journey (beside the java folder).")
        return

    allowed = {"Arrays","Strings","Hashing","TwoPointers","SlidingWindow","BinarySearch",
               "LinkedList","Stack","Queue","Trees","Heap","Backtracking","Graphs",
               "DynamicProgramming","Greedy","BitManipulation"}
    copied = skipped = 0

    for problem_dir in sorted(p for p in JAVA_DIR.iterdir() if p.is_dir()):
        slug = problem_dir.name
        topic = mapping.get(slug)
        if not topic:
            print(f"UNMAPPED: {slug} — add it to problem_topics.json")
            skipped += 1
            continue
        if topic not in allowed:
            print(f"INVALID TOPIC: {topic} for {slug}")
            skipped += 1
            continue

        m = re.match(r"(\\d+)-(.+)", slug)
        filename = f"LC{m.group(1)}_{re.sub(r'[^A-Za-z0-9_-]+', '_', m.group(2)).strip('_')}" if m else slug
        destination = ROOT / topic / filename
        destination.mkdir(parents=True, exist_ok=True)

        for source in problem_dir.iterdir():
            if source.is_file() and source.suffix.lower() in {".java", ".md"}:
                target = destination / source.name
                if target.exists():
                    print(f"EXISTS (not overwritten): {target.relative_to(ROOT)}")
                    continue
                shutil.copy2(source, target)
                copied += 1
        print(f"COPIED: {slug} -> {topic}/{filename}")

    print(f"Finished. Copied {copied} file(s); skipped/unmapped {skipped} problem(s).")
    print("Original LeetHub files in java/ were not changed.")

if __name__ == "__main__":
    main()
