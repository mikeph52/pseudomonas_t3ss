from Bio import SeqIO

# data absolute paths
df_pst = "data/GCF_000007805.1_ASM780v1_genomic.fna"
df_pss = "data/GCF_043515225.1_ASM4351522v1_genomic.fna"

# ret
pst = list(SeqIO.parse(df_pst, "fasta"))
pss = list(SeqIO.parse(df_pss, "fasta"))

for record1 in pst:
    print(record1.id)
    print(record1.description)

for record2 in pss:
    print(record2.id)
    print(record2.description)