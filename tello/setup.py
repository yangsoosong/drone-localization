import setuptools
import sys

needs_pytest = {"pytest", "test", "ptr"}.intersection(sys.argv)
pytest_runner = ["pytest-runner"] if needs_pytest else []

with open("requirements.txt", "r") as requirements_file:
    requirements = requirements_file.read()

setuptools.setup(
    name="tello",
    description="Class project",
    author="John Ward",
    author_email="john@itsjohnward.com",
    url="https://github.com/yangsoosong/drone-localization",
    long_description_content_type="text/markdown",
    package_dir = {'tello': 'src'},
    packages=['tello'],
    python_requires=">=3.9",
    install_requires=requirements,
    extras_require={},
    setup_requires=pytest_runner,
    test_suite="pytest",
    tests_require=[],
    entry_points={"console_scripts": ["tello=src.__main__:main"]},
)