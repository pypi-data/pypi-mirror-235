from distutils.core import setup

setup(
    name='mailing_logs',  # How you named your package folder (MyLib)
    packages=['mailing_logs'],  # Chose the same as "name"
    version='0.2',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='Easy logs mailing',  # Give a short description about your library
    author='Konstantin Ponomarev(cicwak)',  # Type in your name
    author_email='cicwak@gmail.com',  # Type in your E-Mail
    url='https://github.com/cicwak/mailing-logs',  # Provide either the link to your github or to your website
    download_url='https://github.com/cicwak/mailing-logs/archive/refs/tags/0.2.tar.gz',  # I explain this later on
    keywords=['MAILING', 'LOGS', 'BEST'],  # Keywords that define your package best
    install_requires=[  # I get to this in a second
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
