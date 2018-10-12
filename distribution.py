"""
distribution.py
Author: Johariajwang
Credit: megsnyder

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

rr = input("Please enter a string of text (the bigger the better): ") 

st=rr.lower()

print(st)
i=len(st)
l=list(range(1,i))


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
    if st.count('m')==i:
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

