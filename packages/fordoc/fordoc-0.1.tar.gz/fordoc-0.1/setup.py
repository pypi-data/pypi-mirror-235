from setuptools import setup, find_packages

setup(
    name="fordoc",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'fordoc=fordoc:print_meme',
        ],
    },
    author="DocBot",
    author_email="doc@twohackers.io",
    description="A simple package to print a meme message.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/fordoc",
)
