def count_bases1(sequence, base):
    i = 0 # start count at 0 
    for b in sequence:
        if b == base:
            i += 1
    return i

sequence = input("Enter a sequence in all caps: ") # User input 
base = input("Enter a single base in a capital letter: ") 
n = count_bases1(sequence, base)
print('{base} = {n}'.format(base=base, n=n))

## Sample input and output
# Enter a sequence in all caps: ACGTGTGTTTTGAC
# Enter a single base in a capital letter: A
# A = 2



