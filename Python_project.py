#Convert fastq file into fasta file
def fastq_to_fasta(input_file, output_file):
        from Bio import SeqIO
        count=SeqIO.convert("input_file","fastq","output_file","fasta")
        print("converted %i records" % count)

#Filter out short sequences
def filter_short(input_file, output_file, min_length):
    from Bio import SeqIO
    count = 0
    total = 0
    output_handle = open(output_file, "w")
    for record in SeqIO.parse(input_file, "fasta"):
        total += 1
        if len(record) >= min_length:
            count += 1
            SeqIO.write(record, output_handle, "fasta")
    output_handle.close()
    print(" %i records selected out of %i " % (count, total))
        
#Cut the sequences at the expected length of the first part
    #Duplicate the headers and associate each one with a part of the sequence
def slice_seq(input_file, output_file, len_first_part):
    from Bio import SeqIO
    output_handle = open(output_file, "w")
    for record in SeqIO.parse(input_file, "fasta"):
        partA = str(record.id) + "_A" + "\n" + str(record.seq[:len_first_part])
        partB =  str(record.id) + "_B" + "\n" + str(record.seq[len_first_part:])
        SeqIO.write(partA, output_handle, "fasta")
        SeqIO.write(partB, output_handle, "fasta")
    output_handle.close()
    #OR create 2 files with on part of the sequence in each
def slice_seq_2(input_file, output_file_A, output_file_B, len_first_part):
    from Bio import SeqIO
    output_handle = open(output_file_A, "w")
    for record in SeqIO.parse(input_file, "fasta"):
        record.seq = record.seq[:len_first_part]
        SeqIO.write(record, output_handle, "fasta")
    output_handle.close()   
    output_handle = open(output_file_B, "w")
    for record in SeqIO.parse(input_file, "fasta"):
        record.seq = record.seq[len_first_part:]
        SeqIO.write(record, output_handle, "fasta")
    output_handle.close()  
    
#Eliminate the sequences that do not have the sequence of the resistance gene
#(eliminate the primer sequences)
#create OTUs (usearch -cluster_fast)
    #Create clusters based on similarity 
    #Find consensus seq for each cluster
#Blast the consensus seq of each OTU to a 16S database (silva and/or NCBI)
#Create a phylogenetic tree
