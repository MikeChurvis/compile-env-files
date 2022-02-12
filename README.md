# Environment Variable File Compiler

A script that builds and distributes environment variable files (.env) from a single-source-of-truth config file.

## Installation

`pip install git+https://github.com/MikeChurvis/compile-env-files.git`

**Note**

To avoid compromising potentially sensitive information, I strongly recommend that you add the following to your global `.gitignore`:
```.gitignore
.env.config.json
*.env
```

## Commands

**Compile Environment Variable Files** 
- Syntax: `compile-env [-f <filepath>]`
- Description: Builds and distributes environment variable files from the specified config file (default: `./.env.config.json`).
- Arguments:
  - `-f <filepath>`: The filepath to the config file you want to use. Can be relative or absolute.

**Generate Config File Template**
- Syntax: `make-config-template` 
- Description: Generates a config file template (`.env.config.json`) in the current directory. 

## Config Syntax

Here is the syntax at-a-glance:
```json
{
  "consumers": {
    "<consumer-alias>": "<env-file-output-path>",
    "<consumer-alias>": [ "<env-file-output-path>", "..." ],
    "..."
  },
  "variables": {
    "<variable-alias>": {
      "value": "<variable-value>",
      "consumers": {
        "<consumer-alias>": "<environment-variable-key>",
        "<consumer-alias>": [ "<environment-variable-key>", "..." ],
        "..."
      }
    },
    "..."
  }
```

You can see a hands-on example of this config and its potential use in the [example folder](./example) of this repo.

<TODO: flesh out documentation.>

## Requirements

Python >= 3.3

Dependencies: 
- setuptools >= 42

