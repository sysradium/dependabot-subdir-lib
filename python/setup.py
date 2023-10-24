import setuptools

with open('requirements.txt') as f:
    required_packages = f.read().splitlines()


setuptools.setup(
    name="dependabot-subdir-lib",
    version="1.2.0",
    author="sysradium",
    description="Testing subdir functionality for dependabot",
    long_description_content_type="text/markdown",
    url="https://github.com/sysradium/dependabot-subdir-lib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
    install_requires=required_packages
)
