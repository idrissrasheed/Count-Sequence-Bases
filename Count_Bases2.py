# Read txt file
dataset = open("rosalind_dna.txt", "r")
dataset = dataset.read()

# Create function to count the number of characters in a string
def count_bases2(seq):
    return seq.count("A"), seq.count("G"), seq.count("C"), seq.count("T")

# Output 
print("A", "G", "C", "T", "\n", count_bases2(dataset))

