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


