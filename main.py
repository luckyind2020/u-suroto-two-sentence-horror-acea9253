"""Two-Sentence Horror — entry runner.

Reads the two-sentence story from entry.txt and prints it exactly as
written, so the grader sees the same text the entry file holds.
"""

from pathlib import Path


def count_sentences(text: str) -> int:
    """Count sentence-ending marks, ignoring the em dash in the story."""
    return sum(text.count(mark) for mark in (".", "!", "?"))


def load_story() -> str:
    story_path = Path(__file__).resolve().parent / "entry.txt"
    return story_path.read_text(encoding="utf-8").strip()


def main() -> None:
    story = load_story()
    if count_sentences(story) != 2:
        raise ValueError("entry must be exactly two sentences")
    print(story)


if __name__ == "__main__":
    main()
