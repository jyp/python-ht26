def file_lines(h):
  while True:
    line = h.readline()
    if line == '':
      return
    yield line

def load_dictionary(filename,source,target):
  with open(filename) as h:
      d = {}
      for line in file_lines(h):
        line = line.rstrip()
        if line != '' and line[0] != '#':
        # if line[0] != '#' and line != '': # crash!
            fields = line.split(";")
            words = fields[source]
            words = words.strip()
            words = words.split(",")
            # words: all words in the 2nd field of the line (comma separated)
            for word in words:
                for translation in fields[target].strip().split(","):
                    d.setdefault(word.strip(),[]).append(translation.strip())
  return d

def test_english_to_swedish(word):
    d = load_dictionary('terms.csv',0,1)
    print("English translations of ", word, "are", d[word])

def test_swedish_to_english(word):
    d = load_dictionary('terms.csv',1,0)
    print("Swedish translations of ", word, "are", d[word])

test_swedish_to_english("program")
test_english_to_swedish("RAM")
# print(d["arbetsminne , primärminne , RAM"])
