# Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). 
# Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

# Example: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => returns "This is a test"



def spin_words(sentence):
    splitSen = sentence.split()
    ans = []
    for i in splitSen:
        if len(i) >= 5:
            ans.append(i[::-1])
        else:
            ans.append(i)
    return ' '.join(ans)


