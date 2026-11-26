"""One Line to Your Younger Self - variant 2 (job choice angle).

Writes a single original line to /output/entry.txt (or the directory
named by MAKEFUN_OUTPUT_DIR). Pure stdlib, deterministic, no network.
"""

import os
import sys

LINE = (
    "Take the boring job with the window and the quiet afternoons, "
    "not the flashy one with the free snacks and the ping-pong table, "
    "you'll trade three good years for a branded hoodie."
)


def main() -> int:
    text = LINE

    # Validate the gate contract: one line, 1-200 Unicode code points,
    # not only whitespace, no newline anywhere.
    if not text or not text.strip():
        print("error: entry text is empty or only whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: entry text must be a single line", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(
            f"error: entry text is {len(text)} chars, over the 200 limit",
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
