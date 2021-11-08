# mypy-stubs

[Mypy stubs](https://mypy.readthedocs.io/en/stable/stubs.html) for a variety of libraries. Provided as a set of [PEP 561 compatible packages](https://mypy.readthedocs.io/en/stable/installed_packages.html#creating-pep-561-compatible-packages).

## Usage

Simply add this package as a dependency.

## Development guidelines

- Be sure to bump the version, otherwise dependents may not actually re-install

## Special considerations

### Shapely

To avoid errors, the Shapely types use [NewType](https://mypy.readthedocs.io/en/stable/more_types.html#newtypes) for `X`, `Y`, and `Z` parameters. However, these don’t actually exist in Shapely. Instead, import them like:

```python
from typeshed_vts.shapely import X, Y, Z
```
