import re

number_of_English_words(text):
  """
  This function calculates the number of English words in a mixed Mandarin-English      text expressed as a string.
  """
  m = re.findall(r"\b[[abcdefghijklmnopqrstuvwxyz]]+\b",text)
  return len(m)

print(number_of_English_words(test_string))