import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pycli",
    version="0.0.2",
    author="Noah G. Wood",
    author_email="ngwood111@gmail.com",
    description="Dead simple Command Line Interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NoahGWood/PyCLI",
    keywords = ['CLI', 'command line', 'interface', 'UI', 'input', 'threaded cli', 'easy', 'beginner friendly'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>3.6',
)
