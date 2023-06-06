import os
import re
import matplotlib.pyplot as plt
from typing import List
from datetime import datetime

import logging
from . import logger
logerr = logging.getLogger(__name__)
logerr.addHandler(logger.handler_stderr)

def graph_count_files_week(directory: str):
    files=get_files(directory)
    weekly={}
    for file in files:
        yval=""
        info,ok=parse_date_newname(file)
        if not ok:
            continue
        yval=(f"{info['year']}_W{info['week']}")
        cvalue = weekly.get(yval, 0)
        weekly[yval]=cvalue+1

    ### Save graph
    keys=list(weekly.keys())
    counts=list(weekly.values())

    path = os.path.join(directory,"graph_count_files_week")
    fullpath=os.path.abspath(path)
    fig, ax = plt.subplots()
    # ax.plot(keys, counts)
    # ax.scatter(keys, counts)
    ax.bar(keys, counts)
    num_ticks = 5  # Number of ticks to display
    step = len(keys) // num_ticks  # Determine the step size
    ax.set_xticks(keys[::step])
    ax.set_xticklabels(keys[::step])
    ax.set_xlabel('Week')
    ax.set_ylabel('Weekly count')
    ax.set_title('Contributions per week')

    plt.savefig(fullpath)
    
def get_files(directory_path: str) -> List[str]:
    files = []
    for root, _, filenames in os.walk(directory_path):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            files.append(file_path)

    sorted_files = sorted(files)
    return sorted_files

def parse_date_newname(filename: str) -> tuple[dict,bool]:
    pattern = r"(\d{4}).W(\d{2}).(\d{2})-(\d{2})_(\d+)\.json$"
    match = re.search(pattern, filename)
    if match:
        rdict=dict()
        rdic={ 
              'year': int(match.group(1)),
              'week': int(match.group(2)),
              'month': int(match.group(3)),
              'day': int(match.group(4)),
              'seqnum': int(match.group(5)),
              }
        return rdic,True
    return None,False


