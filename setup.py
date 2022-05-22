from setuptools import setup

setup(
    name='skunkworks-repo',
    version='1.0.3',    
    description='The Skunk Works Code Repository',
    url='https://github.com/skunk-ink/skunkworks',
    download_url='https://github.com/skunk-ink/skunkworks/archive/refs/tags/v1.0.3.tar.gz',
    keywords=['Handshake', 'API', 'HNS'],
    author='skunk-ink',
    license='MIT',
    packages=['handshake'],
    install_requires=['requests',
                      'json'                    
                      ],

    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
