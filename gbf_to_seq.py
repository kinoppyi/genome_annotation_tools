# This code take a .gbf GeneBank file and extract coding sequences sequences from it. 

from Bio import SeqIO

# Specifica il percorso del tuo file GenBank
file_path = ""

# Crea un dizionario per memorizzare le sequenze CDS
sequences = {}

# Apre il file GenBank e lo legge
with open(file_path, "r") as gb_file:
    for record in SeqIO.parse(gb_file, "genbank"):
        # Estrai il nome dell'organismo
        organism = record.annotations["organism"]
        
        # Estrai le sequenze CDS
        for feature in record.features:
            if feature.type == "CDS":
                sequence = feature.location.extract(record).seq
                locus_tag = feature.qualifiers.get("locus_tag", ["N/A"])[0]
                product = feature.qualifiers.get("product", ["N/A"])[0]
                protein_id = feature.qualifiers.get("protein_id", ["N/A"])[0]
                
                # Aggiungi la sequenza al dizionario
                sequences[f">{organism}|{locus_tag}|{product}|{protein_id}"] = sequence

# Scrivi le sequenze nel file multifasta
with open("output.fasta", "w") as output_file:
    for header, sequence in sequences.items():
        output_file.write(f"{header}\n{sequence}\n")
