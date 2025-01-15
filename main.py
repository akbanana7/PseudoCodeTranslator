from verifier import parse, verify
from syntaxHandler import importFile
# Settings below
defFileName = "pseudo.py"



if __name__ == "__main__":
    filename = input("Input the file directory/name: ")
    parsedFile = parse(filename)
    verify(parsedFile)
    importFile(parsedFile,defFileName)