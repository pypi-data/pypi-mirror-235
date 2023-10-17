from setuptools import setup, find_packages

setup(
    name="llm-bash-helper",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "llama-cpp-python",
        "rich",
        "langchain"
    ],
    entry_points={
        'console_scripts': [
            'llm=llm.llmterm:main',
        ],
    }
)
