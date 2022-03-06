import re

def eng_number(annotated_comp_w_t_sent):
  """
Absorbing a part of speech-annotated, language-compartmentalized, and word-tokenized list of lists of tuples as an input, this function totals up the number of switched English fragment-initial nouns, switched English fragment-initial adjectives, and switched English fragment-initial verbs, integrating them into a three-element list output.
  """
  eng_number_values = [0,0,0] #Define all value-storing lists prior to the for loop,   so as to not override them with each iteration of the loop.
  #Eliminate the sentence-initial monolingual fragment, which does not follow a code-switching point.
  annotated_comp_w_t_sent.reverse()
  first_monolingual_segment = annotated_comp_w_t_sent.pop() 
  annotated_comp_w_t_sent.reverse()
  for fragment in annotated_comp_w_t_sent:
    #reference string: fragment[0][0]
    m = re.search(r'[a-zA-Z]',fragment[0][0]) #0th component of 0th tuple in list
    if type(m) == re.Match: #An English first word signals an entirely English fragment.
      #Note: lists are mutable, so list indices can be reallocated new values.
      if  fragment[0][1] == 'NN': #1st component of 0th tuple in list
        eng_number_values[0] = eng_number_values[0]+1
      if  fragment[0][1] == 'JJ': #1st component of 0th tuple in list
        eng_number_values[1] = eng_number_values[0]+1
      if  fragment[0][1] == 'VB' or fragment[0][1] == 'VBP' or fragment[0][1] == 'VBZ' or fragment[0][1] == 'VBN' or fragment[0][1] == 'VBD': #1st component of 0th tuple in list
        eng_number_values[2] = eng_number_values[0]+1
    else: #A Mandarin first word signals an entirely Mandarin fragment.
      pass
  return eng_number_values

def chin_number(annotated_comp_w_t_sent):
  """
Absorbing a part of speech-annotated, language-compartmentalized, and word-tokenized list of lists of tuples as an input, this function totals up the number of switched English fragment-initial nouns, switched English fragment-initial adjectives, and switched English fragment-initial verbs, integrating them into a three-element list output.
  """
  #Eliminate the sentence-initial monolingual fragment, which does not follow a code-switching point.
  annotated_comp_w_t_sent.reverse()
  first_monolingual_segment = annotated_comp_w_t_sent.pop() 
  annotated_comp_w_t_sent.reverse()
  chin_number_values = [0,0,0] #Define all value-storing lists prior to the for loop, so as to not override them with each iteration of the loop.
  for fragment in annotated_comp_w_t_sent:
    #reference string: fragment[0]
    m = re.search(r'[a-zA-Z]',fragment[0][0])
    if m == None: #A Mandarin first word signals an entirely Mandarin fragment.
      #Note: lists are mutable, so list indices can be reallocated new values.
      if  fragment[0][1] == 'NOUN':
        chin_number_values[0]+=1
      if  fragment[0][1] == 'ADJ':
        chin_number_values[1]+=1
      if  fragment[0][1] == 'VERB':
        chin_number_values[2]+=1
    else: #An English first word signals an entirely English fragment.
      pass
  return chin_number_values





print(eng_number([[('你', 'PRON'), ('要', 'VERB'), ('那', 'DET'), ('个', 'NUM')], [('chocolate', 'NN')], [('你', 'PRON'), ('刚', 'ADV'), ('才', 'ADV'), ('吃', 'VERB'), ('的', 'PART'), ('那', 'DET'), ('个', 'NUM')], [('chocolate', 'NN')], [('你', 'PRON')]]))

print(chin_number([[('你', 'PRON'), ('要', 'VERB'), ('那', 'DET'), ('个', 'NUM')], [('chocolate', 'NN')], [('你', 'PRON'), ('刚', 'ADV'), ('才', 'ADV'), ('吃', 'VERB'), ('的', 'PART'), ('那', 'DET'), ('个', 'NUM')], [('chocolate', 'NN')], [('你', 'PRON')]]))

print(eng_number([[('我', 'PRON'), ('是', 'VERB'), ('从', 'ADP')], [('camp', 'NN')], [('那', 'DET'), ('边', 'ADV'), ('拿', 'VERB'), ('来', 'VERB'), ('的', 'PART'), ('自', 'ADV'), ('从', 'VERB')], [('mark', 'NN')], [('那', 'ADV'), ('时', 'PART'), ('拿', 'VERB'), ('来', 'VERB'), ('了', 'PART'), ('之', 'PART'), ('后', 'NOUN')]]))

print(chin_number([[('我', 'PRON'), ('是', 'VERB'), ('从', 'ADP')], [('camp', 'NN')], [('那', 'DET'), ('边', 'ADV'), ('拿', 'VERB'), ('来', 'VERB'), ('的', 'PART'), ('自', 'ADV'), ('从', 'VERB')], [('mark', 'NN')], [('那', 'ADV'), ('时', 'PART'), ('拿', 'VERB'), ('来', 'VERB'), ('了', 'PART'), ('之', 'PART'), ('后', 'NOUN')]]))



annotated_comp_w_t_sent = [[('我', 'PRON'), ('是', 'VERB'), ('从', 'ADP')], [('camp', 'NN')], [('那', 'DET'), ('边', 'ADV'), ('拿', 'VERB'), ('来', 'VERB'), ('的', 'PART'), ('自', 'ADV'), ('从', 'VERB')], [('mark', 'NN')], [('那', 'ADV'), ('时', 'PART'), ('拿', 'VERB'), ('来', 'VERB'), ('了', 'PART'), ('之', 'PART'), ('后', 'NOUN')]]
