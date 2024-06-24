from setuptools import setup, find_packages

setup(
    name='snap_to_anki',
    version='0.1.0',
    description='Convert screenshots of study materials into Anki flashcards.',
    author='Lya Santoso',
    url='https://github.com/fleea/snap-to-anki',
    packages=find_packages(),
    install_requires=[
        'pytesseract',
        'openai',
        'python-dotenv',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
    entry_points={
        'convert': [
            'snap_to_anki=snap-to-anki.main:main',
        ],
    },
)