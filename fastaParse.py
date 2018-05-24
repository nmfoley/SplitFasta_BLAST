###########################################################################################################################
## FastaParse
##
## This script extracts a list of target sequences from a fasta file. 			
##
## usage: python fastaParse.py -fasta [input fasta file] -seq [list of target seq to extract] -out [prefix for outfiles] 
###########################################################################################################################

from Bio import SeqIO
import argparse

# setup arguments for the program.  This came from Daray's version of the script
def get_args():
	parser = argparse.ArgumentParser(description="Split fasta infile into two files based on blast results. One file will contain fastas for blast hits, the other will contain non-hits", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('-fasta', '--fasta', type=str, help='fasta file', required=True)
	parser.add_argument('-seq', '--seq', type=str, help='list of target seq to extract', required=True)
	parser.add_argument('-out', '--out', help='Prefix for output file', required=True)

	args = parser.parse_args()
	FASTA = args.fasta
	SEQ = args.seq
	PREFIX = args.out

	return FASTA, SEQ, PREFIX
FASTA, SEQ, PREFIX = get_args()

# create and open a file to collect results from the loop below
HITS = open(PREFIX + '.highQC_miRNA.fa', 'w')

# open the list of target seq for reading
FILE = open(SEQ).read()

# for every sequence in the fasta file, check to see if the record.id is in the list of target seq.
# if the record id from the fata file matches an id in the list of target seq, 
# write that fasta record to the HITS file in fasta format

for RECORD in SeqIO.parse(FASTA, 'fasta'):
        if RECORD.id in FILE:
                SeqIO.write(RECORD, HITS, 'fasta')

# Close both output files				
HITS.close()
