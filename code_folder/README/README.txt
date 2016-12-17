Here is a list of the functions of all the python codes and some txt files 

pase_DNA.py: 				
parses the raw genome info file from database to pure nuleotide sequence

parse_protein.py: 			
parses the raw protein info file from database to pure peptide sequence

dipeptide_occurrence.py:	
calculates the number of accurance of each dipeptidefor the given peptide sequence of 
difference species(preparing data for make_table.py)

get_frequency.py:			
calculates the number of accurance AND frequency of each dipeptide/dinucleotide for the given 
peptide/nucleotide sequence of difference species

make_table.py:				
Takes the results made by protein_sequencing.py, make a table of the number of dipeptide 
occurrence for all  five species. It will show 'None' if certain species don't have certain peptide 

separate_none.py:			
Takes the result from make_table.py and separate the table into two tables. One of them only shows the dipeptides and numbers 
of occurrence of five species when there is at least one of five species DOESN'T have it. The other table
shows the dipeptides and numbers of occurrence of the five species when ALL of them have it.

expect_occurrence.py:		
calculates the number of occurrence for single nucleotide/peptide and store them in a table

expect_observe_protein.py:	
Takes the table of observed dipeptide frequency and the table of single pepetide occurrence, 
and calculates the expected frequency of each dipeptide. Store both observed and expected
frequency in an output table

expect_observe_DNA.py:		
Takes a table of observed dinucleotide frequency and a table of single nucleotide occurrence, 
and calculates the expected frequency of each dinucleotide. Store both observed and expected
frequency in an output table

test_data_prep.py:			
Takes the observed outlier's data and find the expected value of those outliers. 
Store both the observed and expected value in test_protein.txt for dipeptide or test_DNA.txt 
for dinucleotide.

R_codes.txt:				
The R code for plotting the four graphs

plot_result folder:
Four plots of the result including two pdf files are in this folder.

other txt files: 			
The files made by the above codes. Most of them is self-explainary by their file name.
Or you may check the code file which makes certain txt file.




