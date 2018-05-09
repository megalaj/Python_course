From the fasta file separate the 16S and the resistance gene part of the sequences.
Load the data into python(open or with biopython load as sequence object)
Either slice the sequence according to the known sequence or at the expected length (82)
Write either 2 different files with one part of the sequence each or a new file with the 2 parts of the sequence separated (list[NDM,16S]).
(eliminate the primer sequences)
(create OTUs)
Create clusters based on similarity (unix)
Find a consensus seq for each cluster
Blast the 16S to a 16S database (silva et/NCBI)
Create a phylogenetic tree
