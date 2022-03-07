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

#Manipulate the machine-learning model: sm, md, and lg

test_string = "那 时 候 我 直 接 这 样 我 好 像 是 啊 just speak straight to the point lah like what i want to do lah wa ai ker  do my number my my number one and my number two lah yeah "

def total_number_of_words(text):
  """
  This function computes the total number of words in a mixed Mandarin-English text     expressed as a string.
  """
  processed_string = nlp(text)
  processed_string = str(processed_string)
  #Note: the data type of the output of nlp is 'spacy.tokens.doc.Doc'
  word_tokenized_list = processed_string.split()
  return len(word_tokenized_list)


print(total_number_of_words(test_string))

