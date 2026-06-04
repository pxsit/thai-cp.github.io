import yaml
from pathlib import Path
from typing import Dict, Any


def parse_frontmatter(file_path: Path | str) -> Dict[str, Any]:
    """Reads a markdown file and extracts its YAML frontmatter."""
    file_path = Path(file_path)
    if not file_path.exists():
        return {}

    try:
        with open(file_path, encoding="utf-8") as f:
            lines = f.readlines()
    except OSError:
        return {}

    if not lines or lines[0].strip() != "---":
        return {}

    meta_lines = []
    for line in lines[1:]:
        if line.strip() == "---":
            break
        meta_lines.append(line)

    try:
        return yaml.safe_load("".join(meta_lines)) or {}
    except yaml.YAMLError:
        return {}
