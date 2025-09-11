from subprocess import run
import hashlib as hs
import sys


deploy = run(['pyinstaller', 'main.py', '-F', '-n', 'SystemCentral'])

if sys.platform == 'win32':
    with open('dist/SystemCentral.exe', 'rb') as f:
        data = f.read()
        exec_hash = hs.sha256(data).hexdigest()
elif sys.platform == 'linux':
    with open('dist/SystemCentral', 'rb') as f:
        data = f.read()
        exec_hash = hs.sha256(data).hexdigest() 

if deploy.returncode == 0:
    print(f'Executable SHA256: {exec_hash}')
    input('Deployment succesful. Press enter to exit.')
else:
    input('WARNING: Deployment failed. Press enter to exit.')
