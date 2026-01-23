from .utils import find_matches_with_lines

def check_crypto_issues(code):
    patterns={
        r"\bMD5\b|\bmd5\b": "Weak Hash MD5",
        r"\bSHA1\b|\bsha1\b": "Weak Hash SHA1",
        r"(secret|key|token|password)\s*=\s*['\"]": "Hardcoded Secret"
    }
    findings=["\n=== Crypto Issues ==="]
    results=[]
    for p,issue in patterns.items():
        results+=find_matches_with_lines(code,p,issue)
    if not results:
        findings.append("No crypto issues.")
    else:
        for r in results:
            findings.append(f"[!] {r['type']} | Line {r['line']} | Code: {r['match']}")
    return "\n".join(findings)
