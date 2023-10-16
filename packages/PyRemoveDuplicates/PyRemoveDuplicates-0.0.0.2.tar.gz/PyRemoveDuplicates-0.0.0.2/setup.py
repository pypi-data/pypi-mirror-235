from setuptools import setup

with open('README.rst', 'r', encoding='utf-8') as f:
    ln = f.read()

setup(
    name="PyRemoveDuplicates",
    version="0.0.0.2",
    description="Remove all duplicates value from an array",
    long_description= ln,
    long_description_content_type='text/x-rst',
    license="MIT",
    author="Md. Ismiel Hossen Abir",
    packages=["PyRemoveDuplicates"],
    url="https://pypi.org/project/PyRemoveDuplicates/",
    install_requires=[]
    
)