# f=open("sample.txt","w+")
# f.write("nani\n")
# f.write("sai\n")
# f.write("ravi\n")
# print(f.read())




# f=open("sample.txt","r")
# content=f.read()
# f.close()

# f=open("destination.txt","w")
# f.write(content)

# print("file copy succesfully")


#Word Count – Read a text file and count how many times each word occurs

# with open("nani.txt","r") as file:
#     text=file.read()
#     # file.seek(0)
#     # file.write("Python is great. Python is easy to learn, and Python is powerful.")

# words=text.lower().split()

# words_count={}

# for word in words:
#     word=word.strip(",./:;><|@$*&*")
#     if word in words_count:
#         words_count[word]+=1
#     else:
#         words_count[word]=1

# for word , count in words_count.items():
#     print(f"{word}:{count}")

with open("nani.txt", "r") as file:
    text = file.read()

words = text.lower().split()
words_count = {}

for word in words:
    word = word.strip(",./:;><|@$*&*")
    #words_count[word]=word_count.get(word,0)+1
    if word in words_count:
        words_count[word]+=1
    else:
        words_count[word]=1
# Now overwrite the file with the word counts
with open("nani.txt", "w") as file:
    for word, count in words_count.items():
        file.write(f"{word}:{count}\n")

