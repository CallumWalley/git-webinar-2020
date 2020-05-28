#!/usr/bin/env python

import datetime

__author__ = "Megan"
__copyright__ = "Copyright 2020, Callum Walley"
__credits__ = ["Callum Walley"]
__license__ = "GPL"
__version__ = "1.2.6"
__maintainer__ = "Callum Walley"
__email__ = "callum.walley@nesi.org.nz"

# Important functions for all of my important work.


def get_first_index_of_array(array):
    """
    this function is very usefull useful for returning the first index of array.
    """
    return array[0]


def print_but_louder(in_string):
    """
    For when you need to emphisise something.
   """
    out_string = in_string.upper() + "!!!!"
    return out_string


def is_it_wednesday():
    if datetime.datetime.today().weekday() == 2:
        return True
    return False

