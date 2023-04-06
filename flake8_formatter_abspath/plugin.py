# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import os

from flake8.formatting import default


class AbsolutePathFormatter(default.Default):
    """
    Reports the absolute path of any files with warnings.
    """

    def format(self, error):
        return default.Default.error_format % {
            "code": error.code,
            "text": error.text,
            "path": os.path.abspath(error.filename),
            "row": error.line_number,
            "col": error.column_number,
            **(default.COLORS if self.color else default.COLORS_OFF),
        }
