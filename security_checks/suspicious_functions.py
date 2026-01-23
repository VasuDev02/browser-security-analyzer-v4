from .utils import find_matches_with_lines

def check_suspicious_functions(code):
    patterns = {
        r"\beval\s*\(": "Dangerous eval() usage",
        r"new Function": "Dynamic Function() constructor",
        r"setTimeout\s*\(\s*['\"]": "setTimeout string execution",
        r"setInterval\s*\(\s*['\"]": "setInterval string execution",
        r"document\.write": "document.write usage",
        r"innerHTML\s*=": "innerHTML assignment",
        r"window\.open": "window.open usage"
    }

    findings=["\n=== Suspicious Functions ==="]
    results=[]

    for pattern, issue in patterns.items():
        results.extend(find_matches_with_lines(code, pattern, issue))

    if not results:
        findings.append("No suspicious patterns found.")
    else:
        for r in results:
            findings.append(
                f"[!] {r['type']} | Line {r['line']} | Code: {r['match']}"
            )

    return "\n".join(findings)
