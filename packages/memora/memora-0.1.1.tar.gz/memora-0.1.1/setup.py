from setuptools import setup, find_packages

setup(
    name="memora",
    version="0.1.1",
    packages=find_packages(),
    author="Memora",
    author_email="hello@usememora.app",
    description="Memora's official Python library",
    # long_description="A longer description of your package.",
    # long_description_content_type="text/markdown",
    url="https://docs.usememora.app/python",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests',
    ],
    python_requires='>=3.6',
)
