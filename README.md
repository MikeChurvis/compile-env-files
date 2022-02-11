# Environment Variable File Compiler

A script that builds and distributes environment variable files (.env) from a single-source-of-truth config file.

## Commands

### Compile Environment Variable Files

**Command:** 
`compile-env [-f <filepath>]`

**Description:**
Builds and distributes environment variable files from the specified config file (default: `./.env.config.json`)

**Arguments:**
- `-f <filepath>`: The filepath to the config file you want to use. Can be relative or absolute.

### Generate .env.config.json Template

**Command:**
`make-config-template` 

**Description:**
Generates a config file template in the current directory. 

## Requirements

Python version: 3.5+

Dependencies: 
- setuptools