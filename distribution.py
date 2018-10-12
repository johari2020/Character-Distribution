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

'''
import string
print(str.ascii_lowercase)
'''
'''
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
'''
i=len(st)
l=list(range(1,i))
print(l)

while i > 0:
    if st.count('a')==i:
        print("a"*(st.count('a')))
    if st.count('b') == i:
        print("b"*(st.count('b')))
    if st.count('c')==i:
        print("c"*(st.count('c')))
    if st.count('d')==i:
        print("d"*(st.count('d')))
    if st.count('e')==i:
        print("e"*(st.count('e')))
    if st.count('f')==i:
        print("f"*(st.count('f')))
    if st.count('g')==i:
        print("g"*(st.count('g')))
    if st.count('h')==i:
        print("h"*(st.count('h')))
    if st.count('i')==i:
        print("i"*(st.count('i')))
    if st.count('j')==i:
        print("j"*(st.count('j')))
    if st.count('k')==i:
        print("k"*(st.count('k')))
    if st.count('k')==i:
        print("l"*(st.count('l')))
    if st.count('l')==i:
        print("m"*(st.count('m')))
    if st.count('n')==i:
        print("n"*(st.count('n')))
    if st.count('o')==i:
        print("o"*(st.count('o')))
    if st.count('p')==i:
        print("p"*(st.count('p')))
    if st.count('q')==i:
        print("q"*(st.count('q')))
    if st.count('r')==i:
        print("r"*(st.count('r')))
    if st.count('s')==i:
        print("s"*(st.count('s')))
    if st.count('t')==i:
        print("t"*(st.count('t')))
    if st.count('u')==i:
        print("u"*(st.count('u')))
    if st.count('v')==i:
        print("v"*(st.count('v')))
    if st.count('w')==i:
        print("w"*(st.count('w')))
    if st.count('x')==i:
        print("x"*(st.count('x')))
    if st.count('y')==i:
        print("y"*(st.count('y')))
    if st.count('z')==i:
        print("z"*(st.count('z')))
        
    i-=1
'''
print("d"*st.count('d'))
    print("e"*st.count('e'))
    print("f"*st.count('af'))
    print("g"*st.count('g'))
    print("h"*st.count('h'))
    print("i"*st.count('i'))
    print("j"*st.count('j'))
    print("k"*st.count('k'))
    print("d"*st.count('l'))
    print("m"*st.count('m'))
    print("n"*st.count('n'))
    print("o"*st.count('o'))
    print("p"*st.count('q'))
    print("r"*st.count('r'))
    print("s"*st.count('s'))
    print("t"*st.count('t'))
    print("u"*st.count('u'))
    print("v"*st.count('v'))
    print("w"*st.count('w'))
    print("x"*st.count('x'))
    print("y"*st.count('y'))
    print("z"*st.count('z'))
'''