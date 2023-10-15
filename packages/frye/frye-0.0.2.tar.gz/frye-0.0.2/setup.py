from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='frye',
    version='0.0.2',
    description='LLM toolkit',
    long_description=long_description,
    long_description_content_type="text/markdown", 
    packages=find_packages(),
    install_requires=[
        'fastapi',
        'pydantic',
        'langchain',
        'transformers',
        'torch',
        'numpy',
        'pandas',
        'xformers',
        'sentencepiece',
        'accelerate>=0.20.3',
        'bitsandbytes',
        'sentence_transformers',
        'attention_sinks',
        'uvicorn',
        'psycopg[binary]',
        'sqlalchemy',
        'huggingface_hub',
        'faiss-cpu'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    license='Apache-2.0', 
    python_requires='>=3.6'
)
