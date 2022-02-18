We uploaded the entirety SEAME-dev-set to this data folder. SEAME-dev-set consists of two test sets (one Singaporean English-dominated and one Mandarin-dominated) from the SEAME Mandarin-English code-switching corupus. "dataset1.txt" is our Singaporean English-dominated test set while "dataset2.txt" is out Mandarin-dominated test set.
The data collection and curation process is as follows:
One Mandarin-dominated test set (dataset1.txt), wherein presumably English is the non-native language, and one English-dominated test set (dataset2.txt), wherein presumably Mandarin is the non-native language, were imported from zengzp0912's repository. 
We will convert both dataset1.txt and dataset2.txt to a csv with a NumberTag column and a MandEngSpeech column.
We will read each MandEngSpeech column into a list, titling the list mandEngSpeech for dataset1.txt and MandengSpeech for dataset2.txt.
We will filter out the English fillers (e.g., "um", "eh"); interjections or abrupt sentence-initial words like "ah," "ha", and "hey"; and proper nouns (e.g., Backstreet Boys) from each string in each list by iterating through lists of fillers, interjections, and proper nouns.
If Max is knowlegdeable of fillers, interjections, and proper nouns in Mandarin, then we will filter out those from the both lists of mixed Mandarin-English sentences.


We will initialize lists mandEngSpeech_tokens and MandengSpeech_tokens.

We will import nltk, download popular, and import spacy in order to word tokenize each string, decomposing it into words tokens and punctuation mark tokens.
We will append each tokenized string of mandEngSpeech to mandEngSpeech_tokens and each tokenized string of MandengSpeech to MandengSpeech_tokens.

initialize noun counter
initialize verb counter
for item in mandEngSpeech_tokens
	count the number of nouns in item 
		-> add to noun counter
	count the number of verbs in item
		->add to verb counter
		
print(noun counter)
print(verb counter)

initialize new noun counter
initialize new verb counter
for item in mandEngSpeech_tokens
	count the number of nouns in item 
		-> add to new noun counter
	count the number of verbs in item
		->add to new verb counter
		
print(new noun counter)
print(new verb counter)
