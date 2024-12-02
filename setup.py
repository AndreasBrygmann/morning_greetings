from setuptools import setup, find_packages

setup(
    name='Morning Greetings',  # The package name
    version="0.1",
    packages=find_packages(),  # Automatically find all packages in your project
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in (if any)
    description="Lets you automatically send morning greetings to a contact list",
    author="Jon Andreas Brygmann",
    author_email="jobry7545@oslomet.no",
    install_requires=[
        # List your project's dependencies here, if any, e.g.,
        # 'requests',
    ],
    entry_points={
        'console_scripts': [
            'morning_greetings=morning_greetings.main:main', # Points directly to the main function in main.py
        ],
    },
)