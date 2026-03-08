from .utils import find_matches_with_lines

def check_network_calls(code):

    patterns = {
        r"http://": "Insecure HTTP request detected",
        r"navigator\.sendBeacon": "Beacon API usage detected",
        r"new WebSocket": "WebSocket connection detected"
    }

    findings = ["\n=== Network Calls ==="]

    for pattern, issue in patterns.items():
        matches = find_matches_with_lines(code, pattern, issue)
        findings.extend(matches)

    if len(findings) == 1:
        findings.append("No suspicious network calls detected.")

    return "\n".join(findings)