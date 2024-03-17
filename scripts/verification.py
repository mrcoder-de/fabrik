"""
This is a short script for outputting the table for the REVIEW.md file
"""

import os

from tabulate import tabulate

# Define the directory to explore
dir_to_explore = "patterns"
# Get a list of all subdirectories
subdirs = sorted([d for d in os.listdir(dir_to_explore) if os.path.isdir(os.path.join(dir_to_explore, d))])
# Prepare data for tabulate
table = [[i + 1, subdir] for i, subdir in enumerate(subdirs)]
# Create a markdown table
markdown_table = tabulate(table, headers=['Index', 'Subdirectory'], tablefmt="pipe")

print(markdown_table)
