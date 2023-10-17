from setuptools import setup

setup(
    name="ethercheck",
    version="1.1.1",
    description="A minimal, yet complete, python API for etherscan.io.",
    url="https://github.com/edwardcheck117/ethercheck",
    author="Edward Check",
    author_email="edwardcheck117@gmail.com",
    license="MIT",
    packages=[
        "ethercheck",
        "ethercheck.configs",
        "ethercheck.enums",
        "ethercheck.modules",
        "ethercheck.utils",
    ],
    install_requires=["requests"],
    include_package_data=True,
    zip_safe=False,
)
