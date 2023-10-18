from setuptools import setup

with open('README.rst', 'r', encoding='utf-8') as f:
    ln = f.read()

setup(
    name="PyGraph_DFS",
    version="0.1",
    description="Implement of Depth First Search for a graph",
    long_description= ln,
    long_description_content_type='text/x-rst',
    license="MIT",
    author="Md. Ismiel Hossen Abir",
    packages=["PyGraph_DFS"],
    url="https://pypi.org/project/PyGraphDFS/",
    install_requires=[]
    
)