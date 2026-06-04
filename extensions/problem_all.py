import re
import os
from pathlib import Path
from markdown.extensions import Extension as MDXExtension
from markdown.preprocessors import Preprocessor as MDXPreprocessor
from .utils import parse_frontmatter

_NAT_SPLIT_RE = re.compile(r"(\d+)")


def natural_sort_key(s: str):
    return [
        int(chunk) if chunk.isdigit() else chunk.lower()
        for chunk in _NAT_SPLIT_RE.split(s)
    ]


class ProblemAllExtension(MDXExtension):
    def __init__(self, problems_dir="docs/problems", **kwargs):
        self.problems_dir = Path(problems_dir)
        super().__init__(**kwargs)

    def extendMarkdown(self, md):
        md.registerExtension(self)
        md.preprocessors.register(
            ProblemAllPreprocessor(self.problems_dir), "problem_all", 175
        )


class ProblemAllPreprocessor(MDXPreprocessor):
    tag = re.compile(r"!problem_all")

    def __init__(self, problems_dir):
        super().__init__()
        self.problems_dir = problems_dir

    def run(self, lines):
        new_lines = []
        for line in lines:
            match = self.tag.search(line)
            if match:
                html = self.build_card()
                if html is not None:
                    new_lines.append(html)
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)
        return new_lines

    def build_card(self):
        rows = []

        problems = []
        for file_path in self.problems_dir.glob("*.md"):
            pid = file_path.stem
            if pid == "index":
                continue

            title, source, difficulty, link = pid, None, "?", None

            if file_path.exists():
                meta = parse_frontmatter(file_path)

                title = meta.get("title", pid) or pid
                source = meta.get("source")
                difficulty = meta.get("difficulty", "?") or "?"
                link = meta.get("link")

            problems.append(
                {
                    "pid": pid,
                    "title": title,
                    "source": source,
                    "difficulty": difficulty,
                    "link": link,
                }
            )

        problems.sort(key=lambda x: natural_sort_key(x["pid"]))

        for p in problems:
            pid = p["pid"]
            title = p["title"]
            source = p["source"]
            difficulty = p["difficulty"]
            link = p["link"]
            rows.append(
                f'-   <a href="{link}" target="_blank" rel="noopener noreferrer">**{title}**</a>'
                if link
                else title
            )
            rows.append("    ---")
            rows.append(f"    **Source**: {source}")
            rows.append(f"    **Difficulty**: {difficulty}")
            rows.append(
                f'    <a href="/problems/{pid}/" target="_blank" rel="noopener noreferrer">**View Solution** :material-open-in-new:</a>'
            )

        table = '<div class="grid cards" markdown>'
        table += "\n\n".join(rows)
        table += "\n\n</div>"
        return table


def makeExtension(**kwargs):
    return ProblemAllExtension(**kwargs)
