import argparse
parser = argparse.ArgumentParser(description="Enter file to be formatted")
parser.add_argument('inputfile')
args = parser.parse_args()

file = open(args.inputfile, "r")
output = ""

for line in file:
    everything = line.split()
    for thing in everything:
        output += thing

outputfile = open(args.inputfile+"_formatted" , "w")
outputfile.write(output)
outputfile.close()

file.close()