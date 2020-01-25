from setuptools import find_packages, setup
import os

README = open(os.path.dirname(__file__), "README.md", "r").read()

setup(
    name="robotframework-ls",
    version="0.0.1",
    description="VSCode extension support for Robot Framework",
    long_description=README,
    url="https://github.com/robocorp/robotframework-lsp",
    author="Fabio Zadrozny",
    copyright="Robocorp Technologies, Inc.",
    packages=find_packages(exclude=["robotframework_ls_tests",]),
    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'configparser; python_version<"3.0"',
        'backports.functools_lru_cache; python_version<"3.2"',
        "python-jsonrpc-server>=0.3.2",
        'ujson<=1.35; platform_system!="Windows"',
    ],
    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[test]
    extras_require={"test": ["pytest", "pytest-regressions", "pytest-xdist"],},
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        "console_scripts": ["robotframework_ls = robotframework_ls.__main__:main",],
    },
)
