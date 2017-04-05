import re, sys
from subprocess import call

def main(argv):
    if (len(argv) < 1):
        print("Incorrect Args")
        return
    infile = argv[0]
    extended = False
    if (len(argv) == 2 and argv[1] == "extended"):
        extended = True

    file = open(infile, "r")
    currentFile = None
    puzzle = 1
    output = ""

    for line in file:
        if re.match("^Grid.*", line): #handle Euler format
            filename = line
            filename = filename.strip().replace(" ", "")
            currentFile = open(filename +".txt", "w")
            for _ in range(9):
                currentFile.write(file.next())
            currentFile.close()
            extract(filename, extended)
        else:
            filename = infile + "_" + str(puzzle)
            currentFile = open(filename+".txt", "w")
            currentFile.write(line)
            currentFile.close()
            extract(filename, extended)
            puzzle += 1

    file.close()

def extract(filename, extended=False):
    if extended:
        program = "Sud2SatExtended"
    else:
        program = "Sud2sat"
    call(["javac", program + ".java"])
    call(["java", program, filename+".txt", filename+"_dimacs.txt"])
    call(["minisat", filename+"_dimacs.txt", filename+"_satout.txt"])
    call(["python", "sat2sud.py", filename+"_satout.txt", filename+"_solvedBoard.txt"])

if __name__ == "__main__":
    main(sys.argv[1:])
