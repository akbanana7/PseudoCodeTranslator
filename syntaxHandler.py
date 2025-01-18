# Imports
import re


def variableAssignment(line): # For variable Assignment
    print(f"Assigning variable with line -- {line}")
    # Searches for identifier and toAssign
    varBle = re.search(r"^\S+",line) # Searches for first word (variable identifier) in string
    toAsgn = re.search(r"<-\s*(.+)",line) # Searches and returns: <- toAssign
    try:
        varBle = varBle.group() # Captures just the strings
        toAsgn = toAsgn.group() # Captures just the strings
    except:
        errorHandler(line,"noValidVar")


    toAsgn = toAsgn.strip("<-") # Strips "<-" from the toAssign
    toAsgn = toAsgn.strip() # Strips all whitespace

    if re.match(r"INPUT", toAsgn):
        print("Input found")
        with open(filePath, "a") as file:
            if lineCount != 1:
                file.write(f"\n{varBle} = input()")
            else:
                file.write(f"{varBle} = input()")


    else:
        with open(filePath, "a") as file:
            if lineCount != 1:
                file.write(f"\n{varBle} = {toAsgn}")
            else:
                file.write(f"{varBle} = {toAsgn}")




def output(line): # For print statement writing
    print(f"Outputting object with line -- {line}")
    toPrint = re.search(r"^(?:OUTPUT\s*)?(.*)",line)
    toPrint = toPrint.group(1) # Converts to string

    with open(filePath,"a") as file:
        if lineCount != 1:
            file.write(f"\nprint({toPrint})")
        else:
            file.write(f"print({toPrint})")



def importFile(parsedFile,filePth): # Function to bring in parsed file of type LIST to syntaxHandler
    global userFile
    global filePath
    userFile = parsedFile
    filePath = filePth
    prepareFile()

def prepareFile(): # Function for writing to filePath (python file to be executed)
    print("preparing file")
    with open(filePath, "w"): # Wipes the file. Quick workaround lol
        pass
    global lineCount
    for index, i in enumerate(userFile, start=1):
        lineCount = index
        if re.match(r"^\s", i):
            print("Whitespace -- Assuming indentation")
        elif re.match(r"^OUTPUT", i):
            output(i)
        elif re.search(r"^[^\s]", i):
            variableAssignment(i)
        else:
            print("Blank Space")








def errorHandler(line, error_type, error): # Function for error handling
    if error_type == "lineType":
        try:
            raise SyntaxError(f"Callback on line: {line}    SYNTAX ERROR -- LINE TYPE -- EXPECTED LINE OF TYPE (STR) RECEIVED -- {type(line)}")
        except SyntaxError as e:
            print(e)
    elif error_type == "parseError":
        try:
            raise SyntaxError(f"Callback on method {line}   PARSE ERROR -- EXPECTED DIRECTORY OF TYPE (STR) TO .PSC -- GOT NULL")
        except SyntaxError as e:
            print(e)
    elif error_type == "noValidVar":
        try:
            raise SyntaxError(f"Callback on line {line}    SYNTAX ERROR -- NO VALID VAR -- EXPECTED '<-' AFTER VAR IDENTIFIER DECLARATION -- GOT NULL")
        except SyntaxError as e:
            print(e)
    elif error_type == "errorExecuting":
        try:
            raise SyntaxError(f"Callback on file {line}    EXEC ERROR -- PYTHON EXEPTION -- EXPECTED FILE EXECUTION -- GOT '{error}'")
        except SyntaxError as e:
            print(e)
    exit()