#variables
pyg = 'ay'
original = raw_input('Enter a word:')
word = original.lower()
first = word[0]
#combining variables
new_word = word + first + pyg
new_word = new_word[1:len(new_word)]
#if else statements no need of elif
if len(original) > 0 and original.isalpha():
    print ("this is your word converted to PygLatin: " + new_word)
else:
    print 'empty'
