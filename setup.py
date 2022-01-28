from setuptools import setup, find_packages

setup(
    name="locust_spanner",
    author="tomoemon",
    version="0.1",
    description="locust user for cloud spanner",
    url="https://github.com/tomoemon/locust_spanner",
    packages=find_packages(),
    install_requires=["locust", "google-cloud-spanner"],
)
