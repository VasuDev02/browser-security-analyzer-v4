from .utils import find_matches_with_lines

def check_obfuscation(code):

    patterns = {
        r"\\x[0-9A-Fa-f]{2}": "Hex encoded string detected",
        r"[A-Za-z0-9+/]{40,}={0,2}": "Base64 encoded payload detected",
        r"var\s+[A-Za-z0-9]{25,}\s*=": "Suspicious long variable name (possible obfuscation)"
    }

    findings = ["\n=== Obfuscation Indicators ==="]

    for pattern, issue in patterns.items():
        matches = find_matches_with_lines(code, pattern, issue)
        findings.extend(matches)

    if len(findings) == 1:
        findings.append("No obfuscation patterns detected.")

    return "\n".join(findings)
