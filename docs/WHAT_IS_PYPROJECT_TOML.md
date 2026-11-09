# What is pyproject.toml?

A short guide to the one configuration file every modern Python project has, using this repository's own file as the example.

## Where the name comes from

**TOML** stands for **Tom's Obvious, Minimal Language**. Tom Preston-Werner, a co-founder of GitHub, created it in 2013 because he wanted a configuration format that people could read and edit more easily than JSON or YAML.

Most people say it like "Tom" with an "L" on the end: **TAH-mul**.

## What the file is for

`pyproject.toml` is the standard place where a Python project describes itself. Tools such as `pip` and `pytest` read it, so you do not have to explain the project to each tool by hand.

- **PEP 518** (2016) introduced the file and its `[build-system]` section.
- **PEP 621** (2020) added the `[project]` section for the name, version and dependencies.

It replaces several older files: `setup.py`, `setup.cfg`, `requirements.txt` and `pytest.ini`.

## Our file, section by section

```toml
[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"

[project]
name = "sortsearch"
version = "0.1.0"
description = "Counting-based comparison of sorting and searching algorithms."
requires-python = ">=3.9"
dependencies = []

[project.optional-dependencies]
plots = ["matplotlib"]
test = ["matplotlib", "pytest"]

[tool.setuptools.packages.find]
where = ["src"]

[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["src"]
```

| Section | What it tells the tools |
|---|---|
| `[build-system]` | How to package the project: use setuptools, version 61 or newer. |
| `[project]` | The project's name (`sortsearch`), version, one-line description, and that it needs Python 3.9 or newer. `dependencies = []` means the core code uses only the standard library. |
| `[project.optional-dependencies]` | Add-ons you choose to install. `pip install -e ".[test]"` means "install this project plus its `test` extras", which are matplotlib and pytest. |
| `[tool.setuptools.packages.find]` | The code lives in `src/`. This is why `import sortsearch` works after you install. |
| `[tool.pytest.ini_options]` | Settings for pytest: find tests in `tests/`, and treat `src/` as importable. |

## Reading the install command

```
pip install -e ".[test]"
```

- `.` means "the project in this folder". pip looks for `pyproject.toml` right here.
- `[test]` means "also install the `test` extras".
- `-e` means "editable": pip links to your source files instead of copying them, so your edits take effect without reinstalling.

## Does it have to be at the root?

Yes. It sits at the top of the project, next to `src/` and `tests/`.

- `pip install -e .` looks for it in the folder you name, and `.` is the current folder.
- pytest searches upward from where you run it and treats the folder holding this file as the project root.

Move it into a subfolder and `pip install -e .` from the repository root fails.

## Try it: read the file the way the tools do

Python 3.11 and newer can read TOML with the standard library:

```python
import tomllib

with open("pyproject.toml", "rb") as f:
    config = tomllib.load(f)

print(config["project"]["name"])             # sortsearch
print(config["project"]["requires-python"])  # >=3.9
```

`tomllib` needs Python 3.11 or newer, even though this project supports 3.9. That is fine for a demonstration; the project code itself never reads the file.

Note that the file is opened in binary mode (`"rb"`). `tomllib` requires it, because TOML files are always UTF-8.

## Questions to check your understanding

1. What would `pip install -e ".[plots]"` install?
2. Why does `dependencies = []` matter for a project that promises "standard library for the classes"?
3. If you deleted the `pythonpath = ["src"]` line, what would you expect to break, and how would you check?
