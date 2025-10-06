sentence = input ("enter a sentence : ").lower()
words=sentence.split()
word_count={}
for word in words :
    word_count [word]=word_count.get(word,0)+1

print ("\nword occurence :")
for word , count in word_count.items():
    print(f"{word}:{count}")