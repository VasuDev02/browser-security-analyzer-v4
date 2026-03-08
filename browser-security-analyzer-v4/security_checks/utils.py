
import re

def find_matches_with_lines(code, regex, issue_type):
    results = []
    lines = code.splitlines()

    for i, line in enumerate(lines, start=1):
        # NOTE: We intentionally DO NOT skip comment lines.
        if re.search(regex, line):
            results.append(
                f"[!] {issue_type} | Line {i} | Code: {line.strip()}"
            )

    return results
