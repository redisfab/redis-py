from contextlib import contextmanager
import sys


try:
    import hiredis  # noqa
    HIREDIS_AVAILABLE = True
except ImportError:
    HIREDIS_AVAILABLE = False


def from_url(url, db=None, **kwargs):
    """
    Returns an active Redis client generated from the given database URL.

    Will attempt to extract the database id from the path url fragment, if
    none is provided.
    """
    from redis.client import Redis
    return Redis.from_url(url, db, **kwargs)


@contextmanager
def pipeline(redis_obj):
    p = redis_obj.pipeline()
    yield p
    p.execute()


class dummy(object):
    """
    Instances of this class can be used as an attribute container.
    """
    pass


def merge_dicts(x, y):
    if y == {}:
        return x
    if x == {}:
        return y
    z = x.copy()
    z.update(y)
    return z
