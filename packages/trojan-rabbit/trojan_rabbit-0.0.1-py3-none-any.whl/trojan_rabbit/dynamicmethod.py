from types import MethodType


class dynamicmethod:
    def __init__(self, func):
        self.func = func

    def __set_name__(self, owner, name):
        self._method_name = name
        self.func.__qualname__ = "%s.%s" % (owner.__name__, name)
        self.cls_method = MethodType(self.func, owner)

    def __get__(self, instance, owner):
        if instance:
            method = MethodType(self.func, instance)
            setattr(instance, self._method_name, method)
            return method
        elif owner:
            return self.cls_method
