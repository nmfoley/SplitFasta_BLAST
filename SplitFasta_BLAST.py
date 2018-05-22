#############################################################
#					Jenny's Fasta Blast Parser
## This program will parse a fasta file into two files based on blast results. 
## One output file will contain fastas for blast hits "prefix.nohits.fasta", the other will contain non-hits "prefix.nohits.fasta"
## usage: python fastaParse_attempt2.py -fasta [your_fasta_file] -blast [your_blast_results] -out [prefix_for_outfiles]
#############################################################

# import required stuff to make it go
from Bio import SeqIO
import argparse

# setup overly complicated arguments for the program.  This came from Daray's version of the script
def get_args():
	parser = argparse.ArgumentParser(description="Split fasta infile into two files based on blast results. One file will contain fastas for blast hits, the other will contain non-hits", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('-fasta', '--fasta', type=str, help='peptidefasta', required=True)
	parser.add_argument('-blast', '--blast', type=str, help='blastp', required=True)
	parser.add_argument('-out', '--out', help='Prefix', required=True)

	args = parser.parse_args()
	FASTA = args.fasta
	BLAST = args.blast
	PREFIX = args.out

	return FASTA, BLAST, PREFIX
FASTA, BLAST, PREFIX = get_args()

# print sanity checks to make sure the arguments are accepted as intended and you have the right files
print("Input = " + FASTA + ".")
print("Input blast = " + BLAST + ".")
print("prefix = " + PREFIX + ".")

# create and open two files to write the fastas to in the loop below
HITS = open(PREFIX + '.hits.fasta', 'w')
NOHITS = open(PREFIX + '.nohits.fasta', 'w')

# open the blast results input file for reading
FILES = open(BLAST).read()

# for every fasta sequences in the fasta file, check to see if the record.id is in the blast output (called 'FILES')
# if record id is found in the blast output, write that fasta record to the HITS file in fasta format
# if record id is NOT found in the blast output, write that fasta record to the NOHITS file in fasta format
for RECORD in SeqIO.parse(FASTA, 'fasta'):
        if RECORD.id in FILES:
                SeqIO.write(RECORD, HITS, 'fasta')
        else:
             	SeqIO.write(RECORD, NOHITS, 'fasta')

# Close both output files				
HITS.close()
NOHITS.close()
