def print_pattern(num_rows):
    for i in range(num_rows):
        print("*" * (num_rows - i))
    print()
        
print_pattern(5)
print_pattern(3)

# TODO: Create new function with two params - one for character, 
#       one for num rows

def print_patt(pattern,rows):
    for i in range(0,rows):
        print(pattern * (rows-i))

print_patt("£", 10)

