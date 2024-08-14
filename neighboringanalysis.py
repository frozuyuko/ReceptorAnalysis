inputgff = '/Users/febrinam/Documents/NIGINTERN/Dataset/Gbi_Genes.gff'
outputgff = '/Users/febrinam/Documents/NIGINTERN/Crickets_Genome_Annotation/Annotation_files/scaffoldrelated_genes.gff'
input_file = '/Users/febrinam/Documents/NIGINTERN/Gryllus/scaffoldrelated_genesfinal.gff'
from BCBio import GFF
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
def CreateGFFScafoldFilter(inputgff,outputgff,scaffoldlists): #scaffoldlists should be in form of list
    limit_info = dict(gff_type=["gene","mRNA"],gff_id=scaffoldlists)
    in_handle = open(inputgff)
    out_handle = open(outputgff, "w")
    for rec in GFF.parse(in_handle, limit_info=limit_info):
        GFF.write([rec], out_handle)
def ScaffoldNeighboring(inputgff,scaffoldfind,posstart,posend,gap):
    in_handle = open(inputgff)
    limit_info = dict(gff_id=[scaffoldfind])
    for rec in GFF.parse(in_handle, limit_info=limit_info):
        for feature in rec.features:
            if feature.type == 'gene':
                start = feature.location.start
                end = feature.location.end
                if not (end < posstart - gap or start > posend + gap):
                    print(f"Feature: {feature.type}, Start: {start}, End: {end}")
                    for key, value in feature.qualifiers.items():
                        print(f"  {key}: {value}")
    in_handle.close()
ScaffoldNeighboring(inputgff,'Scaffold153',2142142,2267228,15000)
