# \# 🔍 Browser Security Analyzer v3

# 

# Browser Security Analyzer v3 is a lightweight command-line tool designed to scan JavaScript files for suspicious, insecure, or potentially malicious behavior.  

# This version includes a fully modular scanning engine, line-number detection, pattern-matching utilities, and recursive folder scanning.

# 

# Perfect for:

# \- Security Analysts

# \- Chrome Extension Reviewers

# \- Penetration Testers

# \- Web Developers validating third-party scripts

# 

# ---

# 

# \## 🚀 Features

# 

# \### ✔ Suspicious JavaScript Function Detection

# Detects dangerous usage like:

# \- `eval()`

# \- `new Function()`

# \- `setTimeout("string")`

# \- `document.write()`

# \- `innerHTML =`

# \- `window.open()`

# 

# \### ✔ Obfuscation Indicators

# \- Hex-encoded strings (`\\x41`)

# \- Base64 strings

# \- Overly long variable names (possible malware obfuscation)

# 

# \### ✔ Crypto Abuse Detection

# \- Weak hashing (MD5, SHA1)

# \- Hardcoded secrets, tokens, passwords, or API keys

# 

# \### ✔ DOM Manipulation Risks

# \- Cookie modifications

# \- Hidden iframes

# \- Clipboard hijacking

# 

# \### ✔ Network Request Monitoring

# \- Insecure HTTP calls

# \- WebSocket usage

# \- Beacon API (exfiltration risk)

# 

# \### ✔ Line-Number Enabled Reports

# Every finding includes:

# \- Pattern type

# \- Line number

# \- Matched code

# 

# \### ✔ Recursive Folder Scanning

# Scan \*hundreds\* of JS files at once.

# 

# ---

# 

# \## 📁 Project Structure

# 



