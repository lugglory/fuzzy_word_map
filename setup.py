from setuptools import setup, find_packages

setup(
    name='fuzzy_word_map',
    version='0.0',
    description='여러 방법을 혼합하여 효율적으로 유사 단어를 찾는 기능 제공',
    author='Hyonyoung Park',
    author_email='lugglory@gmail.com',
    url='https://github.com/lugglory/fuzzy_word_finder',
    packages=find_packages(),
    install_requires=['python-Levenshtein', 'jamo'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    license='MIT',
)
