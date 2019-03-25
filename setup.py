from setuptools import setup, find_packages

setup(
    name='myapp',
    version='0.0.4',
    packages=find_packages(exclude=["tests.*", "tests"]),
    author="",
    author_email="",
    description="",
    license="",
    keywords="",
    url="",
    entry_points={
        'console_scripts': [
            'run.py=myapp.run:main']
    },
    install_requires=["requests",
                      "Flask",
                      "connexion[swagger-ui]",
                      "gevent"],
    zip_safe=False,
    package_data={'myapp': ['openapi.yaml']}
)
