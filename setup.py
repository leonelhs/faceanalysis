from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='face analysis',
    version='0.1.0',
    author='leonel hernandez',
    author_email='leonelhs@gmail.com',
    description='Library for facial region detection and extraction',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/leonelhs/faceanalysis',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        "onnx>=1.19.0",
        "onnxruntime>=1.22.1",
        "opencv-python>=4.12.0.88",
        "scikit-image>=0.25.2",
        "huggingface-hub>=0.35.3"
    ],
)


