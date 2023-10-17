# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['batch_operation_of_files']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'batch-operation-of-files',
    'version': '0.0.0',
    'description': ' 文件的批量移动复制删除，可指定文件夹可操作层数与最大输出位置层数',
    'long_description': '# batch_operation_of_files\n 文件的批量移动复制删除，可指定文件夹可操作层数与最大输出位置层数\n',
    'author': 'ziru-w',
    'author_email': '77319678+ziru-w@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
