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
            with open(_meaning_file, 'a') as f:
                f.writelines(mean +'\n')
            with open(_key_file,'a') as f1:
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

        if key[-2:]== 'ww':
            Cur.ID = -1
            return Cur.ID

        length = len(key)
        for level in range(length):
            index = self._indexing(key[level])
            if not Cur.children[index]:
                return False
            Cur = Cur.children[index]
        return Cur.ID

    def delete(self, key):
        exist_File = open(_key_file,'r')
        _cur = exist_File.read()
        l_word = _cur.split(',')
        print(l_word)
        i = l_word.index(key)
        l_word[i] = l_word[i] +'ww'
        exist_File.close()

        newfile = open(_key_file,'w')
        for word in l_word:
            newfile.writelines(word + ',')


if __name__ == '__main__':

    _meaning_file ='meaning_alpha.txt'
    _key_file = 'words_alpha.txt'

    #initial Trie
    trie = Trie()
    #Counting number of word
    id = file_len(_meaning_file)
    I = id

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


##################################
#### UI PART #####################
    HEIGHT = 1600
    WIDTH = 900
    def fomat_insert_output():
        return 'Insert successfully'

    def fomat_delete_output():
        return 'Delete successfully'

    def insertButton(entry_word,entry_mean,I):
        if entry_word == '':
            return
        trie.insert(entry_word, entry_mean, I)
        I = I + 1

        bot_label['text'] = fomat_insert_output()

    def deleteButton(entry_word_delete):
        if entry_word_delete == '':
            return
        trie.delete(entry_word_delete)

        bot_label['text'] = fomat_delete_output()

    root = tk.Tk()
    root.title('Dictionary Insert and Delete mode')

    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    background_image = tk.PhotoImage(file='zoro.png')
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1,relheight=1)

    ##NOTE Frame

    note_frame = tk.Frame(root)
    note_frame.place(relx=0.7, rely=0.01, relwidth=0.3, relheight=0.03)

    note_label = tk.Label(note_frame, bg='white', text=u'Lưu ý: Từ điển chỉ thêm được từ không dấu')
    note_label.place(relwidth=1, relheight=1)

    ###############
    # TOP FRAME
    frame = tk.Frame(root, bg='#690408')
    frame.place(relx=0.15, rely=0.1,relwidth=0.7, relheight=0.2)

    label_word = tk.Label(frame, text= u'Từ muốn thêm:')
    label_word.place(relx=0.02,rely=0.15,relwidth=0.165,relheight=0.3)

    label_mean = tk.Label(frame, text='Nghĩa:')
    label_mean.place(relx=0.02, rely=0.5, relwidth=0.165, relheight=0.3)

    entry_word = tk.Entry(frame, bg='white')
    entry_word.place(relx=0.2, rely=0.15, relwidth=0.56, relheight=0.3)
    entry_word.config(font=("Courier", 22))

    entry_mean = tk.Entry(frame, bg='white')
    entry_mean.place(relx=0.2, rely=0.5, relwidth=0.56, relheight=0.3)
    entry_mean.config(font=("Courier", 22))

    # insert button
    button_insert = tk.Button(frame, text='Insert', bg='white',command=lambda : insertButton(entry_word.get(),entry_mean.get(),I))
    button_insert.place(relx=0.8,rely=0.15,relwidth=0.19, relheight=0.3)

    ##########################
    # MID FRAME
    frame1 = tk.Frame(root, bg='#690408')
    frame1.place(relx=0.15, rely=0.35, relwidth=0.7, relheight=0.1)

    label_delete = tk.Label(frame1, text= u'Từ muốn xóa:')
    label_delete.place(relx=0.02, rely=0.15, relwidth=0.165, relheight=0.7)

    entry_word_delte = tk.Entry(frame1, bg='white')
    entry_word_delte.place(relx=0.2, rely=0.15, relwidth=0.56, relheight=0.7)
    entry_word_delte.config(font=("Courier", 22))

    #delete button
    button_delete = tk.Button(frame1, text='Delete', bg='white',command=lambda : deleteButton(entry_word_delte.get()))
    button_delete.place(relx=0.8,rely=0.15,relwidth=0.19, relheight=0.7)



    ############################
    # BOT FRAME
    bot_frame = tk.Frame(root, bg='#690408',bd=5)
    bot_frame.place(relx=0.15,rely=0.5, relwidth=0.7, relheight= 0.5)

    bot_label = tk.Label(bot_frame, bg='white')
    bot_label.place(relwidth=1, relheight=1)
    bot_label.config(font=("Courier", 22))



    root.mainloop()

