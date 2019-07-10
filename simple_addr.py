#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
simple_addr.py

simple_addr is a simplest possible address book, designed to work well with a
mutt query_command for good ol' TUI email. The goal is simplicity over
features.


License Info
------------

This is released under the MIT License.


Copyright (c) 2019 David Lowry-Duda <david@lowryduda.com>.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import os

VERSION = "0.0.1"

# Mutt is expecting responses in the form
# david@lowryduda.com <TAB> David Lowry-Duda <TAB> OtherInfo <TAB> [ignored]


class AddressItem:
    """
    Representation of a single address entry.


    Mutt expects responses in the form

        david@lowryduda.com <TAB> David Lowry-Duda <TAB> OtherInfo <TAB> [other]

    and mutt ignores [other stuff] (including any further tabbed data). Each
    AddressItem must contain an `email_address` and `name`. Optionally it can
    contain `otherinfo`, and `extrainfo`. Any `otherinfo` will be visible in
    mutt, but `extrainfo` will not be visible in mutt.
    """

    def __init__(
            self,
            _email_address=None,
            _name=None,
            _otherinfo="",
            _extrainfo="",
            **kwargs
        ):
        """
        Set email_address, name, otherinfo, and extrainfo.  Any additional
        kwargs are also stored in (key, value) pairs.

        If `_email_address` or `_name` is not defined, raise an Exception.
        """
        self.email_address = _email_address
        self.name = _name
        self.otherinfo = _otherinfo
        self.extrainfo = _extrainfo
        self.misc = kwargs.items()

        self.validate()

    def __str__(self):
        """
        A tab-separated single-line representation for the file. A line is of
        the form

            address\tname\totherinfo[\textrainfo][\tmisc1][\tmisc2]
        """
        ret = "{address}\t{name}\t{otherinfo}".format(
            address   = self.email_address,
            name      = self.name,
            otherinfo = self.otherinfo
        )
        if self.extrainfo:
            ret = ret + "\t" + self.extrainfo
        if self.misc:
            ret = ret + "\t" + self.format_misc()
        return ret

    def format_misc(self):
        """
        Gives a string representation for the misc part fo the address. This is
        of the form

            \t(key1, val1)\t(key2, val2)...
        """
        if not self.misc:
            return ""
        ret = ""
        for key, val in self.misc:
            ret = ret + "\t({key}, {val})".format(key=key, val=val)
        return ret

    def validate(self):
        """
        If email_address of name is not defined, raise an Exception.
        If more than 8 misc attributes are given, raise an Exception.
        """
        if (self.email_address is None) or (self.name is None):
            raise IOError(
                "Invalid address detected. Address and name must be given."
            )
        if len(self.misc) > 8:
            raise IOError(
                "Invalid address detected. Too many misc descriptors."
            )


class AddressList:
    """
    Representation of all addresses.

    AddressList stores a list of tuples of AddressItems. AddressList is read
    from a file if it exists, and is otherwise empty.
    """

    def __init__(self, filedir='.', name='.address_list'):
        """
        Read addresses from address_list if they exist.
        """
        pass

    def __getitem__(self, name):
        pass

    def add_address(self):
        pass

    def remove_address(self):
        pass

    def edit_address(self):
        pass

    def write(self):
        pass


def _build_parser():
    pass


def main():
    pass


if __name__ == "__main__":
    main()
