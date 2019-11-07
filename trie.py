import os
import json
from itertools import islice
import tkinter as tk


def file_len(fname):
    count = 0
    for line in open(fname).readlines(): count += 1
    return count

#Trie node class
class TrieNode:

    # Trie node class
    def __init__(self):
        self.children = [None] * 26

        # isEndOfWord is True if node represent the end of the word
        self.ID = -1

# Trie class
class Trie:
  # init Trie class
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()


    def _indexing(self, ch):
        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case
        ch=ch.lower()
        return ord(ch) - ord('a')


    def insert(self, key,mean,id):
        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        Cur = self.root
        length = len(key)
        for level in range(length):
            index = self._indexing(key[level])

            # if current character is not present
            if not Cur.children[index]:
                Cur.children[index] = self.getNode()
            Cur = Cur.children[index]

        # mark last node as leaf
        Cur.ID = id
        if Cur.ID !=-1:
            with open('meaning_alpha.txt', 'a') as f:
                f.writelines(mean +'\n')
            with open('words_alpha.txt','a') as f1:
                f1.writelines(key + ',')

    def _insert_non_writeFie(self, key,id):
        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        Cur = self.root
        length = len(key)
        for level in range(length):
            index = self._indexing(key[level])

            # if current character is not present
            if not Cur.children[index]:
                Cur.children[index] = self.getNode()
            Cur = Cur.children[index]

        # mark last node as leaf
        Cur.ID = id


    def search(self, key):
        # Search key in the trie
        # Returns true if key presents
        # in trie, else false
        Cur = self.root

        if key[-2:] == 'ww':
            Cur.ID = -1
            return Cur.ID

        length = len(key)
        for level in range(length):
            index = self._indexing(key[level])
            if not Cur.children[index]:
                return False
            Cur = Cur.children[index]
        return Cur.ID



if __name__ == '__main__':

    _meaning_file ='meaning_alpha.txt'
    _key_file = 'words_alpha.txt'

    # Initial Trie
    trie = Trie()

    # Counting number of word
    id = file_len(_meaning_file)
    I = id

    #Reload the Trie from the file
    with open(_key_file, 'r') as exist_File:
        i = 0
        _cur = exist_File.read()
        l_word = _cur.split(',')
        print(l_word)
        for word in l_word:
            if word == '':
                continue
            trie._insert_non_writeFie(word,i)
            i = i + 1

### Open the meaning file
    file = open(_meaning_file, 'r')
    f = file.readlines()


##################################
#### UI PART #####################
    HEIGHT = 1600
    WIDTH = 900
    def fomat_search_output(search_result):
        return search_result

    def serchButton(entry):
        s = trie.search(entry)
        print(s)
        if s == -1 or s == False:
            search_result = u'Từ này không tồn tại'
        elif s==0:
            search_result = f[s]
        else:
            search_result = f[s]

        bot_label['text'] = fomat_search_output(search_result)


    root = tk.Tk()
    root.title('Dictionary Search mode')

    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    background_image = tk.PhotoImage(file='zoro.png')
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1,relheight=1)

    ##NOTE Frame
    note_frame = tk.Frame(root)
    note_frame.place(relx=0.7, rely=0.01,relwidth=0.3, relheight=0.03)

    note_label = tk.Label(note_frame,bg='white',text=u'Lưu ý: Từ điển chỉ tra được từ không dấu')
    note_label.place(relwidth=1, relheight=1)

    #####
    frame = tk.Frame(root, bg='#690408')
    frame.place(relx=0.2, rely=0.1,relwidth=0.6, relheight=0.08)

    entry = tk.Entry(frame, bg='white')
    entry.place(relx=0.01, rely=0.15, relwidth=0.75, relheight=0.7)
    entry.config(font=("Courier", 22))

    #seach button
    button = tk.Button(frame, text='Search', bg='white',command=lambda : serchButton(entry.get()))
    button.place(relx=0.8,rely=0.15,relwidth=0.19, relheight=0.7)

    bot_frame = tk.Frame(root, bg='#690408',bd=5)
    bot_frame.place(relx=0.2,rely=0.25, relwidth=0.6, relheight= 0.65)

    bot_label = tk.Label(bot_frame, bg='white',font=70)
    bot_label.place(relwidth=1, relheight=1)
    bot_label.config(font=("Courier", 22))



    root.mainloop()

