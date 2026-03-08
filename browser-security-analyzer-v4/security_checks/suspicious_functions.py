
from .utils import find_matches_with_lines

def check_suspicious_functions(code):

    patterns = {
        r"\beval\s*\(": "Dangerous eval() usage",
        r"new Function": "Dynamic Function() usage",
        r"setTimeout\s*\(\s*['\"]": "setTimeout string execution",
        r"setInterval\s*\(\s*['\"]": "setInterval string execution",
        r"document\.write": "document.write usage"
    }

    findings = ["\n=== Suspicious Functions ==="]

    for pattern, issue in patterns.items():
        matches = find_matches_with_lines(code, pattern, issue)
        findings.extend(matches)

    if len(findings) == 1:
        findings.append("No suspicious patterns detected.")

    return "\n".join(findings)
