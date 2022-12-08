f=open("Input.txt","w")
f.write("Hello wwelcome to class\n Welcome\nBye")
f.close()
fin = open('Input.txt','r')
charCount= wordCount = lineCount = 0
for line in fin:
    lineCount += 1
    wordCount += len(line.split())
    charCount += len(line)
print("Line Count = ",lineCount)
print("Word count = ", wordCount)
print("Char Count = ", charCount) 