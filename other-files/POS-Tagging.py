
#Installation of Libraries and Language Model

#Prior to implementing this program, install pandas and spaCy in the bash shell, not in the python interpreter.
#Type the following the the bash shell:
#pip install pandas
#(!)pip install -U spacy #Preface the command with an exclamation point ! in Google Colab.
#

#Download the nlp machine learning model from the spaCy library in the python interpreter.
#Type the following in a commandline:
#(!) python -m spacy download zh_web_core_md #Preface the command with an exclamation point ! in Google Colab.

#Importation of modules

import spacy
from spacy import displacy
from collections import Counter
import pandas as pd


import nltk
nltk.download('popular')
nltk.download('tagsets')

import re

#Loading of the nlp Machine-Learning Model
#Load of the nlp machine-learning model, and allocate it in the variable nlp

nlp = spacy.load('zh_core_web_md')



def POS_Tagger(comp_w_t_sent):
  """
This function annotates a language-compartmentalized, word-tokenized sentence with abbreviated tags symbolic of lexical categories. In effect, it transforms a sentence list of monolingual fragment lists of tokens into a sentence list of monolingual fragment lists of token-tag tuples.
  """
  annotated_comp_w_t_sent = []
  for fragment in comp_w_t_sent:
    #reference string: fragment[0]
    m = re.search(r'[a-zA-Z]',fragment[0])
    #We do not need to iterate through the token strings of fragment to annotate them.
    if m == None:#An initial Mandarin word signals an entirely Mandarin fragment.
      #Invoke the nlp model to word-tokenize, and guarantee that the output of the nlp tokenizer is a list.
      reassembled_fragment = " ".join(fragment)
      tokens = nlp(reassembled_fragment)
      tokens = list(tokens)
      tagged_tokens = [(str(s),s.pos_) for s in tokens]
        #We could zip a list of tags and a list of tokens into a dictionary and   extract a list of token-tag tuples from the dictionary, though this would ruin the linear order of words.
      #Append the list of tag-token tuples to the output list.
      annotated_comp_w_t_sent.append(tagged_tokens)
    if type(m) == re.Match:
      #An initial English word signals an entirely English fragment.
      #Call the pos_tag function of nltk. We can forgo the word_tokenize function since the fragment is already word-tokenized.
      tagged_tokens = nltk.pos_tag(fragment)
      #Append the list of tag-token tuples to the output list.
      annotated_comp_w_t_sent.append(tagged_tokens)
  return annotated_comp_w_t_sent



print(POS_Tagger([['你', '要', '那', '个'], ['chocolate'], ['你', '刚', '才', '吃', '的', '那', '个'], ['chocolate'], ['你']]))

print(POS_Tagger([['我', '是', '从'], ['camp'], ['那', '边', '拿', '来', '的', '自', '从'], ['mark'], ['那', '时', '拿', '来', '了', '之', '后']]))