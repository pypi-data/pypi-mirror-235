import setuptools as st

st.setup(name='magicbits',
        version='2.0.2', 
        description='A simple package for demostration of concept of OS in python',
        author='Stella Ruth',
        author_email='stella.ruth7672@proton.me',
        packages=st.find_packages(),
        classifiers=[
        "License :: OSI Approved :: MIT License",
        "Environment :: Web Environment",
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6"],
        python_require = '>=3.9',
        install_requires = ['tabulate >= 0.9.0', 'matplotlib >= 3.8.0', 'numpy >= 1.26.1'], 
        keywords='os cpu scheduling',
        data_files=None)
