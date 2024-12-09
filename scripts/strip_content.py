import os
import re


def clean_databricks_comments(input_dir, output_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Regex patterns to match Databricks comments and their surrounding newlines
    patterns = [
        r"# Databricks notebook source.*\n*",
        r"# MAGIC .*\n*",
        r"# COMMAND.*\n*",
        r"inp\s*=\s*'''(.|\n)*?'''\n*",
        r"inp\s*=\s*'.*'.*\n*",
        r'input\s<-\s"(.|\n)*?\n*"',
        r"input\s<-\s'(.|\n)*?\n*'"
    ]

    # Process each file in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".py") or filename.lower().endswith(".r"):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            with open(input_path, "r") as f:
                content = f.read()

            if filename not in "template.py" and "2024" not in filename:
                # Apply each pattern to remove matches
                for pattern in patterns:
                    content = re.sub(pattern, "", content)
                
                # Replace inp = '''...''' with
                # from aocd import get_data
                # inp = get_data(day=10, year=2024)
                year, day = (int(num) for num in re.findall(r'\d+', filename))

                if filename.endswith(".py"):
                    header = f"from aocd import get_data\n\ninp = get_data(day={day}, year={year})\n\n"
                    content = header + content


            with open(output_path, "w") as f:
                f.write(content)

    print(f"Processed files from {input_dir} and saved to {output_dir}")


# input_directory = "./python/"
# output_directory = "./python2/"
# input_directory = "./R/"
# output_directory = "./R2/"
# clean_databricks_comments(input_directory, output_directory)

def rename_files(input_dir):
    for filename in os.listdir(input_dir):
        if filename.endswith(".py"):
            if filename in "template.py":
                continue
            year, day = (int(num) for num in re.findall(r'\d+', filename))
            new_filename = f'{year}_{day:02}.py'
            print(f'Renaming "{filename}" to "{new_filename}"')
            os.rename(os.path.join(input_dir, filename), os.path.join(input_dir, new_filename))
        elif filename.lower().endswith(".r"):
            year, day = (int(num) for num in re.findall(r'\d+', filename))
            new_filename = f'{year}_{day:02}.R'
            print(f'Renaming "{filename}" to "{new_filename}"')
            os.rename(os.path.join(input_dir, filename), os.path.join(input_dir, new_filename))

# rename_files("./python/")
# rename_files("./R/")
