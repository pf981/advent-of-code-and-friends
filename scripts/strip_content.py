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
        r"inp\s*=\s*'.*'.*\n*"
    ]

    # Process each file in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".py") or filename.endswith(".R"):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            with open(input_path, "r") as f:
                content = f.read()

            # Apply each pattern to remove matches
            for pattern in patterns:
                content = re.sub(pattern, "", content)
            
            # Replace inp = '''...''' with
            # from aocd import get_data
            # inp = get_data(day=10, year=2024)
            if filename != "template.py":
                year, day = (int(num) for num in re.findall(r'\d+', filename))

                header = f"from aocd import get_data\n\ninp = get_data(day={day}, year={year})\n\n"
                content = header + content


            with open(output_path, "w") as f:
                f.write(content)

    print(f"Processed files from {input_dir} and saved to {output_dir}")


input_directory = "./python/"
output_directory = "./python2/"
clean_databricks_comments(input_directory, output_directory)
