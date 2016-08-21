"""
Given an "out" string length 4, such as "<<>>",
and a word, return a new string where the word 
is in the middle of the out string, e.g. "<<word>>".
"""


def make_out_word(out, word):
	out_first=out[:2]
	out_last=out[2:]
	return out_first+word+out_last
  

print make_out_word('<<>>', 'Yay') # '<<Yay>>'
print make_out_word('<<>>', 'WooHoo') # '<<WooHoo>>'
print make_out_word('[[]]', 'word') # '[[word]]'

