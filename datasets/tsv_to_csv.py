import re

with open("sample_nodes.tsv", 'r') as myfile:
    with open("sample_nodes.csv", 'w') as csv_file:
        for line in myfile:

            # Replace every tab with comma
            fileContent = re.sub("\t", ",", line)

            # Writing into csv file
            csv_file.write(fileContent)

print("Successfully made csv file! No errors detected.")
