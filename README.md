# SAT-based Sudoku Solver #

### University of Victoria ###
> CSC 320: Foundations of Computer Science

| Members      | Student Number |
| ------------ | -------------- |
| Rahat Mahbub |    V00790465   |
| Rafat Mahmud |    V008        |

### Files ###

 	* Sud2sat.java - reads a Sudoku puzzle (in some specified text format) and converts it to a CNF formula suitable for input to the miniSAT SAT solver.

	* Sud2SatExtended.java - Same as above but uses extended encoding, in addition to minimal encoding.

	* sat2sud.py - reads the output produced by miniSAT for a given puzzle instance and converts it back into a solved Sudoku puzzle (suitable for printing)

	* extractor.py - Takes in a file with many sudoku puzzles, cleans them and uses Sud2Sat, minisat and sat2sud to produce a final solved board for each.

	* fiftygrids.sudoku - https://projecteuler.net/project/resources/p096_sudoku.txt
	* top95.sudoku - http://magictour.free.fr/top95
	* hexa*.sudoku - 16X16 sudoku puzzles

	* outputformatter.py - Formats a solved board to be checked by: www.sudoku-solutions.com

### Program Requirements ###
    * Java
    * Python
    * minisat

### Usage ###

	* extractor.py - Use this to solve many puzzles at once.
		$ python extractor.py top95.sudoku
		To use extended encoding:
		$ python extractor.py fiftygrids.sudoku extended

	* Sud2sat -
		Compile with:
		$ javac Sud2sat.java
		Run with:
		$ java Sud2sat <sudoku-filename> <dimacs-output-file-name>

	* Sud2SatExtended -
		Compile with:
		$ javac Sud2SatExtended.java
		Run with:
		$ java Sud2SatExtended <sudoku-filename> <dimacs-output-filename>

	* sat2sud.py -
		$ python sat2sud.py <minisat-output> <solved-board-output-filename>
