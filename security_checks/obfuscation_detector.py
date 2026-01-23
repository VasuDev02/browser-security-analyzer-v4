import re

def check_obfuscation(code):
    findings=["\n=== Obfuscation Indicators ==="]
    if re.search(r"\\x[0-9A-Fa-f]{2}", code):
        findings.append("[!] Hex encoded strings detected")
    if re.search(r"[A-Za-z0-9+/]{40,}={0,2}", code):
        findings.append("[!] Base64 encoded payload detected")
    if re.search(r"var\s+[A-Za-z0-9]{25,}\s*=", code):
        findings.append("[!] Long obfuscated variable name detected")
    return "\n".join(findings)
