import time

start = time.time()

def count_duplicates(vorody):
    unique = list(set(vorody))
    zeroes = [0 for i in range(len(unique))]
    count = dict(zip(unique, zeroes)) 
    for i in vorody:
        count[i] += 1
    return count
        

raw_input = input("Neter Your Numbers with space : ")
raw_input = raw_input.split()

inputs = list(map(int, raw_input))

sum_inputs = sum(inputs)
max_inputs = max(inputs)
len_inputs = len(inputs)
duplicated_numbers = count_duplicates(inputs)
print("Sum : {}, max : {}, len_inputs : {}, dunpicated : {}".format(sum_inputs, max_inputs, len_inputs, duplicated_numbers))

stop = time.time()

print("Time is : {}".format(stop - start))



