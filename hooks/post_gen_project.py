import subprocess

PROJECT_SLUG = '{{ cookiecutter.project_slug }}'

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = '\x1b[0m'
print(f'{MESSAGE_COLOR}Inicializando git...{RESET_ALL}')
subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'initial commit'])
print(f'{MESSAGE_COLOR}Git inicializado correctamente!{RESET_ALL}')

print(f'{MESSAGE_COLOR}creando entorno virtual...{RESET_ALL}')
subprocess.call(['conda', 'env', 'create', '--file', 'environment.yml'])
print(f'{MESSAGE_COLOR}entorno creado exitosamente !!{RESET_ALL}')

print(f'{MESSAGE_COLOR}activando entorno...{RESET_ALL}')
subprocess.call(['call', 'conda.bat', 'activate'])
subprocess.call(['conda', 'activate', PROJECT_SLUG])
print(f'{MESSAGE_COLOR}entorno en ejcucion !!{RESET_ALL}')
