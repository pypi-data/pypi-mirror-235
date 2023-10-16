from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="cyrius",
    version="1.1.1",
    description="WGS-based CYP2D6 caller",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[],
    keywords="CYP2D6",
    url="https://github.com/illumina/Cyrius",
    author="Xiao Chen",
    author_email="xchen2@illumina.com",
    license="PolyFormStrict",
    packages=["cyrius", "cyrius/caller", "cyrius/depth_calling"],
    package_data={"cyrius": ["data/*"]},
    install_requires=["pysam", "numpy", "scipy", "statsmodels"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    entry_points={"console_scripts": ["cyrius=cyrius.star_caller:main"]},
    include_package_data=True,
    zip_safe=False,
)
