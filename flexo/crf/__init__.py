from typing import Union

import gecco.crf

try:
    from importlib.resources import files
    from importlib.resources.abc import Traversable
except ImportError:
    from importlib_resources import files  # type: ignore
    from importlib_resources.abc import Traversable


class ClusterCRF(gecco.crf.ClusterCRF):

    @classmethod
    def trained(cls, model_path: Union[Traversable, str, None] = None) -> "ClusterCRF":
        if model_path is None:
            model_path = files(__name__)
        return super().trained(model_path)
