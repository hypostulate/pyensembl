from pyensembl import Locus

#mapping of ensembl releases to transcript IDs for FOXP3-001
FOXP3_001_transcript_id = "ENST00000376207"

TP53_gene_id = "ENSG00000141510"

# beta-catenin interacting protein from the negative strand of chromosome 1
# URL: http://useast.ensembl.org/Homo_sapiens/Transcript/Sequence_cDNA?
#      db=core;g=ENSG00000178585;r=1:9848276-9910336;t=ENST00000377256
CTNNBIP1_004_transcript_id = "ENST00000377256"

# coding sequence for beta-catenin interacting protein (CTNNBIP1-004)
CTNNBIP1_004_CDS = "".join([
    "ATG",
    "AACCGCGAGGGAGCTCCCGGGAAGAGTCCGGAG",
    "GAGATGTACATTCAGCAGAAGGTCCGAGTGCTGCTCATGCTGCGGAAGATGGGATCAAAC",
    "CTGACAGCCAGCGAGGAGGAGTTCCTGCGCACCTATGCAGGGGTGGTCAACAGCCAGCTC",
    "AGCCAGCTGCCTCCGCACTCCATCGACCAGG",
    "GTGCAGAGGACGTGGTGATGGCGTTTTCCAGGTCGGAGACGGAAGACCGGAGGCAG",
    "TAG"
])

# 5' UTR for beta-catenin interacting protein (CTNNBIP1-004)
CTNNBIP1_004_UTR5 = "".join([
    "TGTGGGTGCAGGTTTCCTGGGCTTGCCAGACACACAGGGCGGCACCTTCCTACTTCTGCC",
    "CAGCCACAGCCCTCCCCTCACAGTTGAGCACCTGTTTGCCTGAAGTTAATTTCCAGAAGC",
    "AGGAGTCCCCAGAGCCAGGCAGGGGG"])

# 3' UTR for beta-catenin interacting protein (CTNNBIP1-004)
CTNNBIP1_004_UTR3 = \
    "CTGCAAAGCCCTTGGAACACCCTGGATGCTGTTGAGGGCCAAGAGATCTGTGTGGCTCC"

CTNNBIP1_004_locus = Locus("1", 9850659, 9878176, "-")

# properties of CTNNBIP1-004's exons copied from
# http://useast.ensembl.org/Homo_sapiens/Transcript/Exons?g=ENSG00000178585;
# r=1:9850659-9878176;redirect=no;t=ENST00000377256
CTTNNIP1_004_exon_ids = [
    'ENSE00001473268',
    'ENSE00001643659',
    'ENSE00001600669',
    'ENSE00001267940',
    'ENSE00001473265',
]

CTTNNIP1_004_exon_lengths = [
    37,
    85,
    120,
    91,
    118
]
