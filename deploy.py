from subprocess import run

deploy = run(['pyinstaller', 'main.py', '-F', '-n', 'AutomationStuff'])

if deploy.returncode == 0:
    input('Delpoyment succesful. Press enter to exit.')
else:
    input('WARNING: Delpoyment failed. Press enter to exit.')