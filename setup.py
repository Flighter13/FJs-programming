import setuptools
with open("README.md", "r" as fh:
          description = fh.read()

setuptools.setup(
    name="Fighter",
    version="0.0.1",
    author="Joshua Parr",
    author_email="jdp37803@email.vccs.edu",
    packages=["fjosh"],
    description="A programming rendition of modern U.S. fighter jet operating systems",
    long_description=description,
    long_description_content_type="text/markdown",
    url=None,
    license='MIT',
    python_requires='>=3.8',
    install_requires=[]
)
