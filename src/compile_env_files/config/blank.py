config = """{
  "consumers": {
    "<consumer-alias>": ["<relative-path-to-output-file>"]
  },
  "variables": {
    "<variable-alias>": {
      "value": "<variable-value>",
      "consumers": {
        "<consumer-alias>": ["<ENVIRONMENT_VARIABLE_KEY>"]
      }
    }
  }
}"""