import subprocess
import json

def analyze_complexity(code: str):
    with open("temp_code.py", "w") as f:
        f.write(code)
    
    result = subprocess.run(["radon", "cc", "temp_code.py", "-s", "-j"], capture_output=True, text=True)
    return json.loads(result.stdout)
