
from .utils import find_matches_with_lines

def check_crypto_issues(code):

    patterns = {
        r"\bMD5\b": "Weak Hash MD5",
        r"\bSHA1\b": "Weak Hash SHA1",
        r"(secret|key|token|password)\s*=": "Hardcoded Secret"
    }

    findings = ["\n=== Crypto Issues ==="]

    for pattern, issue in patterns.items():
        matches = find_matches_with_lines(code, pattern, issue)
        findings.extend(matches)

    if len(findings) == 1:
        findings.append("No crypto issues detected.")

    return "\n".join(findings)
