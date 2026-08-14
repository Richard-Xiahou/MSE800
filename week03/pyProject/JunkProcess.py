
data = open("junk.txt") # Default is open for reading

lines = data.readlines() # Get a list of all the lines in the file 
print("Total lines:", len(lines))

# print whole txt file content
for line in lines:
  print(line[0:-1])

data.close()


# convert to lowcase
newLines = []
for line in lines:
  newLines.append(line.lower())

# add a new line
newLines.append("\ntext file nanalysis\n")

# Save the processed file
data = open("Junk.txt", "w")
for line in newLines:
    data.write(line)

# print whole txt file content
for line in lines:
  print(line[0:-1]) 

data.close()

print("good!-----,File processing completed.")