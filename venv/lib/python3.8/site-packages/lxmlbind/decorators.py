"""
Declarative object decorators.
"""
from lxmlbind.api import Base


def tag(name):
    """
    Class decorator that replaces `Base.tag()` with a function that returns `name`.
    """
    def wrapper(cls):
        if not issubclass(cls, Base):
            raise Exception("lxmlbind.base.tag decorator should only be used with subclasses of lxmlbind.base.Base")

        @classmethod
        def _tag(cls):
            return name

        cls._tag = _tag
        return cls
    return wrapper


def attributes(**kwargs):
    """
    Class decorator that replaces `Base.attributes()` with a function that returns `kwargs`.
    """
    def wrapper(cls):
        if not issubclass(cls, Base):
            raise Exception("lxmlbind.base.attributes decorator should only be used with subclasses of lxmlbind.base.Base")  # noqa

        @classmethod
        def _attributes(cls):
            return kwargs

        cls._attributes = _attributes
        return cls
    return wrapper


def of(*classes):
    """
    Class decorator that replaces `List.of()` or `Dict.of` with a function that matches classes.
    """
    def wrapper(cls):
        if not issubclass(cls, Base):
            raise Exception("lxmlbind.base.of decorator should only be used with subclasses of lxmlbind.base.Base")

        tag_to_class = {
            class_._tag(): class_ for class_ in classes
        }

        @classmethod
        def _of(cls):
            def for_tag(element, parent=None):
                return tag_to_class[element.tag](element, parent)
            return for_tag

        cls._of = _of
        return cls
    return wrapper


def key(key_func):
    """
    Class decorator that replaces `Dict._key()` with a function that maps elements to keys.
    """
    def wrapper(cls):

        @classmethod
        def _key(cls, element):
            return key_func(element)

        cls._key = _key
        return cls
    return wrapper
