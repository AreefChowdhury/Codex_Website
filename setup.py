echo "from setuptools import setup, find_packages

setup(
    name=\"Codex-Website\",
    version=\"0.1\",
    packages=find_packages(),
    install_requires=[
        \"requests\",
        \"numpy\",
    ],
    entry_points={
        \"console_scripts\": [
            \"codex_website=src.main:main\",
        ],
    },
)" > setup.py
