import collections

file = open("C:\\Users\\Anton\\Desktop\\98-0.txt", encoding='utf-8')

wordcount = {}
stopwords = set(line.strip() for line in open('C:\\Users\\Anton\\Desktop\\stopwords', encoding='utf-8'))

for word in file.read().lower().split():
    word = word.replace('.', '')
    word = word.replace(',', '')
    word = word.replace('"', '')
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word]=1
        else:
            wordcount[word]+=1
            
d = collections.Counter(wordcount)
                   
for word, count in d.most_common(10):
    print(word, ": ", count)