from setuptools import find_packages
from setuptools import setup


requirements = []
try:
    with open('./requirements.txt', 'r') as file:
        requirements = [r.strip() for r in file.readlines()]
except FileNotFoundError:
    print('Warning! Requirements were not loaded')

setup(
    name='app',
    version='0.0.1.dev1',
    description='API',
    platforms=['POSIX'],
    install_requires=requirements,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
        ]
    }
)