#!/usr/bin/python

# To use:
# python soundnotes.py <name-of-flashcard.txt> <directory-name>

import sys
import os
from gtts import gTTS as gtts

# takes command line argument for file name
card_file = sys.argv[1]
# takes command line argument for the directory name where the mp3 files will
# be stored, and makes the directory if it does not exist already
directory = sys.argv[2]
if not os.path.exists(directory):
    os.makedirs(directory)
# prints file name to command line
print ("The subject of these flashcards are: ",card_file)
# opens file with name defined on the command line
f = open(card_file)
# counts the number of lines in the file
num_lines = sum(1 for num_lines in open(card_file))

# opens an empty list, then fills it with each line in the text file
my_list = list(f)
length = len(my_list)

# prints the number of 'flashcards' tp the command line
q_num = num_lines/3
print ("my_list is",length," and the number of questions is: ",q_num)

# closes the file
f.close()

for b in range(q_num):
    text = str(my_list[3*b + 1]+my_list[3*b + 2])
    name = str(my_list[3*b])+'.mp3'
    soundbite = gtts(text, lang='tr')
    soundbite.save(directory+"/"+name)