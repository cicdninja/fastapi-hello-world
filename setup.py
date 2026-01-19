from setuptools import setup, find_packages

setup(
    name="fastapi-hello-world",
    version="0.1.0",
    description="A simple FastAPI Hello World application",
    author="CICD NINJA",
    author_email="cicd.ninja@gmail.com",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.104.1",
        "uvicorn[standard]==0.24.0"
    ],
    extras_require={
        "test": [
            "pytest==7.4.3",
            "httpx==0.25.2"
        ]
    },
    python_requires=">=3.7",
    include_package_data=True,
)
