from setuptools import find_packages, setup

setup(
    name="{{cookiecutter.project_slug}}",
    version="0.1.0",
    description="",
    url="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}",
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.email}}",
    license="MIT",
    install_requires=[
    ],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            #"command_name = pythonpackage.package:methodname",
        ]
    },
    zip_safe=False,
)
