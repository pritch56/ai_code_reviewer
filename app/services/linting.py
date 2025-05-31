import subprocess

def run_linting(code: str):
    with open("temp_code.py", "w") as f:
        f.write(code)
    
    result = subprocess.run(["flake8", "temp_code.py"], capture_output=True, text=True)
    return result.stdout.splitlines()
