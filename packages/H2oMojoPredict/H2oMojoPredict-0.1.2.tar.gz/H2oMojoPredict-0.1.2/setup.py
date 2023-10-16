from setuptools import setup, find_packages

setup(
    name="H2oMojoPredict",
    version="0.1.2",
    packages=['H2oMojoPredict'],
    package_data={
        'H2oMojoPredict': ['*.jar'],
    },
    install_requires=[
            'pandas==1.1.5',
        ],
    author="yklian",
    author_email="923412504@qq.com",
    description="In H2oMojoPreidct, you can perform predictions on MOJO files without the need for H2O initialization or dependency on an H2O cluster. You are free to use Python to make predictions using MOJO files.",
    long_description = open("H2oMojoPredict/README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/lianyukun",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
    ],
)