Escape characters

'Say hi to bob\'s mother'

###

\'
\"
\n - newline
\t - tab
\\ Backslash


  
###

Raw string

r'That is Carol\'s cat'
That is Carol\'s cat


###

Multi line """

Print("""Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary,
and extortion.
Sincerely,
Bob.""")

Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary,
and extortion.
Sincerely,
Bob.

spam = """Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary,
and extortion.
Sincerely,
Bob."""

spam
"Dear Alice,\nEve's cat has been arrested for catnapping, cat burglary,
and extortion.\nSincerely,\nBob."

###

print(len(spam))

