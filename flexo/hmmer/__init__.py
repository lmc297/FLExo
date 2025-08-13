import functools

from gecco.hmmer import embedded_hmms as _embedded_hmms


@functools.wraps(_embedded_hmms)
def embedded_hmms(module: str = __name__):
    return _embedded_hmms(module)