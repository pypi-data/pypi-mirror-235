# Harmony Fake Module

This repository contains a fake ToonBoom package featuring a Harmony module that includes all the classes used within Harmony's Python interface. Its primary purpose is to provide autocompletion, access to docstrings, and accurate type hints in your preferred IDE.

All classes have been written based on Harmony's Python documentation, which can be found at: [Harmony Python Documentation](https://docs.toonboom.com/help/harmony-22/scripting/pythonmodule/index.html).

Please note that this fake module may contain inconsistencies, missing return types, and typos. Unfortunately, most of these issues stem from faithfully transcribing Harmony's flawed documentation.

## Installation

```shell
pip install harmony-fake-module
```

## Enabling Autocompletion in VSCode

Ctrl + Shift + P -> Preferences: Open Workspace Settings (JSON)

In the settings.json file, add the path to the fake module under python.analysis/autoComplete extra paths and save the file.

```json
{
    "python.analysis.extraPaths": [
        "path/to/harmony-fake-module"
    ],
    "python.autoComplete.extraPaths" : [
        "path/to/harmony-fake-module"
    ]
}
```