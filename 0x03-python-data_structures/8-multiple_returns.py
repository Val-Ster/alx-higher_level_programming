#!/usr/bin/python3
def multiple_returns(sentence):
    # Check if the sentence is empty
if len(sentence) == 0:
    # Return a tuple with length 0 and None as the 1st character
return (0, None)
else:
    # Return a tuple with length and the 1st character
return (len(sentence), sentence[0])
