import os

#get current path
folder_path = os.getcwd()+"/pic"
output_file = 'fileList.txt'

# Get all file names in the folder
file_names = os.listdir(folder_path)

# Sort the file names based on the number in the file name
sorted_file_names = sorted(file_names, key=lambda x: int(''.join(filter(str.isdigit, x))))

# Write the sorted file names to a text file
with open(output_file, 'w') as file:
    for file_name in sorted_file_names:
        file.write("pic/"+file_name + '\n')

print('File names sorted and recorded in', output_file)