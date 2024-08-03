# This code take a .gbf GeneBank file and extract protein sequences from it. 

from Bio import SeqIO

# Specifica il percorso del tuo file GenBank
file_path = ""

# Crea un dizionario per memorizzare le sequenze proteiche
protein_sequences = {}

# Apre il file GenBank e lo legge
with open(file_path, "r") as gb_file:
    for record in SeqIO.parse(gb_file, "genbank"):
        # Estrai il nome dell'organismo
        organism = record.annotations["organism"]
        
        # Estrai le sequenze proteiche contrassegnate come "translation"
        for feature in record.features:
            if "translation" in feature.qualifiers:
                protein_sequence = feature.qualifiers["translation"][0]
                locus_tag = feature.qualifiers.get("locus_tag", ["N/A"])[0]
                product = feature.qualifiers.get("product", ["N/A"])[0]
                protein_id = feature.qualifiers.get("protein_id", ["N/A"])[0]
                
                # Aggiungi la sequenza proteica al dizionario
                protein_sequences[f">{organism}|{locus_tag}|{product}|{protein_id}"] = protein_sequence

# Scrivi le sequenze proteiche nel file multifasta
with open("protein_output.fasta", "w") as protein_output_file:
    for header, sequence in protein_sequences.items():
        protein_output_file.write(f"{header}\n{sequence}\n")
