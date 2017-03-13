
# coding: utf-8

# In[115]:

lines = []
for line in open('Building_Global_Community.txt'):
    line = line.strip()
    lines.append(line)


# In[116]:

# read sentences from file "Building_Global_Community.txt"
lines


# In[117]:

lines[3]


# In[90]:

# split sentences into words (split, or nltk word_tokenize)
get_ipython().system('pip3 install nltk -U')


# In[91]:

import nltk
nltk.download('punkt')


# In[118]:

from nltk import word_tokenize
print(word_tokenize(lines[3]))


# In[119]:

from nltk import wordpunct_tokenize
print(wordpunct_tokenize(lines[3]))


# In[120]:

words_test = wordpunct_tokenize(lines[3])


# In[121]:

words_test


# In[122]:

for line in lines:
    print(wordpunct_tokenize(line))


# In[123]:

words=[]
for line in lines:
    for x in wordpunct_tokenize(line):
        words.append(x)


# In[124]:

words


# In[146]:

len(words)


# In[147]:

words_1 = [word for word in words if word.isalpha() is True]


# In[155]:

words_1


# In[154]:

for word in words_1:
    if word.isdigit() is True:
        print(word)


# In[156]:

# normalize words and count ('Word' and 'word' are considered as the same word)
words_lower = []
for x in words_1:
    words_lower.append(x.lower())


# In[157]:

words_lower


# In[158]:

nltk.download('stopwords')


# In[2]:

from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))


# In[3]:

stopwords


# In[160]:

data = [word for word in words_lower if word not in stopwords]


# In[161]:

# count the occurance of words (counting exmaple)
from collections import Counter


# In[162]:

counter = Counter(data)


# In[163]:

counter


# In[164]:

counter.most_common(20)


# In[165]:

# save as csv file
import csv


# In[166]:

with open('wordcount_Olive.csv', 'w') as csvfile:
    # set up header
    fieldnames = ['word', 'count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for word, count in counter.most_common():
        writer.writerow({'word': word, 'count': count})


# In[ ]:



