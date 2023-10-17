'''
设置函数
'''

import setuptools

with open(r"README.md","r") as f:
    long_description = f.read()

setuptools.setup(
    # 包的名字
    name = 'meiqian',
    # 版本号
    version= '0.0.1',
    # 作者
    author='meiqian',
    #包的描述
    description='各种奇奇怪怪的函数',
    # 包的详细介绍
    long_description = long_description,
)
