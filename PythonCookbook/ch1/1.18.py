"""
1.18. Mapping Names to Sequence Elements

Problem
You have code that accesses list or tuple elements by position, but this
makes the code somewhat difficult to read at times. You'd also like to be
less dependent on position in the structure, by accessing the elements by
name.

Solution
collections.namedtuple() provides these benefits, while adding minimal
overhead over using a normal tuple object. collections.namedtuple()
is actuall a factory method that returns a subclass of the standard
Python tuple type. You feed it a type name, and the fields it should have,
and it returns a class that you can instantiate, passing in values for fields
you've defined, and so on. For example:
"""

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub, sub.addr, sub.joined)

"""
Although an instance of a namedtuple looks like a normal class instance, it
is interchangeable with a tuple and supports all of the usual tuple operations
such as indexing and unpacking. For example:
"""

print(len(sub))
addr, joined = sub
print(addr, joined)

"""
A major use case for named tuples is decoupling your code from the position 
of the elements it manipulates. So, if you get back a large list of tuples
from a database call, then manipulate them by accessing the positional elements,
your code could break if, say, you added a new column to your table.
Not so if you first cast the returned tuples to namedtuples.

To illustrate, here is some code uding ordinary tuples:
"""


def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total


"""
References to positional elements often make the code a bit less expressive
and more dependent on the structure of the records. Here is version that
uses a namedtuple:
"""

Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


"""
Naturally, you can avoid the explicit conversion to the Stock namedtuple if
the records sequence in the example already contained such instances.

Discussion
One possible use of a namedtuple is as a replacement for a dictionary,
which requires more space to store. Thus, if you are building large data
structures involving dictionaries, use of a namedtuple will be more effcient.
However, be aware that unlike a dictionary, a namedtuple is immutable.
For example:
"""

s = Stock('ACME', 100, 123.45)
print(s)
try:
    s.shares = 75
except Exception as e:
    print(e)

"""
If you need to change any of the attributes, it can be done using the
_replace() method of a namedtuple instance, which makes an entirely new
namedtuple with specified values replaces. For example:
"""

s = s._replace(shares=75)
print(s)

"""
A subtle use of the _replace() method is that it can be a convenient way to
populate named tuples that have optional or missing fields. To do this, you
make a prototype tuple containing the default values and then use _replace()
to create new instances with values replaced. For example:
"""

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)


# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)


"""
Here is an example of how this code would work:
"""
a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))

b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_stock(b))

"""
Last, but not least, it should be noted that if your goal is to define an
efficient data structure where you will be changing various instance attributes,
using namedtuple is not your best choice. Instead, consider defining a class
using __slots__ instead (see Recipe 8.4).
"""
