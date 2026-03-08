from .utils import find_matches_with_lines

def check_dom_manipulation(code):

    patterns = {
        r"document\.cookie": "document.cookie usage detected",
        r"<iframe.*display\s*:\s*none": "Hidden iframe detected",
        r"navigator\.clipboard\.writeText": "Clipboard write detected"
    }

    findings = ["\n=== DOM Manipulation Risks ==="]

    for pattern, issue in patterns.items():
        matches = find_matches_with_lines(code, pattern, issue)
        findings.extend(matches)

    if len(findings) == 1:
        findings.append("No DOM risks detected.")

    return "\n".join(findings)