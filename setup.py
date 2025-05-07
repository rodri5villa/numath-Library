from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('-e')]

try:
    with open('README.md', 'r', encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ''

setup(
    name='numath',
    version='0.1.0',
    author='Rodrigo Villa',
    author_email='rodrigo.villa@alumnos.uneatlantico.es',
    description='Librería de operaciones matemáticas para Matemática Numérica',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/rodri5villa/numath-Library',
    license='MIT',
    packages=find_packages(),  # o ['numath'] si tu módulo está en una carpeta numath/
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'Topic :: Scientific/Engineering :: Mathematics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
    install_requires=parse_requirements('requirements.txt'),
    extras_require={
        'dev': ['pytest>=6.0'],
        'test': ['pytest'],
    },
    include_package_data=True,
)
