from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='vectorlite',
    version='0.0.8',
    description='Lightweight vector search engine',
    long_description=long_description,
    long_description_content_type="text/markdown", 
    packages=find_packages(),
    install_requires=[
        "numpy",
        "sentence_transformers",
        "torch",
        "hnswlib",
        "fastapi",
        "uvicorn"
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    license='Apache-2.0', 
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'serve=vectorlite.server:main',
        ],
    },
)
