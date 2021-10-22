import inspect

import justpy as jp

from webapp.about import About
from webapp.dictionary import Dictionary
from webapp.home import Home
from webapp import page

imports = list(globals().values())

for obj in imports:
    if inspect.isclass(obj):
        if issubclass(obj, page.Page) and obj is not page.Page:
            jp.Route(path=obj.path, func_to_run=obj.serve)

jp.justpy()
