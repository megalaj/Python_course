#Convert fastq file into fasta file
from Bio import SeqIO
count=SeqIO.convert("../Pune-C3.assembled.fastq","fastq","../Pune-C3.assembled.fasta","fasta")
print("converted %i records" % count)

#Filter out short sequences (<300)
from Bio import SeqIO
input_filename = "../Pune-C3.assembled.fasta"
output_filename = "../len_filtered_Pune-C3.assembled.fasta"
min_len = 300
count = 0
total = 0
output_handle = open(output_filename, "w")
for record in SeqIO.parse(input_filename, "fasta"):
    total += 1
    if len(record) >= min_len:
        count += 1
        SeqIO.write(record, output_handle, "fasta")
output_handle.close()
print(" %i records selected out of %i " % (count, total))

#filter out unique sequences (usearch?)
        
#Separate the 16S and the resistance gene part of the sequences by slicing the sequence according to the known sequence or at the expected length (82)
    #Make a new file with lists called by the seqID ex:seq_name[NDM,16S]
input_filename = "len_filtered_Pune-C3.assembled.fasta"
output_filename = "split_list"
len_Rpart = 82 
output_handle = open(output_filename, "w")
for record in SeqIO.parse(input_filename, "fasta"):
    Rgene = str(record.id) + "_Rgene" + "\n" + str(record.seq[:len_Rpart])
    part16S =  str(record.id) + "_16S" + "\n" + str(record.seq[len_Rpart:])
    SeqIO.write(Rgene, output_handle, "fasta")
    SeqIO.write(part16S, output_handle, "fasta")
output_handle.close()
    #OR create 2 files 
input_filename = "len_filtered_Pune-C3.assembled.fasta"
output_Rgene =
output_16S =
len_Rpart = 82 
output_handle = open(output_Rgene, "w")
for record in SeqIO.parse(input_filename, "fasta"):
    record.seq = record.seq[:len_Rpart]
    SeqIO.write(record, output_handle, "fasta")
output_handle.close()   
output_handle = open(output_16S, "w")
for record in SeqIO.parse(input_filename, "fasta"):
    record.seq = record.seq[len_Rpart:]
    SeqIO.write(record, output_handle, "fasta")
output_handle.close()  
#Eliminate the sequences that do not have the sequence of the resistance gene
    #
#(eliminate the primer sequences)
#create OTUs (usearch -cluster_fast)
    #Create clusters based on similarity 
    #Find consensus seq for each cluster
#Blast the consensus seq of each OTU to a 16S database (silva and/or NCBI)
#Create a phylogenetic tree
