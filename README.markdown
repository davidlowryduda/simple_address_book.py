# simple_addr

`simple_addr.py` is a simplest possible address book, designed to work
well with mutt. It's dead simple and has almost no features.

[![Build Status](https://travis-ci.com/davidlowryduda/simple_address_book.py.svg?branch=master)](https://travis-ci.com/davidlowryduda/simple_address_book.py)


## Like a simpler abook

The great ancestor of this tool is `abook`, a C-library for address book
management (including convenient mutt hooks). `abook` is much more complicated,
but it's also faster, more robust, and more featureful.

Perhaps the only other downside of abook is that it's barely maintained anymore.
On the other hand, only tools that get dull need to be resharpened.


## Why write another address book?

This began a simple one-day exercise to be done at a python meetup. I've been
using mutt for a little while now, but for some reason I had some problem
building `abook` for one of my machines. I thought "how hard can it be to just
write my own address book?" And the answer is "Not actually that hard at all."

I get some great satisfaction when writing my own versions of classic software.


## Installing simple_addr.py

`simple_addr.py` is tested on python 3.4+, but presumably works for any python3.
It uses only the python standard library. *Simplicity is queen*.

In its current state, there is no good way to install it aside from procuring
the script file and putting it in a safe place on your system.

On call, `simple_addr.py` will use an address-file. It's expected that this
address-file will be provided as command line arguments "-d DIR" and "-f FILE".
In practice, it's a good idea to set up an alias for calling `simple_addr.py`,
as in

```bash
alias sadr='python ~/path/to/simple_addr.py -d ~/addresses -f .address-book'
```

# Usage

`simple_addr.py` can be used from the command line or called from mutt.

Type

```bash
python simple_addr.py -h
```

for command-line reference.


## Command line

On its own, `simple_addr.py` prints a copy of the entire addressbook. This is
not so helpful.


### Simple Searching

```bash
python simple_addr.py David
```

will print out a copy of addresses in the addressbook containing "David". In the
future, more sophisticated search functionality might be given --- but for now,
that's it.


### Adding Addresses

```bash
python simple_addr.py "test@example.com" "Gale Winds" "Sunny disposition"
```

will add a line to the addressbook with email `test@example.com` under name
`Gale Winds` and with additional information `Sunny disposition`. The order
matters.


## From Mutt

It is necessary to configure mutt to use `simple_addr.py`. The primary way to do
this is to set mutt's `query_command` in order to reference the addressbook, and
to add a mutt-macro to add an address from an email.


### Querying the addressbook from mutt

In one's `.muttrc`, add the line

```bash
set query_command = "python /path/to/simple_addr.py -d <dir> -f <file> '%s'"
```

with appropriate choices for `<dir>` and `<file>`. If one is using a bash alias
with `sadr` already pointing to the correct addressfile, then this can be
simplified to

```bash
set query_command = "sadr '%s'"
```

To use, suppose you are writing a message in mutt. You type `m` to compose a
message, and mutt presents you with a `To:` field and awaits the address.
Hitting `<TAB>` brings up one's mutt alias file. Hitting `CTRL-T` queries
`simple_addr.py`.

After using `CTRL-T` and querying `simple_addr.py`, one can highlight the
desired address and use enter to select it. You can tag multiple people from one
query by using `t` on each desired address and `;m` to have them all placed on
the `To:` line. You can use `A` to perform additional queries.


### Adding an address from a mutt message

In one's `.muttrc`, add the line

```bash
macro index,pager A "<pipe-message>sadr --mutt-add<return>" "Add sender to simple_addr.py"
```

to add a macro. This makes it so that when you type `A`, the sender of the
message (as deduced from the `From:` field of that email) is added to your
`simple_addr.py` addressbook.


## Tips

### Convert gmail contacts to this format

It is easy to convert gmail contacts to this format. (And other formats, for
that matter, but this is part of a grander gmail --> mutt progression for me).
For convenience, I placed the script I used to convert my contacts to this form
in `convert_gmail_contacts.py`. Your mileage may vary.


## Imperfections

There are many. But in particular, the big ones are

- there is no provided way to remove an address from the addressbook. It is
  necessary to manually open the addressbook file and remove it.
- similary, there is no way to edit an address from the addressbook. Current
  solution: don't mistype anything and don't let anyone change anything.
- parsing an address from mutt is not particularly robust. There exist valid
  addresses that will confuse the parser, arising essentially from the fact that
  addresses in headers can contain comments and these comments are annoying.


There is no end of other things that might arise. But this is a one-day project
(that I am actually currently using).


## License Info

This is released under the MIT License.

Copyright (c) 2024 David Lowry-Duda <david@lowryduda.com>.

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
