import re

def check_network_calls(code):
    findings=["\n=== Network Calls ==="]
    if re.search(r"http://", code):
        findings.append("[!] Insecure HTTP call detected")
    if "navigator.sendBeacon" in code:
        findings.append("[!] Beacon API usage")
    if "new WebSocket" in code:
        findings.append("[!] WebSocket connection detected")
    return "\n".join(findings)
