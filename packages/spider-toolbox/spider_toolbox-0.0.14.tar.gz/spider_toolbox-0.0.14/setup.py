from setuptools import setup

version = '0.0.14'
author = 'neco_arc'
email = '3306601284@qq.com'

with open('README.md', mode='r', encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='spider_toolbox',
    version=version,
    author=author,
    author_email=email,
    description='爬虫工具库',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sweetnotice/spider_toolbox',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    package_dir={'spider_toolbox': 'src'},
    packages=['spider_toolbox'],
    python_requires='>=3.6',
    install_requires=[
        'requests',
        'PyExecJS',
        'rich'
    ],
)
