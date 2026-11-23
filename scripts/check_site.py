"""Check that docs/index.html has its six sections and that its links resolve.

Usage (from the repository root):  python scripts/check_site.py [page.html]

Every image and local link must point at an existing file. Links to this
repository's GitHub pages are mapped back to files in the repository and
checked the same way. Other external links are not fetched. Exits 1 on any
problem, 0 otherwise.
"""

import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO_URL = "https://github.com/jeremy-evert/sorting_and_searching/"
SECTIONS = ["result", "theory", "built", "code", "agents", "more"]


class PageReader(HTMLParser):
    """Collects section ids, image sources, link targets and image alt text."""

    def __init__(self):
        """Start with empty lists."""
        super().__init__()
        self.ids = []
        self.images = []
        self.links = []
        self.images_without_alt = []
        self.external_resources = []

    def handle_starttag(self, tag, attrs):
        """Record what this tag points at."""
        attributes = dict(attrs)
        if tag == "section" and attributes.get("id"):
            self.ids.append(attributes["id"])
        if tag == "img":
            self.images.append(attributes.get("src", ""))
            if not attributes.get("alt", "").strip():
                self.images_without_alt.append(attributes.get("src", ""))
        if tag == "a" and attributes.get("href"):
            self.links.append(attributes["href"])
        if tag in ("script", "link") and (attributes.get("src") or attributes.get("href", "")).startswith("http"):
            self.external_resources.append(attributes.get("src") or attributes.get("href"))


def resolve(target, page_dir, root):
    """Return the repository file a link means, or None if it is not checkable."""
    target = target.split("#")[0].split("?")[0]
    if not target:
        return None
    if target.startswith(REPO_URL):
        rest = target[len(REPO_URL):]
        for prefix in ("blob/main/", "tree/main/"):
            if rest.startswith(prefix):
                return root / rest[len(prefix):]
        return None
    if "://" in target or target.startswith("mailto:"):
        return None
    return (page_dir / target).resolve()


def check(page, root):
    """Return a list of problem descriptions for the page."""
    reader = PageReader()
    reader.feed(page.read_text(encoding="utf-8"))
    problems = []
    for section in SECTIONS:
        if section not in reader.ids:
            problems.append(f"missing section id={section!r}")
    if reader.ids != [s for s in SECTIONS if s in reader.ids]:
        problems.append(f"sections out of order: {reader.ids}")
    for src in reader.images_without_alt:
        problems.append(f"image without alt text: {src}")
    for src in reader.external_resources:
        problems.append(f"external script or stylesheet: {src}")
    for target in reader.images + reader.links:
        if target.startswith("http") and not target.startswith(REPO_URL):
            if target in reader.images:
                problems.append(f"external image: {target}")
            continue
        path = resolve(target, page.parent, root)
        if path is not None and not path.exists():
            problems.append(f"broken link or image: {target}")
    return problems


def main(argv):
    """Check the page and return the exit code."""
    page = Path(argv[1]) if len(argv) > 1 else ROOT / "docs" / "index.html"
    problems = check(page, ROOT)
    for problem in problems:
        print("PROBLEM:", problem)
    if problems:
        print(f"FAILED: {len(problems)} problem(s).")
        return 1
    print("OK: six sections present, every image has alt text, every local image and link resolves. "
          "Links to other sites were not fetched, and alt text was not checked for accuracy.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
