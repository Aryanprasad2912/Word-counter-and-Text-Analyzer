import string
text=input("Enter the text(or type File):")
if text.strip().upper()=="FILE":
  filename = input("Enter file name: ")
  try:
    with open(filename,"r") as file:
       text = file.read()
       print("File content:",text)
  except FileNotFoundError:
    print(f"File'{filename}'not found.")
    text=None
    if text is None:
      pass
elif not text.strip():
  print("No text to analyse")
else:
  original_text = text.strip()
text=text.lower()
text= text.translate(str.maketrans("","",string.punctuation))
words=text.split()

frequency={}
for word in words:
   frequency[word]= frequency.get(word,0)+1


unique_words=set(words)

sentence=sum(original_text.count(mark) for mark in ".!?")
if sentence==0 and words:
   sentence=1

try:
        option = input("Menu option (2 for frequency): ").strip()
except EOFError:
        option = ""
        if option == "2":
          top_word = sorted(
            frequency.items(),
            key=lambda item: (-item[1], item[0])
        )
        result=[]
        for word, count in top_word[:2]:
         result.append(word + ": " + str(count))
    
         print(" Top words:" + " |".join(result) )
         print("Unique words:  " + str(len(unique_words)) + " (" +
      ",".join(sorted(unique_words)) + ")")

else:
    print("Words:", len(words))
    print("Characters:", len(original_text))
    print("Sentences:", sentence)
    print("Unique words:", len(unique_words))

    print("Word frequency:")
    for word, count in sorted(
        frequency.items(), key=lambda item: item[1], reverse=True
    ):
        print(word, ":", count)







