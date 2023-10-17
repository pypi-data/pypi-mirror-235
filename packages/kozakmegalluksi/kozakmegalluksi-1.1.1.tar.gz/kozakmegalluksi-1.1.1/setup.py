from setuptools import setup, find_packages


setup(
    name="kozakmegalluksi",
    version='1.1.1',
    author="mr.dnd",
    author_email="<klestianb@gmail.com>",
    description='A package from mr.dnd',
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "PythonTurtle==0.3.2"
    ],
    keywords=[ 'nemzz', 'kozak', 'mega', 'lluksi'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)