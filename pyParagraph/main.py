import re 

f_open = open('test_para.txt','r')
paragraph = f_open.read()
f_open.close()

sentences = re.split("(?<=[.!?]) +", paragraph)
sent_count = len(sentences)

words_count = []
l_count = 0
for sent in sentences:
    words = sent.split()
    w_count = len(words)
    words_count.append(w_count)
    for w in words:
        l_count += sum(c.isalpha() for c in w)
        
   
total_words = sum(words_count)
total_sent = len(words_count)
avg_words = total_words/total_sent
avg_letters = l_count/total_words 
print(f"Approximate word count: {total_words}")
print(f"Approximate sentence count: {total_sent}")
print(f"Average Word Length: {avg_letters}")
print(f"Average Sentence Length: {avg_words}")
    