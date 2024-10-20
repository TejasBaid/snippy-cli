from setuptools import setup
setup(
    name = 'py-snippy',
    version = '1.0.0',
    packages = ['snippy'],
    entry_points = {
        'console_scripts': [
            'snip = snippy.__main__:main'
        ]
    },
    description= "This is a snippet management package",
    author="Tejas Baid",
    install_requires = ['python-editor','pyperclip'])