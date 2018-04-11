from setuptools import setup, find_packages

setup(
    name='myapp',
    version='0.0.1',
    packages=find_packages(exclude=["tests.*", "tests"]),
    author="",
    author_email="",
    description="",
    license="",
    keywords="",
    url="",
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'run.py=myapp.run:main']
    },
    install_requires=["requests", "Flask", "connexion"],
    include_package_data=True
)
