
# Outline of Mandarin-English Code-Switching Final Project

## Introduction
- In this project, we will be analyzing two datasets of Mandarin-English code-switching data from the SEAME dataset , one of them are majority-English and the other one are majority-Mandarin. We will be analyzing the syllables of words in the dataset, the part of speeches of the dataset, the phrases and sentence structures that occurs in the dataset. We will also be identifying word boundaries, sentence boundaries, code-switching boundaries in this dataset, as well as calculating the syllable length of each English words in the dataset. These data will be collected in order to answer a list of questions provided below.

## Questions to investigate and Hypotheses

At what part of speeches (a.k.a., lexical category) does Mandarin-English code-switching usually occurs?
- Code-switching occurs equally frequently as nouns, adjectives, and verbs.
- No matter if the switched word starts a Mandarin fragment, or starts an English fragment, the result will be the same.

## Background


We have only remotely, tangentially related studies and Max's experience as a Mandarin-English code-switcher to hint at any outcome of this experiment.

- Picture Naming Experiment
	- In the article titled “A Comparison of Noun and Verb Retrieval”, 21 Mandarin-English bilinguals native in only Mandarin and 21 English monolinguals recalled nouns in response to sketches of objects and recalled verbs in response to sketches of actions. 
	- Each noun or verb picture naming task was rated 0 for inaccurate and 1 for accurate, plus the retrieval time for each task was also logged.
	- Mandarin-English bilinguals scored higher for verbs than nouns in terms of retrieval rate, especially in their non-native language, but higher 
	  for nouns  in terms of accuracy.
	  
Max witnesses himself code-switching on adjectives and nouns more than verbs. At variance with Max's observations, a picture naming experiment concluded that Mandarin speakers have more immediate access to verbs than nouns. Because tensions arise between Max's experience predicting a higher prevalence of switched adjectives or nouns and ab experiment predicting a higher prevalence of switched verbs, this experiment's hypothesis will be null. We expect the number of switched nouns, switched adjectives, and switched verb to be the same, and we do not anticipate that the language to which these switched words belong influences the results.


## Methods
- ##### Here is the dataset that we will use for the project:
	- SEAME is a Mandarin-English code-switching corpus replete with 192 hours of interview question-facilitated casual conversations. SEAME-dev-set contains two repackaged SEAME-derived test sets of mixed-language speech, one Mandarin-dominated and one Singaporean English-dominated. Keep in mind that SEAME only reflects only code-switching in Mandarin diasporan communities of Singapore and Malaysia. Any unexpected discrepancies between part of speech distribution in SEAME-dev-set and the noun and word retrieval experiment could result from different populations surveyed or different circumstances. The word retrieval in SEAME transpired in conversation unlike how word retrieval in the noun and word retrieval experiment occurred in response to pictures.

## Data Collection:

One Mandarin-dominated test set (dataset1.txt), wherein presumably English is the non-native language, and one English-dominated test set (dataset2.txt), wherein presumably Mandarin is the non-native language, were imported from zengzp0912's repository.
We will manually convert both dataset1.txt and dataset2.txt to a csv with a NumberTag column and a MandEngSpeech column, so they can be processed by the computer easier.
We will read the column titled “sentences” of dataset1.txt and column titled “sentences” of dataset1.txt of dataset2.txt into a single list list_of _sentences.
The Algorithms and Pseudocode expound on the rest of the data curation.

### Algorithms and Pseudocode:
- Here is the algorithm of the project
- This algorithm might be heavily modified later during the project based on needs.

The Analytical Tasks

Preprocessing Step
Read the column titled “sentence” in dataset1.txt as well as in dataset2.txt into a single list_of _sentences.

Code-Switching Boundary Detection , Word Tokenization, and Part of Speech Tagging
Initialize a list titled nlp_processed_sentences to contain all the language-compartmentalized, word tokenized, part of speech-tagged sentences. 
For each index i in range(len(list_of_sentences)), identify all the boundaries or switching points from English to Mandarin and vice-versa. (Note that we are interested in the part of speech of the word following each switching point.) Then compartmentalize each sentence into all-Mandarin word sequences and all-English word sequences by splitting it at language boundaries before you finally tag the part of speech of every all-Mandarin sequence and tag the part of speech of every all-English sequence.

i = 18

19: ‘那 时 候 we’

Insert commas at switching points by regex

19: ‘那 时 候, we’

Split the string at commas into a list of monolingual sequences by specifying “,” as the delimiter, as in  string.split(“,”).

List_of_monolingual_sequences = [‘那 时 候’, ‘we’]

Construct a processed sentence from list_of_monolingual_sequences with list comprehension and spaCy/nltk.

processed_sentence = [[(那, DET), (时 候, NN)], [(we, PRON)]]

processed_sentence to the list nlp_processed_sentences.

i = 100

101: '诶 就 是 就 是 old 就 是 那 种 middle age 那 种 middle age 的 啊'

List_of_monolingual_sequences = [‘那 时 候’, ‘we’]

Construct a processed sentence from list_of_monolingual_sequences with list comprehension and spaCy/nltk.

processed_sentence = [[(那, DET), (时 候, NN)], [(we, PRON)]]

processed_sentence = [ [('诶’, X), (‘就’, ADV) (‘是’, PART), (‘就 是’, ADV)], [(‘old’, JJ)], [(‘就’, PRON), (‘是’, VERB), (‘那’, DET), (‘种’, NOUN)], [(‘middle’, JJ),  (‘age’, NN)], [(‘那’, DET), (‘种’, NOUN)], [(‘middle’, JJ),  (‘age’, NN)], [(‘的’,PART), (啊,PART)] ]

Append processed_sentence to the list list nlp_processed_sentences.



Computation of the Number of switched English Nouns, Adjectives, and Verbs and Switched 

Initialize two lists: tagged_switched_Mandarin_words and tagged_switched_English_words

At each transition from English to Mandarin, retrieve the tagged Mandarin word and append it to a list tagged_switched_Mandarin_words.

Tally up the number of adjectives, nouns, and verbs in  tagged_switched_Mandarin_words

At each transition from Mandarin to English, retrieve the tagged English word and append it to a list tagged_switched_English_words.

Tally up the number of adjectives, nouns, and verbs in  tagged_switched_English_words

Create a bar chart or other diagram in excel, colab, etc that can visually illustrate the number of switched words that are adjectives, nouns, and verbs and the number of switched words that are adjectives, nouns, and verbs.
