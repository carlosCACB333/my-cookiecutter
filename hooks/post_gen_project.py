import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = '\x1b[0m'
print(f'{MESSAGE_COLOR}Inicializando git...{RESET_ALL}')
subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'initial commit'])

print(f'{MESSAGE_COLOR}Git inicializado correctamente!{RESET_ALL}')
