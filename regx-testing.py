import string

def frequency_count(filename):
  d = {}
  
  remove_chars = str.maketrans('', '', string.punctuation + string.whitespace + "'-")
  
  with open(filename, 'r') as file:
    text = file.read()
    
  cleaned_text = text.translate(remove_chars)
  
  words = cleaned_text.split()
  
  for word in words:
    d[word] = d.get(word, 0) + 1
  
  return d

  
def main():
  filename = '/Users/christopherblystone/Documents/turing.txt'
  word_frequency = frequency_count(filename)
  print(word_frequency)
  
if __name__ == '__main__':
  main()
  
  