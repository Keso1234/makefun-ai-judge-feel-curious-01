"""Make the AI judge feel curious.

Writes one short text to /output/entry.txt.
Python 3.13, standard library only, no network, no randomness:
the same text every run.
"""

from pathlib import Path

ENTRY_TEXT = (
    "You sit at your grandmother's kitchen table, the tea gone cold, "
    "her chair still warm beside you, and the old radio she never "
    "switched off is playing a song in your voice, singing words you "
    "have not written yet, while the kettle clicks, as if it is "
    "listening too."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = ENTRY_TEXT
    if not 1 <= len(text) <= 280:
        raise ValueError(
            f"entry must be 1-280 code points, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    # Post-write check: what is on disk must be exactly the validated
    # text, UTF-8, 1-280 code points, and not only whitespace.
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    if written != text:
        raise ValueError("written entry does not match the validated text")
    if not 1 <= len(written) <= 280 or not written.strip():
        raise ValueError("written entry failed the 1-280 / whitespace gate")


if __name__ == "__main__":
    main()
