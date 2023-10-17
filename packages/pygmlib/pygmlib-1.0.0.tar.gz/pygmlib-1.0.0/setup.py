from setuptools import Extension, setup
import glob

sources = []
sources += glob.glob("src/*.cpp")
sources += glob.glob("gmlib/gmlib/**/*.cpp", recursive=True)

ext_modules = [
    Extension(
        name="pygmlib",
        sources=sources,
        include_dirs=["gmlib/", "pybind11/include/"],
    )
]

setup(
    name="pygmlib",
    version="1.0.0",
    description="python bind of GMLib",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type= "text/markdown",
    author="oldprincess",
    author_email="zirui.gong@foxmail.com",
    url="https://github.com/oldprincess/pygmlib",
    install_requires=["setuptools>=42"],
    ext_modules=ext_modules,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False,
    python_requires=">=3.7",
)
