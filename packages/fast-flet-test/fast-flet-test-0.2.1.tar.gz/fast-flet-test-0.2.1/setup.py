from setuptools import setup,find_packages

with open("./README.md", "r", encoding="utf-8") as e:
    long_description = e.read()

VERSION = "0.2.1"
DESCRIPCION = "🔥 Fast-Flet is a package built as a complement to Flet, designed for newbies which facilitates the handling of flet events, designed to work with numerous pages and be customizable."


setup(
    name="fast-flet-test", 
    version=VERSION,
    author='Jrxvx',
    description=DESCRIPCION,
    long_description='test',
    url='https://github.com/Jrxvx/Fast-Flet',
    long_description_content_type="text/markdown",
    download_url='https://github.com/Jrxvx/Fast-Flet',
    project_urls = {
        "Bug Tracker":"https://github.com/Jrxvx/Fast-Flet/issues"
    },
    packages=find_packages(),
    package_data={
        "commands": [
            "templates/*",
            "templates/*/*",
            "templates/*/*/*",
            "templates/*/*/*/*",
            "templates/*/*/*/*/*",
        ],
    },
    install_requires=[
        "typer[all]",
        "flet",
        "flet_fastapi",
        "uvicorn",
        ],
    classifiers={
        "License :: OSI Approved :: Apache Software License",
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
    },
    #python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "fast-flet=commands.cli:cli",
        ],
    },
    license= "Apache-2.0",
    keywords=[
        "python web template",
        "flet",
        "app python",
        "flet mvc",
        "fast flet mvc",
        "fast flet",
        "flet-fastapi",
        "flutter python",
        "flet personalized",
        "web application",
        "development"
        ],
    
)