from pathlib import Path
from setuptools import setup, find_packages

readme = Path(__file__).parent.joinpath('README.md').read_text()
requirements = Path(__file__).parent.joinpath('requirements.txt').read_text().splitlines()

setup(
    name='automation',
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
    url='https://github.com/FrancoisNadeau/automation_shortcuts.git',
    license='MIT License',
    author='Francois Nadeau',
    author_email='francois.nadeau.1@umontreal.ca',
    description='Short methods automating specific, yet common processes.',
    long_description=readme,
    keywords='automation docstring flat flatten size sizeof default defaults arguments args'
)
