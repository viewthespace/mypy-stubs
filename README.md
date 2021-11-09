# mypy-stubs

[Mypy stubs](https://mypy.readthedocs.io/en/stable/stubs.html) for a variety of libraries. Provided as a set of [PEP 561 compatible packages](https://mypy.readthedocs.io/en/stable/installed_packages.html#creating-pep-561-compatible-packages).

## Usage

Simply add this package as a dependency.

## Development guidelines

- Be sure to bump the version, otherwise dependents may not actually re-install
- Be sure to add new stub packages (dirs in `./src`) to the `packages` list in `pyproject.toml`

### Using in a project for development

Poetry has some bad ergonomics (read: bugs) around this. Workarounds are noted.

1. In the other project, update the dependency to e.g. `{path="../mypy-stubs", develop = true}`
2. Due to bugs, it may be necessary to uninstall the existing package with e.g. `poetry run pip uninstall typeshed_vts`
3. Due to bugs, it may be necessary to remove all the `*-stubs` entries in `packages` in this project’s `pyproject.toml`
4. In the other project, update packages e.g. `poetry update typeshed_vts`

## Special considerations

Some types have additional constructs added to them that are instead part of the `typing_vts` package.

### Airflow

- `typing_vts.Context` is an Airflow Context

### Shapely

To avoid errors, the Shapely types use [NewType](https://mypy.readthedocs.io/en/stable/more_types.html#newtypes) for `X`, `Y`, and `Z` parameters. However, these don’t actually exist in Shapely. Instead, import them like:

```python
from typeshed_vts.shapely import X, Y, Z
```
