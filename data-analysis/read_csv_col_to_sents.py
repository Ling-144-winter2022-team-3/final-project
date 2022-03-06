# Preprocessing Step

# - Read the column titled “sentence” in dataset1.csv as well as in dataset2.csv into a single list_of_sentences.
# - Filter out "v-noise" from the sentence string elements of the list
# - Split list_of_sentences into two different array, one contains only Chinese-major sentences, another contains only English-major sentences.
# - Output both array as two seperate datasets titled dataset_eng_major.txt and dataset_ch_major.txt

from pandas import *
import re 

#Step 2: read the two csv files into two dataframes by means of the read_csv function
dataframe_1 = read_csv('../data/dataset1.csv')
dataframe_2 = read_csv('../data/dataset2.csv')
 
#We are reading csv files, not txt files, so we do not employ the open function above, but we can specify the file path in the read_csv function 
#just as we would in the open function, according to the code snipped accessible via the link <https://www.codegrepper.com/code-examples/python/how+to+get+csv+file+path+in+python>.
#Step 3: Convert the column data for "sentence" to list data. Note that dataset1_sentences and dataset2_sentences are of the list data type.
dataset1_sentences = dataframe_1['sentence'].to_list()
dataset2_sentences = dataframe_2['sentence'].to_list()

#Step 4: Concatenate the lists together, and output the list data in the form of a descriptive print statement.
list_of_sentences = dataset1_sentences + dataset2_sentences

# Print the length of list_of_sentences in a f-string formatted text
print(f"The length of list_of_sentences is {len(list_of_sentences)}")

# Remove "v-noise" from each sentence string element of the list MandEng_mixed_sentences via a filer-by-regex technique.
list_of_sentences_no_vnoice = []

for i in range(len(list_of_sentences)):
  # reference string: string element of MandEng_mixed_sentences (i.e., MandEng_mixed_sentences[i])
  MandEng_mixed_sentences_1 = re.sub(r'<v-noise>', " ", list_of_sentences[i])
  list_of_sentences_no_vnoice.append(MandEng_mixed_sentences_1)

# Print the length of list_of_sentences_no_vnoice in a f-string formatted text
print(f"The length of list_of_sentences_no_vnoice is {len(list_of_sentences_no_vnoice)}")

# Verify if the entire dataset contains v-noise 
for i in range(len(list_of_sentences_no_vnoice)):
  if re.search(r'<v-noise>', list_of_sentences_no_vnoice[i]):
    print(f"The sentence {list_of_sentences_no_vnoice[i]} contains <v-noise>")

# Step 5: Split the list_of_sentences_no_vnoice into two different array, one contains only Chinese-major sentences, another contains only English-major sentences.
# If the amount of English words reaches 50% of the total amount of words in the sentence, then the sentence is considered to be English-major.
english_major = []
chinese_major = []

for i in range(len(list_of_sentences_no_vnoice)):
  # get all of the english words in this sentence
  english_words = re.findall(r'[a-zA-Z]+', list_of_sentences_no_vnoice[i])
  # get the amount of words in the current sentence
  sentence_length = len(list_of_sentences_no_vnoice[i].split())
  # If the amount of English words is more than 55% of the total amount of words in the sentence, then the sentence is considered to be English-major.
  if len(english_words) / sentence_length >= 0.55:
    english_major.append(list_of_sentences_no_vnoice[i])
  else:
    chinese_major.append(list_of_sentences_no_vnoice[i])
  
print(f"There are {len(english_major)} English-major sentences in the dataset.")
print(f"There are {len(chinese_major)} Chinese-major sentences in the dataset.")
print(f"Total up to now: {len(english_major) + len(chinese_major)} sentences in the dataset.")

# Write english_major out to dataset_eng_major.txt
with open('dataset_eng_major.txt', 'w') as f:
  for i in range(len(english_major)):
    f.write(english_major[i] + '\n')

# Write chinese_major out to dataset_ch_major.txt
with open('dataset_ch_major.txt', 'w') as f:
  for i in range(len(chinese_major)):
    f.write(chinese_major[i] + '\n')