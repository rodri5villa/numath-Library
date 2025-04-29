from setuptools import setup, find_packages

def parse_requirements(filename):
    """Lee requirements.txt y filtra líneas no válidas como '-e'."""
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('-e')]

setup(
    name='numath',  # Nombre del paquete
    version='0.1.0',  # Versión inicial del paquete
    author='Rodrigo Villa',  # Tu nombre como autor
    author_email='rodrigo.villa@alumnos.uneatlantico.es',  # Tu correo electrónico
    description='Librería de operaciones matemáticas para Matemática Numérica',
    long_description=open('README.md', 'r', encoding='utf-8').read(),  # Leer la descripción larga desde README.md
    long_description_content_type='text/markdown',  # Especifica que el README.md usa Markdown
    url='https://github.com/rodri5villa/numath-Library',  # URL del repositorio en GitHub
    license='MIT',  # Especifica la licencia (MIT en este caso, que es permisiva)
    packages=find_packages(),  # Encuentra automáticamente todos los paquetes dentro del directorio
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'Topic :: Scientific/Engineering :: Mathematics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',  # Requiere Python 3.10 o superior
    install_requires=parse_requirements('requirements.txt'),  # Dependencias listadas en requirements.txt
    extras_require={
        'dev': ['pytest>=6.0'],  # Dependencias para desarrollo
        'test': ['pytest'],  # Dependencias para testing
    },
    include_package_data=True,  # Incluye archivos adicionales como README.md y LICENSE
)