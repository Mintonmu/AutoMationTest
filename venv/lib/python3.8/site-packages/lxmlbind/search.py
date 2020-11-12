"""
Property search support.
"""
from logging import getLogger as get_logger

from lxml import etree
from six.moves import filter as ifilter


def search(instance, property_, create):
    """
    Search `lxml.etree` rooted at `instance._element` for the child
    element matching `property_.tags`.
    """
    parent = _search_parent(instance, property_, create)
    if parent is None:
        return None
    return _search_child(parent, property_.tags[-1], instance, property_, create, terminal=True)


def _search_parent(instance, property_, create):
    """
    Search for the parent element of `property_`.
    """
    element = instance._element
    for tag in property_.tags[:-1]:
        element = _search_child(element, tag, instance, property_, create)
        if element is None:
            return None
    else:
        return element


def _filter_func(property_, tag, terminal):
    """
    Determine the filtering function for selecting child elements.

    The logic for the terminal element is allowed to be customized.
    """
    if terminal and property_.filter_func is not None:
        return property_.filter_func
    else:
        return lambda element: element.tag == tag


def _attributes_func(property_, tag, terminal):
    """
    Determine the attributes generating function for creating child elements.

    The logic for the terminal element is allowed to be customized.
    """
    if not terminal:
        return lambda instance: {}
    elif property_.attributes_func is None:
        return lambda instance: property_.attributes
    else:
        return property_.attributes_func


def _search_child(element, tag, instance, property_, create, terminal=False):
    """
    Search for a child element matching filter_func.
    """
    try:
        # using next/ifilter allows comparable behavior to element.find(tag),
        # but with greater flexibility
        return next(ifilter(_filter_func(property_, tag, terminal), element))
    except StopIteration:
        if not create:
            return None
        attributes = _attributes_func(property_, tag, terminal)(instance)
        return _create_child(tag, element, attributes)


def _create_child(tag, parent, attributes):
    """
    Create child element.
    """
    get_logger("lxmlbind.base").debug("Creating element '{}' for '{}'".format(tag, parent.tag))
    return etree.SubElement(parent, tag, attrib=attributes)
