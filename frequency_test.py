import re
import string


def word_frequency(filename):
  #The dictionary that will hold the words and counts
  d = {}
  
  #Open file and read its contents
  with open(filename, 'r') as file:
    text = file.read()
  
  #Remove punctuation (except apostrophies) and convert tolowercase 
  text = re.sub(r'[' + string.punctuation.replace("'", "") + r"\d]|'", "", text).lower()
  
  #Split the text into words
  words = text.split()
  
  #Count the frequency of each word.
  for word in words:
    d[word] = d.get(word, 0) + 1

  return d

def main():
  filename = '/Users/christopherblystone/Documents/turing.txt'
  word_frequencies = word_frequency(filename)
  print(word_frequencies)
  for word, frequency in word_frequencies.items():
    print(f"{word}: {frequency}")
  print("End of Main")
  
if __name__ == '__main__':
  main()
  
