import logging
from enum import Enum


class BaseEnum(Enum):

    @classmethod
    def to_list(cls):
        return list(map(lambda x: x.value, cls))

    @classmethod
    def to_tuple(cls):
        return tuple(map(lambda x: x.value, cls))


def log_scope(log):
    def outer_d_f(f):
        def d_f(*args, **kargs):
            kn = f.__name__
            log.info("*** %s() is entering ..." % (kn))
            if args:
                log.debug("args: {}".format(args))
            if kargs:
                log.debug("kargs: {}".format(kargs))
            r = f(*args, **kargs)
            if r:
                if log.isEnabledFor(logging.DEBUG):
                    log.debug("<== {}(): {} ...".format(kn, r))
                else:
                    if type(r) not in (tuple, dict, list):
                        log.info("<== {}(): {} ...".format(kn, r))

            log.info("*** %s() is leaving ..." % (kn))
            return r
        d_f.__doc__ = f.__doc__
        return d_f
    return outer_d_f
