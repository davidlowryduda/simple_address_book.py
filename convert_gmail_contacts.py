#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a little script I wrote to convert my gmail contacts into this
address-book format. I don't know whether gmail's format is constant over time,
and this is not something that needs to be done repeatedly. Thus I write it as a
sample one-off script.

In order for this to work, I exported gmail's contacts as a csv. I save the
resulting addressbook in the local directory and append it to my systemwide
addressbook afterwards (it would be easy to generate it directly, but this
is sufficient for a one-off script).

I suggest running the addressbook through uniq once afterwards.


Licence Info
------------

MIT License.
Copyright (c) 2019 David Lowry-Duda <david@lowryduda.com>.
"""
import csv
import simple_addr as sadr


def extract_info_from_contacts(line):
    name, email1, email2 = line[0], line[-9], line[-7]
    if not name:
        name, _, _ = email1.partition("@")
        name = name.strip()
    return name, email1, email2


def main():
    with open("contacts.csv", "r") as f:
        lines = f.readlines()
    reader = csv.reader(lines)
    cols = next(reader)

    addresslist = sadr.AddressList()

    for line in reader:
        expression = '\t'.join(extract_info_from_contacts(line))
        addressitem = sadr._addressitem_from_line(expression)
        addresslist.add_addressitem(addressitem)

    addresslist.write()

if __name__ == "__main__":
    main()
