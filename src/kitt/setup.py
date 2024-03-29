from setuptools import find_packages, setup

package_name = 'kitt'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/images', ['resource/images/model.png']),#拷贝汽车图片到共享目录
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='fotianmoyin',
    maintainer_email='190045431@qq.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'car = kitt.car:main'
        ],
    },
)
