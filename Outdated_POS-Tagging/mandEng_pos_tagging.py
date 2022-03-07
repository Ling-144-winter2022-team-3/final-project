#This program evaluates spaCy's ability to word tokenize and tag the part of speech of mixed English-Mandarin text. It will display a dataframe that organizes a maximum of four most frequent adpositions and their associated counts. It will also output a processed txt file features a column of tokens, a column of part-of-speech tags, and a column of fine-grained details of the lexical categorization.


#Step 1: Ensure that Pandas and spaCy are both installed.
#Type in the bash shell, not in the python interpreter, 
#pip install pandas
#AND
#!pip install -U spacy

#Step 2: Import modules or libraries from spaCy and pandas.
import spacy
from spacy import displacy
from collections import Counter
import pandas as pd

#Step 3: Specification of the pandas display settings
#pd.set_option("max_rows", 400)
#pd.set_option("max_colwidth", 400)


#Step 4: Download the machine learning nlp model in the shell/terminal.

#Type in the terminal/shell the following: python -m spacy download zh_core_web_md

#Preface python with an exclamation point (!) to run this program in GoogleColab.


#Step 5: Load the machine learning nlp model in the program script.

nlp = spacy.load('zh_core_web_md')

#When opening a file in Repl.it, the file path must be specified via a system argument and a commandline in the shell, not directly in the open function.


#Manipulate the machine-learning model: sm, md, and lg


#Step 6: Open the file that encapsulates the text of interest/under investigation, and extract an nlp-processed text from it.

#file1 = open('/final-project/POS-Tagging/sunfish.txt','r',encoding = 'utf-8')

import sys

file1 = open(sys.argv[1],'r', encoding = 'utf-8')

#---------Statement in the commandline-------

#python mandEng_pos_tagging.py ~/final-project/POS-Tagging/sge-dominated.txt ~/final-project/POS-Tagging/sge-dominated_processed_text.txt

#---------------------------------------------

#Note: The syntax for passing two txt files into a script program is python program.py ~/filepath1/filename1.py ~/filepath2/filename2.py .
#The first txt file can be referenced as by index 1 while the second txt file can be referenced via index 2 in the commandlines.

#file.read() reads all the content of a file into a single, continuous string

text = file1.read()

document = nlp(text)

file1.close()

#Step 7: Open the file that will retain the output.

#file2 = open('/final_project/POS-Tagging/sunfish_processed.txt','w', encoding = 'utf-8')

file2 = open(sys.argv[2],'w',encoding = 'utf-8')


document_1 = list(document)

document_2 = ""

for item in document_1:
  item = str(item)
  document_2+=item

file2.write("token"+","+"POS"+","+"details"+","+"\n")

for token in document:
  file2.write(str(token)+","+str(token.pos_)+","+str(token.dep_)+"\n")
 

#Step 8: Initialize an empty list to store words of a particular lexical category, conduct a for loop iterating through the tokens in the nlp-processed document, and append the tokens if they classify in that lexical category

adps = []

for token in document:
  if token.pos_ == 'ADP':
    adps.append(token)

#Step 9: Total up the number of adposition types (i.e., unique adpositions).

adpositions_tally = Counter(adps)

#Step 10: Construct a dataframe of the four most frequent adpositions.

#adpositions_tally.most_common generates a list of adposition-adposition count tuples.
  
df = pd.DataFrame(adpositions_tally.most_common(), columns=['asposition','count'])

print(df)

file2.close()
