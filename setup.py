from setuptools import find_packages
from setuptools import setup

setup(
    name='pre-commit-hooks-lxml',
    description='Some CSS/HTML validating pre-commit hooks using lxml',
    url='https://github.com/Lucas-C/pre-commit-hooks-lxml',
    version='1.1.0',

    author='Lucas Cimon',
    author_email='lucas.cimon@gmail.com',

    platforms='linux',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=find_packages('.'),
    install_requires=[
        'lxml',
        'tinycss2',
    ],
    entry_points={
        'console_scripts': [
            'detect_missing_css_classes = pre_commit_hooks.detect_missing_css_classes:main',
            'forbid_html_img_without_alt_text = pre_commit_hooks.forbid_html_img_without_alt_text:main',
            'forbid_non_std_html_attributes = pre_commit_hooks.forbid_non_std_html_attributes:main',
            'html_tags_blacklist = pre_commit_hooks.html_tags_blacklist:main',
            'html_attributes_blacklist = pre_commit_hooks.html_attributes_blacklist:main',
            'enforce_new_tab_policy = pre_commit_hooks.enforce_new_tab_policy:main',
        ],
    },
)
