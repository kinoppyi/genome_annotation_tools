import re
import argparse

# Function to modify the last column based on specified conditions
def modify_gtf_line(line, attribute_prefix):
    fields = line.strip().split('\t')
    feature_type = fields[2]
    attributes = fields[8]

    if feature_type == "gene" or feature_type == "transcript":
        attributes = attribute_prefix + attributes
    else:
        attributes = re.sub(r'transcript_id "([^"]+)"', r'transcript_id "' + attribute_prefix + r'\1"', attributes)
        attributes = re.sub(r'gene_id "([^"]+)"', r'gene_id "' + attribute_prefix + r'\1"', attributes)

    fields[8] = attributes
    return '\t'.join(fields)

def main(input_file, output_file, attribute_prefix):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.strip():
                modified_line = modify_gtf_line(line, attribute_prefix)
                outfile.write(modified_line + '\n')
    print(f"Modified file saved to: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=(
            "Modify GTF files to add a prefix to IDs.\n"
            "This script is particularly useful for annotations of large genomes where chromosomes "
            "are split into individual files. When merging these files back into a single GFF or GTF, "
            "it becomes necessary to rename the outputs to ensure unique identifiers."
        ),
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('-i', '--input', required=True, help="Input GTF file")
    parser.add_argument('-o', '--output', required=True, help="Output GTF file")
    parser.add_argument('-a', '--attribute', required=True, help="Prefix to add to IDs (the text you want to add must be enclosed in quotes)")

    args = parser.parse_args()
    main(args.input, args.output, args.attribute)
