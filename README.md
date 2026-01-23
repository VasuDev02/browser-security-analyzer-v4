🔍 Browser Security Analyzer v3

A modular and lightweight JavaScript security auditing tool that scans .js files for suspicious, insecure, or potentially malicious patterns.
Designed for Security Analysts, Penetration Testers, and Developers who review browser scripts and Chrome extensions.

✨ Key Features
🛑 1. Suspicious JavaScript Functions Detection

Identifies risky code patterns such as:

eval()

new Function()

setTimeout("string"), setInterval("string")

document.write()

Unsafe innerHTML usage

window.open()

🕵️ 2. Obfuscation Indicators

Recognizes hidden or encoded payloads:

Hex-encoded values (\x41)

Base64 payloads

Overly long variable names (indicative of malware obfuscation)

🔐 3. Crypto & Secret Misuse

Flags:

MD5 and SHA1 (weak hashing algorithms)

Hardcoded API keys, tokens, passwords

📌 4. DOM Manipulation Risks

Detects:

Cookie manipulation (document.cookie)

Hidden iframes

Clipboard hijacking attempts

🌐 5. Network Activity Monitoring

Alerts on:

Insecure HTTP calls

WebSocket connections

Beacon API usage (data exfiltration risk)

📄 6. Line-Number Reporting

Each finding includes:

Issue type

Line number

Extracted code snippet

📂 7. Recursive Folder Scanning

Scan one file or an entire folder of .js files.

📁 Project Structure
browser-security-analyzer-v3/
│
├── analyzer.py
├── README.md
├── sample-malicious.js
│
└── security_checks/
    ├── utils.py
    ├── suspicious_functions.py
    ├── crypto_usage.py
    ├── obfuscation_detector.py
    ├── dom_manipulation.py
    └── network_calls.py

🛠️ Installation & Setup
1. Install Python 3.8+

Check version:

python --version


If not installed:
https://www.python.org/downloads/

2. Extract the Project Folder
browser-security-analyzer-v3/

3. Open Terminal / CMD

Windows:
Shift + Right-click → Open PowerShell here
Mac/Linux:

cd browser-security-analyzer-v3

▶️ Usage

Run the analyzer:

python analyzer.py


Enter the path of:

a single JS file

or an entire folder

Output will be saved to:

report.txt

🧪 Testing

Use the included file:

sample-malicious.js

🧩 Extending the Tool

Add new rules by editing:

security_checks/


Possible upgrades:

Severity scoring

HTML/JSON export

CLI arguments

Chrome extension support

🤝 Contributing

Pull requests are welcome.

📜 License

MIT License.
