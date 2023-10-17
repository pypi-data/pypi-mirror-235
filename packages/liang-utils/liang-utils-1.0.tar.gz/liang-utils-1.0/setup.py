from setuptools import setup, find_packages


setup(
    name="liang-utils",
    version="1.0",
    packages=find_packages(),    # detect and include all packages automatically
    install_requires=[
        # 'ttp',
        # 'openpyxl',
        # 'tqdm',
    ],
    entry_points={
        "console_scripts": [
            "match_dict = utils.match_dict:main",      # CLI tool entry point
        ],
    },
    # scripts=['bin/upgrade_check'],      # CLI tool entry point
    author="Liang",
    description="A couple of utils for network automation",
    python_requires='>=3.8',
)
