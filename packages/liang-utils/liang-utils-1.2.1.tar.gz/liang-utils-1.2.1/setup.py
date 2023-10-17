from setuptools import setup, find_packages


setup(
    name="liang-utils",
    version="1.2.1",
    packages=find_packages(),    # detect and include all packages automatically
    install_requires=[
        'ttp',
        # 'openpyxl',
        'tqdm',
    ],
    entry_points={
        "console_scripts": [
            "match_dict = liang_utils.match_dict:main",
            "split_log = liang_utils.process_log:main",
        ],
    },
    # scripts=['bin/upgrade_check'],      # CLI tool entry point
    author="Liang",
    description="A couple of liang_utils for network automation",
    python_requires='>=3.8',
)
