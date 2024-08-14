from BCBio import GFF
from Bio import SeqIO

gff_file = '/Users/febrinam/Documents/NIGINTERN/Gryllus/scaffoldrelated_genesfinal.gff'
scaffolds, features, starts, ends, strands, qualifiers = [],[], [], [], [], []
GBI_IDs,DBxRefs,Notes = [],[],[]
with open(gff_file) as gff_handle:
    for record in GFF.parse(gff_handle):
        print(f"Record ID: {record.id}")
        for feature in record.features:
            start = feature.location.start
            end = feature.location.end
            strand = feature.location.strand
            scaffold = record.id
            print(f"Scaffold: {scaffold}, Feature Type: {feature.type}, Start: {start}, End: {end}, Strand: {strand}")
            for key, value in feature.qualifiers.items():
                print(f"  {key}: {value}")
            scaffolds.append(scaffold)
            features.append(feature.type)
            starts.append(start)
            ends.append(end)
            strands.append(strand)
            # GBI_IDs.append(feature.qualifiers['Name'][0])
            qualifiers.append(feature.qualifiers)
            # GBI_IDs.append(feature.qualifiers['Name'])
            # DBxRefs.append(feature.qualifiers['Dbxref'])
            # Notes.append(feature.qualifiers['Note'])
df = pd.DataFrame({'Scaffold':scaffolds, 'Feature': features, 'Start': starts, 'End': ends, 'Strand': strands,'Qualifier':qualifiers})
