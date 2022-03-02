#This script converts a .txt space-separated dataset into a .txt comma-separated dataset that can tractably be redesignated as a csv.

input_file = 'dataset1_w_o_commas.txt'

with open(input_file,'r',encoding = 'utf-8') as file1:
#Read the file line by line into an interable
  lines = file1.readlines()

#Initialize a string-storing list prior to the for loop.
  L = []
  
  for line in lines:
    #Replace each space between a Tagged token and a code-    switching sentence with a comma.
    revised_line = line.replace(" ", ",", 1)
    #revised_line = revised_line +"\n"
    L.append(revised_line) #Lists are mutable
    file1.close() #Indent file1.close() as well.

output_file = 'dataset1_w_commas.txt'

with open(output_file,'w',encoding = "utf-8") as file2:
  for i in range(len(L)):
    file2.write(L[i])
  
  file2.close() #Do not close the file at the end of the     #first iteration.
  