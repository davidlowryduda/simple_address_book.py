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


def _addressitem_from_line(line):
    """
    Convert a raw text line to an AddressItem.

    The structure of a line is defined in the definition for AddressItem.
    """
    sline = line.split("\t")
    if len(sline) < 2:
        raise IOError("Error parsing address from line. Malformed data.")
    address = sline[0]
    name = sline[1]

    if len(sline) > 2:
        otherinfo = sline[2]
    else:
        otherinfo = ""
    if len(sline) > 3:
        extrainfo = sline[3]
    else:
        extrainfo = ""
    if len(sline) > 4:
        raw_misc = sline[4:]
        misc = _raw_misc_to_dict(raw_misc)
    else:
        misc = {}

    return AddressItem(
        _email_address=address,
        _name=name,
        _otherinfo=otherinfo,
        _extrainfo=extrainfo,
        **misc
    )


def _raw_misc_to_dict(raw):
    """
    Converts text-form of misc to a dictionary.

    misc will be stored in the form ["(key1, val1)", "(key2, val2)",...]
    """
    ret = {}
    for elem in raw:
        key, _, val = elem.partition(',')
        key = key[1:].strip()
        val = val[:-1].strip()
        ret[key] = val
    return ret


class AddressList:
    """
    Representation of all addresses.

    AddressList stores a list of tuples of AddressItems. AddressList is read
    from a file if it exists, and is otherwise empty.
    """

    def __init__(self, filedir='.', filename='.address_list'):
        """
        Read addresses from address_list in `filename` if they exist.
        """
        self.addresses = []
        self.filedir = os.path.expanduser(filedir)
        self.filename = filename

        path = os.path.join(os.path.realpath(self.filedir), self.filename)
        if os.path.isdir(path):
            raise IOError("Invalid address_list file. File is a directory.")
        if os.path.exists(path):
            with open(path, 'r') as address_file:
                lines = [line.strip() for line in address_file if line]
                self.addresses = list(map(_addressitem_from_line, lines))

    def __getitem__(self, name):
        pass

    def add_address(self, **kwargs):
        """
        Add address with given data to addresses.

        AddressItem is responsible for validation of input.
        """
        addressitem = AddressItem(**kwargs)
        self.addresses.append(addressitem)

    def remove_address(self):
        pass

    def edit_address(self):
        pass

    def write(self):
        """
        Saves addressfile.
        """
        path = os.path.join(os.path.realpath(self.filedir), self.filename)
        if os.path.isdir(path):
            raise IOError("Invalid address file. File is a directory.")
        if self.addresses:
            with open(path, 'w') as addressfile:
                for addressitem in self.addresses:
                    addressfile.write(str(addressitem))


def _build_parser():
    pass


def main():
    pass

def stest():
    name = "D LD"
    email = "yo@shonuff.com"
    otherinfo = "awesome guy"
    alist = AddressList()
    alist.add_address(_name=name, _email_address=email, _otherinfo=otherinfo)
    alist.write()

if __name__ == "__main__":
    stest()
    #main()
