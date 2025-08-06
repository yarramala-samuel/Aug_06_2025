import os


#creating data_input if that didnt exist
input_folder = "data_input"
output_folder = "data_output"


if not os.path.exists(input_folder):
    os.mkdir(input_folder)
    print(f"'{input_folder}' folder created. Please add .txt files to it and rerun the script.")
    exit()


#creating data_output if that didnt exist
if not os.path.exists(output_folder):
    os.mkdir(output_folder)


#processing all text files in the folder
summary_lines = []


for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)


        line_count = 0
        word_count = 0
        modified_lines = []


        with open(input_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip().startswith("#"):
                    continue  # Ignore comment lines
                line_count += 1
                word_count += len(line.split())
                modified_line = line.replace("temp", "permanent")
                modified_lines.append(modified_line)


        #saving the file which was modified, saving that file into data_output
        with open(output_path, 'w', encoding='utf-8') as f:
            f.writelines(modified_lines)


        # as asked, creating summary file to show the file name, line count and word count
        summary_lines.append(f"{filename} | Lines: {line_count} | Words: {word_count}")


#Writing into summary.txt (file which we created earlier)
summary_path = os.path.join(output_folder, "summary.txt")
with open(summary_path, 'w', encoding='utf-8') as f:
    f.write("Filename | Line Count | Word Count\n")
    f.write("-----------------------------------\n")
    for line in summary_lines:
        f.write(line + "\n")


print("Processing complete. Modified files and summary.txt are saved in 'data_output'.")