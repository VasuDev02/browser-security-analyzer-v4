import re

def check_dom_manipulation(code):
    findings=["\n=== DOM Manipulation Risks ==="]
    if "document.cookie" in code:
        findings.append("[!] Cookie modification detected")
    if re.search(r"<iframe.*hidden|style=.*display:\s*none", code):
        findings.append("[!] Hidden iframe detected")
    if "navigator.clipboard.writeText" in code:
        findings.append("[!] Clipboard write detected")
    return "\n".join(findings)
