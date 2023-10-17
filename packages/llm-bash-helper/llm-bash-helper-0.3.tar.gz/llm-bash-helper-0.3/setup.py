from setuptools import setup, find_packages

setup(
    name="llm-bash-helper",
    version="0.3",
    packages=find_packages(),
    install_requires=[
        "llama-cpp-python",
        "rich",
        "langchain"
    ],
    entry_points={
        'console_scripts': [
            'llm=llmterm.llmterm:main',
        ],
    }
)
