size = 9

import argparse
parser = argparse.ArgumentParser(description="Solve a sudoku puzzle")
parser.add_argument('minisatinputfile')
parser.add_argument('minisatoutputfile')
args = parser.parse_args()

def from_base(n, base):
    n = int(n) - 1
    k = n % base + 1
    j = int(((n - (k - 1)) / base) % base + 1)
    i = int(((n - (k - 1)) - base * (j - 1))/ (base * base)) + 1
    return (i, j, k)

with open(args.minisatinputfile, 'r') as content_file:
    minisatOutput = content_file.read()
    minisatOutput = minisatOutput.split()

if (minisatOutput[0] != "SAT"):
    print ("Sudoku puzzle can't be solved :(")
    exit(0)

# get rid of first line
minisatOutput.pop(0)

outputBoard = [[0 for i in range(9)] for j in range(9)]
for v in minisatOutput:
    result = int(v)
    if result > 0:
        (i, j, k) = from_base(result, size)
        outputBoard[i-1][j-1] = k

# write out file
outputFile = open(args.minisatoutputfile, "w")

output = ""
for i in range(size):
    for j in range(size):
        output += str(outputBoard[j][i]) + " "
    output += "\n"

outputFile.write(output)
outputFile.close()