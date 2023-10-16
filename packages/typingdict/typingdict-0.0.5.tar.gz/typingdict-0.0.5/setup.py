from setuptools import find_packages, setup

with open("README.rst", mode="r", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt", mode="r", encoding="utf-8") as f:
    requirements = [*map(str.strip, f.read().splitlines())]

author = "am230"
name = "typingdict"
py_modules = [name]

setup(
    name=name,
    version="0.0.5",
    keywords=["Automation", "Typing"],
    description="Generate TypedDict Automatically",
    long_description=long_description,
    license="MIT Licence",
    long_description_content_type="text/x-rst",
    packages=find_packages(),
    requires=requirements,
    url=f"https://github.com/{author}/{name}",
    author=author,
    py_modules=py_modules,
    platforms="any",
)
