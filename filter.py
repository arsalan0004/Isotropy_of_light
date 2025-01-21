# filter the dataset so that it does not have duplicates 


raw_file      = open("output2.txt", 'r')
filtered_file = open("filtered.txt", 'a')

unique_lines = set()

for line in raw_file:
    if(line not in unique_lines):
        filtered_file.write(line)
        unique_lines.add(line)