def remove_whitespaces(filename):
    with open(filename, "r") as file:
        contents = file.read()
        contents = contents.replace(" ", "")    #Normal whitespace
        #contents = contents.replace("\n", "")  #End of line whitespace
        contents = contents.replace("\t", "")   #Tab whitespace

    with open(filename, "w") as file:
        file.write(contents)

filename = "IOmap.txt"
remove_whitespaces(filename)
