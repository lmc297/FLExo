# PYTHON_ARGCOMPLETE_OK

import sys
import typing
from typing import List, Optional

from rich.console import Console
from gecco.cli import main as _main

from . import __version__, __package__ as _program
from .crf import ClusterCRF
from .types import TypeClassifier
from .hmmer import embedded_hmms


def main(
    argv: Optional[List[str]] = None, 
    console: Optional[Console] = None,
    *,
    program: str = _program,
    version: str = __version__,
) -> int:
    return _main(
        argv,
        console,
        program=program,
        version=version,
        crf_type=ClusterCRF,
        classifier_type=TypeClassifier,
        default_hmms=embedded_hmms,
        defaults={
            "--c1": 1.0,
            "--c2": 0.0,
            "--e-filter": None,
            "--p-filter": 1e-9,
            "--window-size": 20,
            "--feature-type": "protein",
            "--select": 0.75,
            "--threshold": 0.1,
            "--cds": 2,
        }
    )


if __name__ == "__main__":
    sys.exit(main())
