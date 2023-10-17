from setuptools import setup, find_packages

setup(
    name='MLSwanlab',
    version='0.1.0',
    url='https://swanlab.co',
    author='MLSwanlab',
    author_email='22009100671@stu.xidian.edu.cn',
    description='A python package which can help you visually track your training process of machine-learning',
    packages=find_packages(),
    include_package_data=True,  # include other files like static and templates
    zip_safe=False,
    install_requires=[
        'flask',
        'torch',
        'numpy',
        'time',
        'random',
        'threading',
        # 添加你的其他依赖项
    ],
)