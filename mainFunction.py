'''
What is a Dunder?
“Dunder” method name is the common pronunciation
for python's built-in method names that
start and end with double underscores.
Since “Dunder” is easier to say than
“double underscore”, the name stuck.
These methods are also sometimes
referred to as “Special Methods” or
“Magic Methods”

eg: __name__ = "__main__"

__name__ variabel is a special variable that represents
the name of a python file

Running any py prgrm as a script then the __name__ is always main.
Running it as a moduel returns the name of the file as the __name__


USES:
-----

- Allows us to run the same file differently in different scenarios.
- If a module file we have have things that we dont want to be run
when we import in another file , we can use _name__ in the first
file which we will import_
- It is a best practice.

Python starts execution from the first line. Different from other prgrmn languages.

'''

print(__name__)