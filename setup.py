import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='compile_env_files',
    version='0.1.0',
    author='Mike Churvis',
    author_email='mikechurvis@gmail.com',
    description='A script that builds and distributes environment variable files from a single-source-of-truth config file.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/MikeChurvis/compile-env-files',
    license='GPL-3',
    packages=['src'],
    entry_points={
        'console_scripts': [
            'compile-env=src.commands:compile_env_files',
            'make-config-template=src.commands:generate_blank_config',
        ],
    }
)