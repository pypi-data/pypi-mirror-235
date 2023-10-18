from setuptools import setup, find_packages

setup(
    name="manipulating_data",
    version="0.1.0",
    author="Krzysztof Chrzan",
    author_email="krzysztof.a.chrzan@email.com",
    description="A package for manipulating Python data structures.",
    license='MIT',
    packages=find_packages( include=["manipulating_data", "manipulating_data.*"] ),
    install_requires=["pandas", "numpy","typing"]
)
