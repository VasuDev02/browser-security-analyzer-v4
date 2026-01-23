def find_matches_with_lines(code, regex, issue_type):
    import re
    results=[]
    lines=code.split("\n")
    pat=re.compile(regex)
    for i,line in enumerate(lines, start=1):
        for m in pat.finditer(line):
            results.append({"line":i,"match":m.group(0),"type":issue_type})
    return results
