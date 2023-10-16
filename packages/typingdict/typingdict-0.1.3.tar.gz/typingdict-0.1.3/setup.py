from setuptools import find_packages, setup

with open("README.rst", mode="r", encoding="utf-8") as f:
    long_description = f.read()

author = "am230"
name = "typingdict"
version = "0.1.3"
py_modules = [name]

setup(
    name=name,
    version=version,
    keywords=["Automation", "Typing"],
    description="Generate TypedDict Automatically",
    long_description=long_description,
    license="MIT Licence",
    long_description_content_type="text/x-rst",
    packages=find_packages(),
    requires=["strinpy", "astor", "click"],
    url=f"https://github.com/{author}/{name}",
    author=author,
    py_modules=py_modules,
    platforms="any",
)
