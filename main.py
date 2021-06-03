#!/usr/bin/env python
# coding: utf-8

# In[92]:


import nltk
from nltk.corpus import *
import random
import matplotlib


# In[93]:


data = None
cuss_words = {
    'english':[],
    'hindi':[]
}
sr = stopwords.words('english')


# In[94]:


with open('data.txt', 'r') as data_file:
	data = data_file.read()
	data_file.close()
with open('cuss_words_english.txt', 'r') as english_cuss:
    for cuss in english_cuss:
        cuss_words['english'].append(cuss.replace('\n',''))
    english_cuss.close()
        
with open('cuss_words_hindi_beginners.txt', 'r') as hindi_beginners:
    for cuss in hindi_beginners:
        cuss_words['hindi'].append(cuss.replace('\n',''))
    hindi_beginners.close()

with open('cuss_words_hindi_commonly_used.txt', 'r') as hindi_beginners:
    for cuss in hindi_beginners:
        cuss_words['hindi'].append(cuss.replace('\n',''))
    hindi_beginners.close()

with open('cuss_words_hindi_challengers.txt', 'r') as hindi_beginners:
    for cuss in hindi_beginners:
        cuss_words['hindi'].append(cuss.replace('\n',''))
    hindi_beginners.close()

with open('cuss_words_hindi_champs.txt', 'r') as hindi_beginners:
    for cuss in hindi_beginners:
        cuss_words['hindi'].append(cuss.replace('\n',''))
    hindi_beginners.close()
    
with open('cuss_words_hindi_legends.txt', 'r') as hindi_beginners:
    for cuss in hindi_beginners:
        cuss_words['hindi'].append(cuss.replace('\n',''))
    hindi_beginners.close()


# In[95]:


tokens = [x for x in data.split()]
clear_tokens = tokens[:]


# In[96]:


for token in tokens:
	if token in sr:
		clear_tokens.remove(token)


# In[97]:


freq = nltk.FreqDist(clear_tokens)


# In[98]:


freq.plot(20)


# In[99]:


print(f'The Topic in this data is \'{freq.most_common()[0][0]}\'!')


# In[100]:


slang_counter = 0
#Check for English Slangs
for cuss in cuss_words['english']:
    if cuss in clear_tokens:
        slang_counter = slang_counter + 1
        
for cuss in cuss_words['hindi']:
    if cuss in clear_tokens:
        slang_counter = slang_counter + 1

slang_average = slang_counter/len(clear_tokens)

print(f'{slang_average} is your Slang Average')
if slang_average > 5:
    print(f'Well {random.choice(cuss_words["hindi"])}, You need to Control Yourself!')
elif slang_average == 0:
    print(f'Wait what? Its incredible, that you don\'t slang {random.choice(cuss_words["english"])}')
else:
    print(f'Well, You are under Control {random.choice(cuss_words["hindi"])}  but try to eliminate Slangs in your Conversation')
