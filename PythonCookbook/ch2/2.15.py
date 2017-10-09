"""
Problem:
You want to create a string in which embedded variable names are substituted with a
string representation of a variable's value.

Solution:
Python has no direct support for simply substituting variable values in strings. However,
this feature can be approximated using the format() method of strings. For example:
"""
import string
import sys

s = '{name} has {n} messages.'
print(s.format(name='Guido', n=37))

"""
Alternatively, if the values to be substituted are truly found in variables, you can use the
combination of format_map() and vars(), as in the following:
"""

name = 'Guido'
n = 37
print(s.format_map(vars()))
print(vars())
print(locals())

"""
One subtle feature of vars() is that it also works with instances. For example:
"""
class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n
a = Info('guido', 37)
print(vars(a))
print(s.format_map(vars(a)))

"""
One downside of format() and format_map() is that the they do not deal gracefully with
missing values. For example:
"""
try:
    s.format(name='Guido')
except KeyError as err:
    print('Encounter KeyError: {}'.format(err))

"""
One way to avoid this is to define an alternative dictionary class with a __missing__()
method, as in the following:
"""
class safesub(dict):
    def __missing__(selfself, key):
        return '{' + key + '}'

"""
Now use this class to wrap the inputs to format_map():
"""
del n
print('n' in vars())
print(s.format_map(safesub(vars())))

"""
If you find yourself frequently performing these these steps in your code, you could hide the
variable substitution process behind a small utility function that employs a so-called
"frame hack." For example:
"""
def sub(text):
    # _getframe(1).f_locals is equivalent to vars() or locals()
    return text.format_map(safesub(sys._getframe(1).f_locals))


"""
Now you can type things like this:
"""
name = 'Guido'
n = 37
print(sub('Hello {name}'))
print(sub('You have {n} messages.'))
print(sub('Your favorite color is {color}.'))

"""
Discussion
The lack of true variable interpolation in Python has led to a variety of solutions over
the years. As an alternative to the solution presented in this receipt, you will sometimes
see string formatting like this:
"""
name = 'Guido'
n = 37
# print('%(name) has %(n) messages.' % vars())

"""
You may also see the use of template strings:
"""
s = string.Template('$name has $n messages.')
print(s.substitute(vars()))

"""
However, the format() and format_map() methods are more modern than either of
these alternatives, and should be preferred. One benefit of using format() is that you
also get all of the features related to string formatting (alignment, padding, numerical
formatting, etc.), which is simply not possible with alternatives such as Template string
objects.

Parts of this receipt also illustrate a few interesting advanced features. This little-known
__missing__() method of mapping/dict classes is a method that you can define to
handle missing values. In the safesub class, this method has been defined to return
missing values back as a placeholder. Instead of getting a KeyError exception, you
would see the missing values appearing in the resulting string (potentially useful for
debugging).

The sub() function uses sys._getframe(1) to return the stack frame of the caller. From
that, the f_locals attribute is accessed to get the local variables. It goes without saying
that messing around with stack frames should probably be avoided in most code. However,
for utility functions such as a string substitution feature, it can be useful. As an
aside, it's probably worth noting that f_locals is a dictionary that is a copy of the local
variables in the calling function. Although youcan modify the contents of f_locals,
the modifications don't actually have any lasting effect. Thus, even though accessing a
different frame might look evil, it's not possible to accidentally overwrite variables
or change the local environment of the caller.
"""
