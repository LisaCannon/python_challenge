#import regular expressions module
import re 

#change the path to pull in any txt file that consists of a paragraph of text
#assign the string to the variable called paragraph
f_open = open('test_para.txt','r')
paragraph = f_open.read()
f_open.close()

#create a list of the sentences that make up the paragraph
sentences = re.split("(?<=[.!?]) +", paragraph)

#initialize values 
words_count = []
l_count = 0
#looking at a the sentence in the sentence list
for sent in sentences:
    #split the sentence into words
    words = sent.split()
    w_count = len(words)
    #add the total number of words to a word_count list
    words_count.append(w_count)
    #looking at each word 
    for w in words:
        #count the letters and add to a total letter count
        l_count += sum(c.isalpha() for c in w)
        
#calculations for totals and averages   
sent_count = len(sentences)
total_words = sum(words_count)
total_sent = len(words_count)
avg_words = total_words/total_sent
avg_letters = l_count/total_words 

#output
print("Paragraph Analysis")
print("---------------------")
print(f"Approximate Word Count: {total_words}")
print(f"Approximate Sentence Count: {total_sent}")
print(f"Average Word Length: {avg_letters}")
print(f"Average Sentence Length: {avg_words}")
    