from setuptools import setup, find_packages

setup(
    name="enumerate-iam",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'boto3',
        'botocore'
    ],
    entry_points={
        "console_scripts": [
            "enumerate-iam=enumerate_iam.cli:main",  # Replace with your actual command and function
        ],
    },
)
