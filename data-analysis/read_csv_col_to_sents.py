#This script reads the column under the header "sentence" from dataset1.csv and the column titled "sentence" from dataset2.csv into two lists and concatenates thee lists together.
#This script also filters out the "v-noise" from each sentence string element.

#Step 1: Install pandas in the bash shell, not into the python interpreter prior to importing the * module from pandas.
#Type the following statement in a commandline to install it: pip install pandas.

from pandas import *


#Step 2: read the two csv files into two dataframes by means of the read_csv function

dataframe_1 = read_csv('/data/dataset1.csv')
dataframe_2 = read_csv('/data/dataset2.csv')
 
#We are reading csv files, not txt files, so we do not employ the open function above, but we can specify the file path in the read_csv function 
#just as we would in the open function, according to the code snipped accessible via the link <https://www.codegrepper.com/code-examples/python/how+to+get+csv+file+path+in+python>.


#Check the dataframe by printing the first five and last five entries.

dataframe_1.head()
dataframe_1.tail()

dataframe_2.head()
dataframe_2.tail()


#Step 3: Convert the column data for "sentence" to list data. Note that dataset1_sentences and dataset2_sentences are of the list data type.

dataset1_sentences = dataframe_1['sentence'].to_list()
dataset2_sentences = dataframe_2['sentence'].to_list()

#Step 4: Concatenate the lists together, and output the list data in the form of a descriptive print statement.

MandEng_mixed_sentences = dataset1_sentences + dataset2_sentences

print(f'The mixed Mandarin-English sentences from dataset1.txt and dataset2.txt include the following: {MandEng_mixed_sentences}')

#Remove "v-noise" from each sentence string element of the list MandEng_mixed_sentences via a filer-by-regex technique.

import re

for i in range(len(MandEng_mixed_sentences))):
 #reference string: string element of MandEng_mixed_sentences (i.e., MandEng_mixed_sentences[i])
 MandEng_mixed_sentences_1 = re.sub(r'<.*>', " ", MandEng_mixed_sentences[i])

print(MandEng_mixed_sentences_1)

#In our Mandarin-English code-switching final project, we intend for an nlp machine learning model in spaCy to process each sentence string element of a list in anoter script. Since it is difficult to design a script to manipulate each string element of a list in a different script,
#would it behoove us to write all the string elements to separate lines of an output.txt and instruct spaCy to read and manipulate each line of the output.txt?  


