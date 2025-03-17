#WordCount.py
#Name: Jessica Pusher
#Date: 3.16.25
#Assignment: WordCount.py

def main():
  File = input("Enter a File Name: ") # tested with file names fish.txt and gettysberg.txt
  textFile = open(File, 'r')
  lineCount = 0
  wordCount = 0
  letterCount = 0
  
  for line in textFile:
    lineCount = lineCount + 1
    words = line.split()
    for w in words:
      wordCount = wordCount + 1
      letterCount = letterCount + wordCount +len(w) # I included wordcount since the spces between each word are also technically a character in the text.
        
    
  print("Lines: ", lineCount)
  print("Words: ", wordCount)
  print("Characters: ", letterCount)
  

if __name__ == '__main__':
  main()
