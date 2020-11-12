"""
Declarative object collection classes.
"""
from functools import partial

from six.moves import filter as ifilter
from six.moves import map as imap
from six.moves import zip as izip

from lxmlbind.api import Base


class List(Base):
    """
    Extension that supports treating elements as list of other types.

    Attempts to maintainer _parent references.
    """
    @classmethod
    def _of(cls):
        """
        Defines what this class is a list of.

        :returns: a function that operates on `lxml.etree` elements, returning instances of `Base`.
        """
        return Base

    def append(self, value):
        # This maintains ordering
        self._element.append(value._element)
        value._parent = self

    def __getitem__(self, key):
        func = partial(self.__class__._of(), parent=self)
        return func(self._element.__getitem__(key))

    def __setitem__(self, key, value):
        self._element.__setitem__(key, value._element)
        value._parent = self

    def __delitem__(self, key):
        # Without keeping a parallel list of Base instances, it's not
        # possible to detach the _parent pointer of values added via
        # append() or __setitem__. So far, not keeping a parallel list
        # is worth it.
        self._element.__delitem__(key)

    def __iter__(self):
        func = partial(self.__class__._of(), parent=self)
        return imap(func, self._element.__iter__())

    def __len__(self):
        return len(self._element)


class Dict(Base):
    """
    Extension that supports treating elements as dict of types.

    Attempts to maintainer _parent references.
    """
    @classmethod
    def _of(cls):
        """
        Defines what this class is a list of.

        :returns: a function that operates on `lxml.etree` elements, returning instances of `Base`.
        """
        return Base

    @classmethod
    def _key(cls, item):
        """
        Defines how to equate items with keys.
        """
        return item._element.tag

    def add(self, item):
        """
        Add an instance of `Base` to this dictionary, using the key function to assign a key.
        """
        key = self.__class__._key(item)
        self[key] = item

    def get(self, key):
        try:
            return self[key]
        except KeyError:
            return None

    def _find_item(self, key):
        if key is None:
            return None
        func = partial(self.__class__._of(), parent=self)
        for child in self._element:
            item = func(child)
            if self.__class__._key(item) == key:
                return item
        else:
            return None

    def __contains__(self, key):
        return self._find_item(key) is not None

    def __getitem__(self, key):
        item = self._find_item(key)
        if item is None:
            raise KeyError(key)
        return item

    def __setitem__(self, key, value):
        item = self._find_item(key)
        if item is None:
            self._element.append(value._element)
            value._parent = self
        else:
            element_parent = item._element.getparent()
            element_parent.remove(item._element)
            element_parent.append(value._element)
            value._parent = self

    def __delitem__(self, key):
        item = self._find_item(key)
        if item is None:
            raise KeyError(key)
        item._element.getparent().remove(item._element)
        # see comments in List.__delitem__ re: removing _parent linkage

    def iterkeys(self):
        func = partial(self.__class__._of(), parent=self)
        return ifilter(None,
                       imap(self.__class__._key,
                            imap(func, self._element.__iter__())))

    def keys(self):
        return list(self.iterkeys())

    def itervalues(self):
        func = partial(self.__class__._of(), parent=self)
        return (item for item in imap(func, self._element.__iter__())
                if self.__class__._key(item) is not None)

    def values(self):
        return list(self.itervalues())

    def iteritems(self):
        return izip(self.iterkeys(), self.itervalues())

    def items(self):
        return list(self.iteritems())

    def __iter__(self):
        return self.iterkeys()

    def __len__(self):
        return len(self._element)
