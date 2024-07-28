import argparse
from Bio import SeqIO

def filter_short_proteins(input_fasta, output_fasta, min_length=50):
    with open(output_fasta, 'w') as output_handle:
        for record in SeqIO.parse(input_fasta, "fasta"):
            if len(record.seq) >= min_length:
                SeqIO.write(record, output_handle, "fasta")

def main():
    parser = argparse.ArgumentParser(
        description="Filter out proteins shorter than a specified length from a multifasta file.\n"
                    "This script reads a multifasta file, filters out protein sequences that are "
                    "shorter than the specified length, and writes the remaining sequences to an "
                    "output file. This can be particularly useful for genome annotation projects "
                    "where short, potentially non-functional protein predictions need to be excluded.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('-i', '--input', required=True, help='Input multifasta file containing protein sequences')
    parser.add_argument('-o', '--output', required=True, help='Output multifasta file to write filtered protein sequences')
    parser.add_argument('-l', '--length', type=int, default=50, help='Minimum length of proteins to keep (default: 50 amino acids)')

    args = parser.parse_args()

    filter_short_proteins(args.input, args.output, args.length)

    print(f"Proteins with at least {args.length} amino acids have been saved to {args.output}")

if __name__ == "__main__":
    main()
