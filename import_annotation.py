import shutil

# User input (change this string or rewrite this part to prompt to select file later)
TIMESTAMP_FILE_PATH = "INPUT/shaping3_rat5_6_day5.txt"

# Load in text file
timestamps = open(TIMESTAMP_FILE_PATH, "r")
code = timestamps.readlines()
total = len(code)
timestamps.close()

# Start writing to annotations
annotation = open("template.annotation/annotations.xml","w") 
annotation.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>")
annotation.write("\n")
annotation.write("<data>")

# Insert in timestamps
for i in range(0, total):
    annotation.write("\n\t<event startTimeInterval=\"") 
    pair = str.split(code[i])
    event = pair[0]
    time = pair[1]
    # Write timepoint
    annotation.write(time)
    annotation.write("\" ")
    # Dummy dates; redundant information for us
    annotation.write("start=\"December 9 9999 00:00:00 GMT-0800\" ")
    annotation.write("annotation-modificationDate=\"December 9 9999 00:00:00 GMT-0700\" ")
    # Default lab username
    annotation.write("annotation-modificationUser=\"Basolateral\" ")
    annotation.write("annotation-category=\"")
    # Write event tag
    annotation.write(event)
    annotation.write("\" ")
    # Dummy image; not sure what this is used for
    annotation.write("image=\"images/dummy.jpg\">")
    # Write event tag again
    annotation.write("<category name=\"")
    annotation.write(event)
    annotation.write("\"></category>\n")
    annotation.write("\t</event>")

# Close <data> element
annotation.write("\n</data>")
annotation.close() 

# Send annotation folder to OUTPUT
OUTPUT_FILE_PATH = TIMESTAMP_FILE_PATH[6:len(TIMESTAMP_FILE_PATH) - 4] + ".annotation"

# Create annotation folder at 
try:
    shutil.copytree("template.annotation", "OUTPUT/" + OUTPUT_FILE_PATH)
except FileExistsError:
    shutil.rmtree("OUTPUT/" + OUTPUT_FILE_PATH)
    shutil.copytree("template.annotation", "OUTPUT/" + OUTPUT_FILE_PATH)
