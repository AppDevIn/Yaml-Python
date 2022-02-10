import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="Yaml8",
    version="0.1.1",
    author="AppDevIn Sliver",
    author_email=" teamprojectlive@example.com",
    description="Python package to make getting yaml easier and cleaner",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AppDevIn/Yaml-Python",
    project_urls={
        "Bug Tracker": "https://github.com/AppDevIn/Yaml-Python/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
      "PyYAML==6.0"
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)