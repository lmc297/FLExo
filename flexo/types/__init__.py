from typing import Union

import gecco.types

try:
    from importlib.resources import files
    from importlib.resources.abc import Traversable
except ImportError:
    from importlib_resources import files  # type: ignore
    from importlib_resources.abc import Traversable


class TypeClassifier(gecco.types.TypeClassifier):

    @classmethod
    def trained(cls, model_path: Union[Traversable, str, None] = None) -> "TypeClassifier":
        if model_path is None:
            model_path = files(__name__)
        return super().trained(model_path)
