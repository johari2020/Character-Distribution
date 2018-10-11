"""
distribution.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""

st = input("Please enter a string of text (the bigger the better): ") 
import string
print(str.ascii_lowercase)
""""
a = (st.count('a'))
b = (st.count('b'))
c = (st.count('c'))
d = (st.count('d'))
e = (st.count('e'))
f = (st.count('af'))
g = (st.count('g'))
h = (st.count('h'))
i = (st.count('i'))
j = (st.count('j'))
k = (st.count('k'))
l = (st.count('l'))
m = (st.count('m'))
n = (st.count('n'))
o = (st.count('o'))
q = (st.count('p'))
r = (st.count('q'))
s = (st.count('r'))
t = (st.count('s'))
u = (st.count('t'))
v = (st.count('u'))
w = (st.count('v'))
x = (st.count('w'))
y = (st.count('x'))
z = (st.count('y'))
""""
