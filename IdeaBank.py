IdeaList = []
for i in range(5):
    IdeaList.append(input("Mi az uj otleted? :"))
IdeaFile = open("Ideas.txt", "a",)
for idea in IdeaList:
    IdeaFile.write(idea)
IdeaFile.close()
IdeaFile = open("Ideas.txt", "r")
TempList = IdeaFile.read
print(len(TempList))