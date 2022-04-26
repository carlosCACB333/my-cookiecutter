import sys

project_slug = '{{cookiecutter.project_slug}}'
if project_slug.startswith('.'):
    print('El nombre del projecto no puede empezar con punto')
    sys.exit(1)
print(f'Creando proyecto {project_slug}')
