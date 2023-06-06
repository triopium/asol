import os
import matplotlib.pyplot as plt
from typing import List

def get_files(directory_path: str) -> List[str]:
    files = []
    for root, _, filenames in os.walk(directory_path):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            files.append(file_path)
    return files

# def graph_count_files_week(directory: str):
#     week_counts = {}
#     # for filename in os.listdir(directory):
#         if filename.endswith(".json"):
#             # Extract the week number from the file name
#             parts = filename.split("-")
#             weekly_counts = int(parts[1])

#             # Increment the count for the week
#             week_counts[weekly_counts] = week_counts.get(weekly_counts, 0) + 1

#     # Sort the week counts by week number
#     sorted_weeks = sorted(week_counts.items())

#     # Extract the week numbers and counts
#     weeks, counts = zip(*sorted_weeks)

#     # Plot the data
#     plt.plot(weeks, counts, marker="o")
#     plt.title("Number of Files per Week")
#     plt.xlabel("Week Number")
#     plt.ylabel("File Count")
#     plt.show()

