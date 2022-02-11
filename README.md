# Environment Variable File Compiler

A script that builds and distributes environment variable files (.env) from a single-source-of-truth config file.

## Commands

### Compile Environment Variable Files

`compile-env [-f <filepath>]`

Builds and distributes environment variable files from the specified config file (default: `./.env.config.json`).

Arguments:
- `-f <filepath>`: The filepath to the config file you want to use. Can be relative or absolute.

### Generate Config File Template

`make-config-template` 

Generates a config file template (`.env.config.json`) in the current directory. 

## Requirements

Python version: 3.5+

Dependencies: 
- setuptools

## Note

To avoid compromising potentially sensitive information, I strongly recommend you add the following to your global `.gitignore`:
```.gitignore
.env.config.json
*.env
```
