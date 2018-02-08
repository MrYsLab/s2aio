from setuptools import setup

setup(
    name='s2aio',
    version='1.12',
    packages=['s2aio'],
    install_requires=['pymata-aio>=2.7',
                      'aiohttp==0.22.4'],
    package_data={'s2aio': [('configuration/*.cfg'),
                            ('miscellaneous/*.txt, *.csv, *.ods'),
                            ('ScratchFiles/ExtensionDescrptors/*.s2e'),
                            ('ScratchFiles/ScratchProjects/*.sb2'),
                            ('Snap!Files/*.xml')]},
    entry_points={
        'console_scripts': [
            's2aio = s2aio.__main__:main'
        ]
    },
    url='https://github.com/MrYsLab/s2aio/wiki',
    download_url='https://github.com/MrYsLab/s2aio',
    license='GNU General Public License v3 (GPLv3)',
    author='Alan Yorinks',
    author_email='MisterYsLab@gmail.com',
    description='A Scratch 2.0 (Offline) Hardware Extension for Arduino',
    keywords=['Firmata', 'Arduino', 'Scratch'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Other Environment',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Education',
    ],
)
