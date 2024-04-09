#!/usr/bin/python3

# Open the input file in read mode
infile = open("full path to output_1.txt", "r", encoding='utf-8')

# Create an empty set to store the unique lines
unique_lines = set()

# Create an empty list to store the output lines
output_lines = []

# Loop through each line in the input file
for line in infile:
    # Strip the trailing newline character from the line
    line = line.rstrip("\n")

    # If the line is not empty and not already in the set, add it to the set and the list
    if line and line not in unique_lines:
        unique_lines.add(line)
        output_lines.append(line)

    # If the line is empty, add it to the list
    elif not line:
        output_lines.append(line)

# Close the input file
infile.close()

# Open the output file in write mode
outfile = open("new path to save output_2.txt", "w", encoding='utf-8')

# Write each line in the output list to the output file, followed by a newline character
for line in output_lines:
    outfile.write(line + "\n")

# Close the output file
outfile.close()

