intro = input("Enter a random word")
intro=intro.lower()
letters = set('abcdefghijklmnopqrstuvwxyz')
sentence = set(intro)
print(sentence)
dif = letters-sentence
print(dif)
if len(dif) == 0:
    print("Your word is a pangram")
else:
    print("Your word is not a pangram")