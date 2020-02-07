sentence = 'Welcome to edunbox this program shows creation of sets and some of its functions'
words=sentence.split()
word_count=dict()
for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1
print('word occurances:')
for key,value in word_count.items():
    print('{}\t{}'.format(key,value))
