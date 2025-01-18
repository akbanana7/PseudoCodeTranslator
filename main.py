from verifier import parse, verify
from syntaxHandler import importFile, errorHandler
# Settings below
defFileName = "pseudo.py"



if __name__ == "__main__":
    filename = input("Input the file directory/name: ")
    parsedFile = parse(filename)
    verify(parsedFile)
    importFile(parsedFile,defFileName)

    # Opening file then executing
    with open(defFileName) as execute:
        try:
            exec(execute.read())
        except SyntaxError as e:
            errorHandler(filename,"errorExecuting",e)
            exit()