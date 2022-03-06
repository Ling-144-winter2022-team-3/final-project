#Installation of Libraries
#In order to wield this program, pandas and spaCy must be installed in the bash shell, not in the python interpreter.

#Type the following in the bash shell:
#pip install pandas
#pip install -U spacy (hyphen, not a dash)
#Precede pip by ! in the spacy installation command if you are working in Google Colab.


#Importation of Modules
#A user-defined function can depend on modules imported prior to where it is defined.

import nltk
nltk.download('popular')
nltk.download('tagsets')


import spacy
from spacy import displacy
from collections import Counter
import pandas as pd

#Invocation of the nlp Machine Learning Model

#Download the nlp machine learning model from spacy in the shell:
#Type the into a commandline the following statement, preceding it by ! only in GoogleColab:
#python -m spacy download zh_core_web_md 

#Load the nlp machine learning model and harbor it in the variable identifier nlp.

nlp = spacy.load('zh_core_web_md')


import re

#File Input/Output

import sys

#-----------statement in the commandlines that runs this program---------------
#python compartmentalization_and_word_tokenization.py ~/sample_output.txt
#------------------------------------------------------------------------------

#file1 = open(sys.argv[1],'r+', encoding = 'utf-8')


def compartmentalization_and_word_tokenization_1(sentence):
  """
Analyzing a single sentence, this function detects the code-switching points,     compartmentalizes the sentence into entirely Mandarin fragments and entirely English fragments, word-tokenizes each monolingual fragment, and converts each token to a token-tag tuple.
  """
  #reference string: sentence
  Mand_Eng_switches = re.findall(r'[^a-zA-Z]\s\b[a-zA-Z]+\b',sentence)
  #return Mand_Eng_switches
  #a non-alphabetic character followed by a sequence of alphabetic characters
  Eng_Mand_switches = re.findall(r'\b[a-zA-Z]+\b\s[^a-zA-Z]',sentence)
  #a sequence of alphabetic characters followed by a non-alphabetic character
  ###Insert a comma at each switching point, so initialize a list of indices of positions where commas will be inserted.
  comma_indices = []
  ##Recover the final-position index of a Mandarin word preceding the switching point. 
  for item in Mand_Eng_switches:
    var1 = item
    #m_a = re.search(r'[^a-zA-Z]\s',item)
    #Mandarin_word = m_a.group()
    #len(Mandarin_word) would result in 2
    m_1 = re.search(rf'{var1}',sentence)
    position_of_matched_sequence = m_1.span()
    comma_index_1 = position_of_matched_sequence[0]+2-1
    comma_indices.append(comma_index_1)
  ##Recover the final-position index of an English word preceding the switching point.
  for item in Eng_Mand_switches:
    var2 = item
    m_b = re.search(r'[a-zA-Z]+\s',item)
    English_word = m_b.group()
    m_2 = re.search(rf'{var2}',sentence)
    position_of_matched_sequence = m_2.span()
    comma_index_2 = position_of_matched_sequence[0]+len(English_word)-1
    comma_indices.append(comma_index_2)
    #Attempt to keep the strings the same length by replacing a single space with a       single comma.
  for item in comma_indices:
    p = int(item)
    sentence = sentence[:p]+','+sentence[p+1:]
  compartmentalized_sentence = sentence.split(",")
  #POS-tag the words of each monolingual fragment 
  comp_w_t_sent = []
  j=0
  while j < len(compartmentalized_sentence):
    m_3 = re.search(r'[a-z]',compartmentalized_sentence[j])
    if m_3 == None: #None, not NONE, is the correct reserved term.
        #word tokenize the string titled compartmentalized_sentence[j] with spaCy
      #If the monolingual fragment is entirely Mandarin
        w_t_str = nlp(compartmentalized_sentence[j])
        w_t_str = list(w_t_str)
        for i in range(len(w_t_str)): #Guarantee that elements of w_t_str are strings.
          w_t_str[i] = str(w_t_str[i])
        comp_w_t_sent.append(w_t_str)
        j+=1
    if type(m_3) == re.Match:
      #If the monolingual fragment is entirely English
         #word tokenize the string titled compartmentalized_sentence[j] with nltk
        w_t_str = nltk.word_tokenize(compartmentalized_sentence[j])
        comp_w_t_sent.append(w_t_str)
        #comp_w_t_sent stands for compartmentalized, word-tokenized sentence
        j+=1
  #return comp_w_t_sent

#A SHORTCOMING OF THE FUNCTION compartmentalization_and_word_tokenization_1

#Mand_Eng switches ['个 chocolate', '个 chocolate']
#The search function's match option will only carry search information for the first occurrence of '个 chocolate', so only the first boundary marked by '个 chocolate' gets divided. 


#print(compartmentalization_and_word_tokenization_1('你 要 那 个 chocolate 你 刚 才 吃 的 那 个 chocolate'))

  
  ##Ascertainment of the formula for the index of comma insertion in an example
  #search_string = '你 要 那 个 chocolate 你 刚 才 吃 的 那 个 chocolate'
  #search_string[5:15] extracts the substring 'chocolate 你'
  #position_of_matched_sequence will store (5,15), as the first tuple component is   the initial-position index while the second tuple component is one greater than the final-position index.
  #len(m_b) will output 10.
  #We seek to insert a comma at index 14.
  #comma_index = position_of_matched_sequence[0]+len(m_b)-1=5+10-1 = 14
      
      #comma_index_2 = position_of_matched_sequence[0]+len(English_word)-1


def compartmentalization_and_word_tokenization_2(sentence):
  """
Analyzing a single sentence, this function detects the code-switching points,     compartmentalizes the sentence into entirely Mandarin fragments and entirely English fragments, word-tokenizes each monolingual fragment, and converts each token to a token-tag tuple. This function mangages the case of identical Mandarin-to-English code-switching points in the same string, such as the repetition of "个 chocolate" in '你 要 那 个 chocolate 你 刚 才 吃 的 那 个 chocolate.' We enhanced this function to handle identical English-to-Mandarin code-switching points if time permits. 
  """
  #reference string: sentence
  Mand_Eng_switches = re.findall(r'[^a-zA-Z]\s\b[a-zA-Z]+\b',sentence)
  #return Mand_Eng_switches
  #a non-alphabetic character followed by a sequence of alphabetic characters
  Eng_Mand_switches = re.findall(r'\b[a-zA-Z]+\b\s[^a-zA-Z]',sentence)
  #a sequence of alphabetic characters followed by a non-alphabetic character
  ###Insert a comma at each switching point, so initialize a list of indices of positions where commas will be inserted.
  comma_indices = []
  ##Recover the final-position index of a Mandarin word preceding the switching point.
  
  if len(Mand_Eng_switches) == 1:
    var1 = Mand_Eng_switches[0]
    m_1 = re.search(rf'{var1}',sentence)
    position_of_matched_sequence = m_1.span()
    comma_index_1 = position_of_matched_sequence[0]+2-1
    comma_indices.append(comma_index_1)
  else: # Handle identical Mandarin-to-English code-switching points in the same sentence.
    sentence_new = sentence[:] #clone the string, so as to not modify the original
    for i in range(len(Mand_Eng_switches)):
      var1 = Mand_Eng_switches[i]
      #m_a = re.search(r'[^a-zA-Z]\s',item)
      #Mandarin_word = m_a.group()
      #len(Mandarin_word) would result in 2
      #Save the position of the code-switching point to a list.
      if i == 0:
        m_2 = re.search(rf'{var1}',sentence_new)
        position_of_matched_sequence = m_2.span()
        comma_index_2 = position_of_matched_sequence[0]+2-1
        comma_indices.append(comma_index_2)
      if i >= 1:
        m_2 = re.search(rf'{var1}',sentence_new)
        #return sentence_new
        position_of_matched_sequence = m_2.span()
        comma_index_2 = len(sentence_new_comp)+position_of_matched_sequence[0]+2-1 #Add the exact length of complementary string because the character count of the complementary substring equals the number by which the index of position_of_matched_sequence[0]+2-1 is offset.
        comma_indices.append(comma_index_2)
      pstn = int(position_of_matched_sequence[0])
      #curtail the part of the sentence before the switching point
      sentence_new = sentence_new[pstn+1:]
      #Get the complementary string or the portion of the original sentence not in 
      #the new sentence.
      sentence_new_comp = sentence[:pstn+1]
  #return comma_indices
  ##Recover the final-position index of an English word preceding the switching point.
  if len(Eng_Mand_switches) == 1:
    for item in Eng_Mand_switches:
      var3 = item
      m_b = re.search(r'[a-zA-Z]+\s',item)
      English_word = m_b.group()
      m_3 = re.search(rf'{var3}',sentence)
      position_of_matched_sequence = m_3.span()
      comma_index_3 = position_of_matched_sequence[0]+len(English_word)-1
      comma_indices.append(comma_index_3)
    #Attempt to keep the strings the same length by replacing a single space with a       single comma.
  else: #Handle identical English-to-Mandarin code-switching points in the same sentence.
    sentence_new_1 = sentence[:] #clone the string, so as to not modify the original
    #Handle identical English-to-Mandarin code-switching points in the same sentence.
    sentence_new_1 = sentence[:]

    #Scour the sentence for all occurrences of a search pattern comprised of an English word, a space, and a Mandarin word.

    #reference string: sentence

    match_object = re.findall(r'\b[a-zA-Z]+\b\s[^a-zA-Z]',sentence)

    if len(match_object) >= 1:
      for i in range(len(match_object)):
        if i == 0:
          #Search for English word in match_object[i] (i.e., the pair of an English and Mandarin word straddling the code-switching point).
          m = re.search(r'^[a-zA-Z]+\b', match_object[i])
          Eng_word = m.group()
          #print(Eng_word) correct
          #Search for match_object[i] in the original sentence.
          m_a = re.search(match_object[i],sentence)
          indices_of_code_switching_pair = m_a.span()
          #Extract the posterior portion of the sentence, and let this override the value of sentence_new_1.
          c_s_point = indices_of_code_switching_pair[0]+len(Eng_word) #c_s_point abbreviates code-switching point
          sentence_new_1 = sentence_new_1[c_s_point+1:]
          #print(f"portion posterior to code-switching point:{sentence_new_1}")
        if i >= 1:
          m = re.search(r'^[a-zA-Z]+\b', match_object[i])
          Eng_word = m.group()
          #Search for match_object[i] in the portion posterior to the code-switching point.
          m_b = re.search(match_object[i],sentence_new_1)
          indices_of_code_switching_pair_post = m_b.span() #indices with respect to the posterior portion
          if i == 1:
            indices_of_code_switching_pair = tuple((s+len(sentence_new_1_comp) for s in indices_of_code_switching_pair_post))
          if i > 1: #I do not understand the reason for the -1 adjustment but figured it out by trial and error.
            indices_of_code_switching_pair = tuple((s+len(sentence_new_1_comp)-1 for s in indices_of_code_switching_pair_post))

          #Now we have the indices with respect to original sentence in the tuple output from tuple comprehension.
          c_s_point = indices_of_code_switching_pair[0]+len(Eng_word)
          sentence_new_1 = sentence_new_1[indices_of_code_switching_pair_post[0]+len(Eng_word):] #string from c_s_point with respect to the the posterior portion
          #print(f"portion posterior to code-switching point:{sentence_new_1}")
        sentence_new_1_comp = sentence[:c_s_point+1]
        comma_indices.append(c_s_point)   
#-----------------
  for item in comma_indices:
      p = int(item)
      sentence = sentence[:p]+','+sentence[p+1:]
  compartmentalized_sentence = sentence.split(",")
  #POS-tag the words of each monolingual fragment 
  comp_w_t_sent = []
  j=0
  while j < len(compartmentalized_sentence):
    m_5 = re.search(r'[a-z]',compartmentalized_sentence[j])
    if m_5 == None: #None, not NONE, is the correct reserved term.
        #word tokenize the string titled compartmentalized_sentence[j] with spaCy
      #If the monolingual fragment is entirely Mandarin
        w_t_str = nlp(compartmentalized_sentence[j])
        w_t_str = list(w_t_str)
        for i in range(len(w_t_str)): #Guarantee that elements of w_t_str are strings.
          w_t_str[i] = str(w_t_str[i])
        comp_w_t_sent.append(w_t_str)
        j+=1
    if type(m_5) == re.Match:
      #If the monolingual fragment is entirely English
         #word tokenize the string titled compartmentalized_sentence[j] with nltk
        w_t_str = nltk.word_tokenize(compartmentalized_sentence[j])
        comp_w_t_sent.append(w_t_str)
        #comp_w_t_sent stands for compartmentalized, word-tokenized sentence
        j+=1
  return comp_w_t_sent

#print(compartmentalization_and_word_tokenization_2('你 要 那 个 chocolate 你 刚 才 吃 的 那 个 chocolate'))

print(compartmentalization_and_word_tokenization_2('你 要 那 个 chocolate 你 刚 才 吃 的 那 个 chocolate 你'))
print(compartmentalization_and_word_tokenization_2('我 是 从 camp 那 边 拿 来 的 自 从 mark 那 时 拿 来 了 之 后'))


