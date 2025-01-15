from syntaxHandler import errorHandler

def parse(filename):
    print("Parsing file")
    fileArray = []
    try:
        with open(filename, "r") as file:
            for line in file:
                str(line)
                line = line.strip("\n")
                fileArray.append(line)
            print(fileArray)
            return fileArray
    except:
        errorHandler("~~File Parser in VERIFIER.PY~~", "parseError")



def verify(fileArray):
    print("Verifying file")