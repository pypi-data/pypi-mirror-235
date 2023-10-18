from typing import Callable
import functools
import inspect

from django.http import HttpResponse

from django_di import context


def di(func: Callable[..., HttpResponse]):

    @functools.wraps(func)
    def inject(*args, **kwargs):
        """Inject view dependencies by checking global context by the parameter's type annotation."""

        annotations = inspect.get_annotations(func)
        # See https://docs.python.org/3/howto/annotations.html
        # and https://docs.python.org/3/library/inspect.html#inspect.get_annotations

        for param_name, param_type in annotations.items():
            try:
                kwargs[param_name] = context.DI.get(param_type)
            except KeyError:
                pass

        return func(*args, **kwargs)
    
    return inject
