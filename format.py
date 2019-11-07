input_file = open('words_alpha.txt','r')
out_file = open('word1.txt','w')
l_word = []

while True:
    s = input_file.readline()
    s = s.rstrip('\n')
    if not s:
        break
    print(s)
    l_word.append(s)

for word in l_word:
    out_file.write(word + ',')
