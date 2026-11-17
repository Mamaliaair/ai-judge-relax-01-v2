"""Make the AI judge relax — ai-judge-relax-01.

Writes one short text to /output/entry.txt: a quiet evening scene
that slows the reader down. The calm comes from the scene itself —
a dog asleep, the light coming in low, the day's small jobs done —
never from telling anyone to relax.
"""

import os

TEXT = """The dog has been asleep on the rug by the door for an hour.
His ear twitches once, and then it doesn't.
Evening comes in low through the window and lays one long line of gold along the floor, stopping just short of his paws.
Outside, the garden chairs are being stacked for the night. Their metal legs click against the stone, one by one, until the clicking stops.
The house settles. The dog breathes in, slow, and out, slower still.
The light stays where it is. So does he."""

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
