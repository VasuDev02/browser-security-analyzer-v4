import os
from security_checks.suspicious_functions import check_suspicious_functions
from security_checks.obfuscation_detector import check_obfuscation
from security_checks.crypto_usage import check_crypto_issues
from security_checks.dom_manipulation import check_dom_manipulation
from security_checks.network_calls import check_network_calls

REPORT_FILE = "report.txt"

def analyze_code(code):
    results = []
    results.append(check_suspicious_functions(code))
    results.append(check_obfuscation(code))
    results.append(check_crypto_issues(code))
    results.append(check_dom_manipulation(code))
    results.append(check_network_calls(code))
    return "\n".join(results)

def analyze_file(js_path):
    with open(js_path,"r",encoding="utf-8") as f:
        code=f.read()
    return f"\n\n===== FILE: {js_path} =====\n" + analyze_code(code)

def analyze_folder(folder):
    rep=""
    for root,dirs,files in os.walk(folder):
        for f in files:
            if f.endswith(".js"):
                p=os.path.join(root,f)
                print("[+] Analyzing:",p)
                rep+=analyze_file(p)
    return rep if rep else "[!] No JS files found."

def save_report(content):
    with open(REPORT_FILE,"w",encoding="utf-8") as f: f.write(content)

def main():
    target=input("Enter JS file or folder path to analyze: ").strip()
    if not os.path.exists(target):
        print("[!] Invalid path"); return
    if os.path.isfile(target):
        rep=analyze_file(target)
    else:
        rep=analyze_folder(target)
    save_report(rep)
    print("\n[✓] Analysis complete!\nReport saved:",REPORT_FILE)

if __name__=="__main__":
    main()