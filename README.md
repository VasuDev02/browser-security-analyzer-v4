# Browser Security Analyzer v3

Browser Security Analyzer v3 is a lightweight and modular JavaScript security auditing tool. It scans `.js` files for suspicious, insecure, or potentially malicious patterns.

## Features

### Suspicious JavaScript Function Detection
- eval()
- new Function()
- setTimeout("string") / setInterval("string")
- document.write()
- innerHTML usage
- window.open()

### Obfuscation Indicators
- Hex encoded strings (\x41)
- Base64 encoded strings
- Very long variable names

### Crypto & Secrets Misuse
- MD5, SHA1 detection
- Hardcoded passwords, tokens, keys

### DOM Manipulation Risks
- document.cookie modification
- Hidden iframes
- Clipboard hijacking attempts

### Network Activity Monitoring
- Insecure HTTP calls
- WebSocket connections
- Beacon API usage

### Line Number Reporting
Every detection includes:
- Issue type
- Line number
- Matching code snippet

### Recursive Folder Scanning
Scan a single JavaScript file or an entire directory.

## Project Structure

browser-security-analyzer-v3  
├── analyzer.py  
├── README.md   
└── security_checks  
    ├── utils.py  
    ├── suspicious_functions.py  
    ├── crypto_usage.py  
    ├── obfuscation_detector.py  
    ├── dom_manipulation.py  
    └── network_calls.py  

## Installation

### 1. Install Python 3.8+
python --version

Download Python if needed:  
https://www.python.org/downloads/

### 2. Extract the project folder

### 3. Open terminal inside the folder
Windows: Shift + Right-click → Open PowerShell window here  
Mac/Linux: cd browser-security-analyzer-v3

## Usage

python analyzer.py

Enter a JS file path or folder path.  
Output is saved to `report.txt`.

## Testing
Use `sample-malicious.js`.

## Extending
Add new rules inside `security_checks/`.

## License
MIT License
