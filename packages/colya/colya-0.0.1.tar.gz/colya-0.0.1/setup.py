from setuptools import setup, find_packages  
  
setup(  
    name = 'colya',  
    version = '0.0.1',
    keywords = ('colya'),  
    description = 'A Satori QQBot Scripyt',  
    license = 'MIT License',  
    install_requires = [],  
    packages = ['Colya'],  # 要打包的项目文件夹
    include_package_data=True,   # 自动打包文件夹内所有数据
    author = 'Ysasm',  
    author_email = '1613921123@qq.com',
    url = 'https://gitee.com/YSASM/ColyaBot.git',
    # packages = find_packages(include=("*"),),  
)  
