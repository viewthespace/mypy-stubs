# mypy-stubs

[Mypy stubs](https://mypy.readthedocs.io/en/stable/stubs.html) for a variety of libraries.

## Special considerations

### Shapely

To avoid errors, the Shapely types use [NewType](https://mypy.readthedocs.io/en/stable/more_types.html#newtypes) for `X`, `Y`, and `Z` parameters. However, these don’t actually exist in Shapely. As such, one will need to add this shim:

```python
from typing import NewType, Type, cast

import shapely.geometry as geometry

X: 'Type[geometry.X]' = cast('Type[geometry.X]', NewType('X', float))
Y: 'Type[geometry.Y]' = cast('Type[geometry.Y]', NewType('Y', float))
Z: 'Type[geometry.Z]' = cast('Type[geometry.Z]', NewType('Z', float))
Longitude = X
Latitude = Y

geometry.X = X  # type: ignore
geometry.Y = Y  # type: ignore
geometry.Z = Z  # type: ignore
```

It’s recommended to instantiate these instances from the shim, not Shapely, as they will not be present if the shim hasn’t been loaded.
