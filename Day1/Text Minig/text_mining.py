# -*- coding: utf-8 -*-


f = open('shakespeare.txt', 'r')
raw_txt = ''
for line in f:
    raw_txt += line
    
raw_txt_list = raw_txt.split()

# O(n^2)

count_words = []
for i in range(len(raw_txt_list)):
    word = raw_txt_list[i]
    cnt = 0
    for j in range(i, len(raw_txt_list)):
        if raw_txt_list[j] is word:
            cnt += 1
        
    count_words.append([word, cnt])
    


sorted_raw_list = raw_txt_list
sorted_raw_list.sort()
i = 0
count_words = []
while i < len(sorted_raw_list):
    cnt = 0
    word = sorted_raw_list[i] # && , || , ! => and, or, not
    while i < len(sorted_raw_list) and word == sorted_raw_list[i] :
        i += 1
        cnt += 1
    count_words.append([word, cnt])
    

dict_words = dict()

words = list(set(raw_txt_list))
counters = [0 for i in range(len(words))]

dict_words = dict(zip(words, counters))

for word in raw_txt_list:
    dict_words[word] += 1

counter_words = list(dict_words.values())
counter_words.sort()
sorted_words = dict()
for counter_word in counter_words:
    for key in dict_words.keys():
        if dict_words[key] == counter_word:
            sorted_words[key] = counter_word










