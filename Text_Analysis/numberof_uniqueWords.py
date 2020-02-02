#python code to plot graph
import os 
import pandas as pd 
from collections import *
book_dir = "D:\\dinesh\\june-22\\Books"
os.listdir(book_dir) 

def read_book(title_path): #read a book and return it as a string 
	with open(title_path, "r", encoding ="utf8") as current_file: 
		text = current_file.read() 
		text = text.replace("\n", "").replace("\r", "") 
	return text 
def word_stats(word_counts):     # word_counts = count_words_fast(text)    
    num_unique = len(word_counts) 
    counts = word_counts.values() 
    return (num_unique, counts)

def count_words_fast(text):      #counts word frequency using Counter from collections 
    text = text.lower() 
    skips = [".", ", ", ":", ";", "'", '"'] 
    for ch in skips: 
        text = text.replace(ch, "") 
    word_counts = Counter(text.split(" ")) 
    return word_counts 


text = read_book("D:\\dinesh\\june-22\\Books\\English\\shakespeare\\Romeo and Juliet.txt") 
  
word_counts = count_words_fast(text)          
(num_unique, counts) = word_stats(word_counts) 
print(num_unique, sum(counts)) 
