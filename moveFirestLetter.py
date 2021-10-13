"""

https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python

Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !

"""

def pig_it(text):

    return " ".join( map( lambda word: word[1:] + word[0]+"ay" if word.isalpha() else word,   text.split(" ") ) )



print( pig_it('Pig latin is cool') ) #'igPay atinlay siay oolcay'
print( pig_it('This is my string') )#'hisTay siay ymay tringsay'
print( pig_it('uwu') )