# pylint: disable=expression-not-assigned,abstract-method,import-error
from __future__ import unicode_literals
from ._base import _Base, os


class Manual(_Base):
    def make_clone(self, options):
        try:
            os.mkdir(self.path)
        except OSError as oserror:
            if oserror.errno == os.errno.EEXIST:
                self.delete()
                return self.make_clone(options)
            raise  # nocv
        return None, None

    def make_update(self, options):
        return None, None
