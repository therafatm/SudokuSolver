import re
from subprocess import call

file = open("fiftygrids.sudoku", "r")
filename = None
currentFile = None
output = ""

for line in file:
    if re.match("^Grid.*", line):
        if(currentFile != None):
            currentFile.close()
            call(["javac", "Sudoku.java"])
            call(["java", "Sudoku", filename, filename+"_dimacs.txt"])
            call(["minisat", filename+"_dimacs.txt", filename+"_satout.txt"])
            call(["python3", "sat2sud.py", filename+"_satout.txt", filename+"_solvedBoard.txt"])
        filename = line
        filename = filename.strip().replace(" ", "") + ".txt"
        currentFile = open(filename, "w")
    else:
        currentFile.write(line)

currentFile.close()
file.close()