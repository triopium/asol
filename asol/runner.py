import json
import logging
import os
import sys
from dataclasses import asdict, dataclass
from typing import Any, Optional

from . import logger

logerr = logging.getLogger(__name__)
logerr.addHandler(logger.handler_stderr)
import re
import shutil
from datetime import datetime


def count_files_norecurse(directory):
    return len(os.listdir(directory))

### stdout
@dataclass
class file_processing_data:
    source: str
    target: str

class Runner:
    def __init__(self, pars):
        self.params = pars
        files = os.listdir(pars.input)
        self.files = files
        self.filescount = len(files)
    def tester_debug(self):
        return True
    def params_debug(self):
        print(json.dumps(self.params.__dict__))

    def params_check(self):
        logerr.info("checking parameters")
        self.params = params_check(self.params)
        logerr.info(f"Files {self.filescount} to process")

    def simulate(self):
        self.params = params_check(self.params)
        logerr.info(f"Files {self.filescount} to process")
        processed = 0
        for f in self.files:
            fsource = os.path.join(self.params.input, f)
            fdate = date_from_filename(f)
            jdate = date_from_json(fsource)
            finaldate = fdate

            if jdate is None or fdate is None:
                ### error treated elswhere when parsing values from filename or json
                continue

            ### date in filename and json differs
            if jdate != fdate:
                logerr.error(f"date differs: {fsource}")
                if self.params.date_priority == "filename":
                    finaldate = fdate
                    if self.params.ammend_date:
                        ammend_date_in_json(fsource, fdate)

                if self.params.date_priority == "json":
                    finaldate = jdate
                continue
            seqnum, ok = extract_seqnum(f)
            if not ok:
                logerr.error("Cannot extract sequnece number from filename")
                continue
            dstdir = destination_path(finaldate, seqnum)
            ftarget = os.path.join(self.params.output, dstdir)
            moveinfo = file_processing_data(source=fsource, target=ftarget)
            print(json.dumps(moveinfo.__dict__))
            ok = move_file(fsource, ftarget, self.params.write, self.params.force)
            if ok:
                processed += 1

        if processed == self.filescount:
            logerr.info(f"Success: processed {processed}/{self.filescount} files")
        if processed != self.filescount:
            logerr.error(f"Failed: processed {processed}/{self.filescount} files")


def ammend_date_in_json(filepath: str, fdate: datetime):
    with open(filepath, "r") as file:
        data = json.load(file)
        newdate = fdate.strftime("%Y-%m-%d")
        data["date"] = newdate
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)


def move_file(src: str, dst: str, write: bool, forcewrite: bool) -> bool:
    err_file = f"input_file: {src}, error moving,"
    if os.path.exists(dst):
        if not forcewrite:
            logerr.error(f"{err_file} file already exists: {dst}")
            return False
        logerr.warn(f"{err_file} file already exists: {dst}")
    try:
        dstdir = os.path.dirname(dst)
        # print("heloo",dstdir)
        if write:
            dstdir = os.path.dirname(dst)
            os.makedirs(dstdir, exist_ok=True)
            shutil.move(src, dst)
        return True
    except IOError as e:
        logerr.error(f"{err_file} exception {e}")
        return False

def destination_path(date: datetime,seqnum:int) -> str:
    year,week_number,_=date.isocalendar()
    month=date.month
    day=date.day
    daynum=date.weekday()+1
    fname=f"{month:02d}-{day:02d}_{seqnum:d}.json"
    dstdir=os.path.join(f"{year:d}",f"W{week_number:d}",fname)
    return dstdir


def parse_date(date_string: str) -> datetime:
    try:
        format_string = "%Y-%m-%d"
        parsed_date = datetime.strptime(date_string, format_string)
        return parsed_date
    except ValueError:
        return none

def extract_seqnum(filename: str) -> tuple[int, bool]:
    pattern = r"\d{4}-\d{2}-\d{2}_(\d+)\.json$"
    match = re.search(pattern, filename)
    if match:
        return int(match.group(1)), True
    return 0, False

def date_from_filename(filename: str) -> datetime:
    # Use regular expression to extract date from filename
    pattern = r"\d{4}-\d{2}-\d{2}"
    match = re.search(pattern, filename)
    if match:
        fdate = parse_date(match.group())
        return fdate
    else:
        logerr.error("filename.date: no valid date")
        return None

def date_from_json(input_file: str) -> datetime:
    err_json = f"input_file: {input_file}, error parsing,"
    try:
        with open(input_file, "r") as file:
            try:
                json_data = json.load(file)
                jdatestr = json_data["date"]
                if jdatestr is None:
                    logerr.error(f"{err_json} json.date: None")
                    return None
                jdate = parse_date(jdatestr)
                if jdate is None:
                    logerr.error(f"{err_json} json.date: invalid date")
                    return None
                return jdate
            except json.JSONDecodeError as e:
                logerr.error(f"{err_json} json.date: invalid json, {e}")
                return None
            except Exception as e:
                logerr.error(f"{err_json} json.date: exception, {e}")
                return None
    except FileNotFoundError:
        logerr.error(f"{err_json} json.date: file not found")
        return None
    except PermissionError:
        logerr.error(f"{err_json} json.date: no permission error")
        return None
    except Exception as e:
        logerr.error(f"{err_json} json.date: exception, {e}")
        return None

def params_check(pars):
    """Check that parametrs are valid"""
    ### validate input dir
    if not os.access(pars.input, os.R_OK):
        raise ValueError(f"source dir not readable: {pars.input}")

    ### validate output dir
    if not os.path.exists(pars.output):
        raise ValueError(f"path does not exists: {pars.output}")
    if not os.path.isdir(pars.output):
        raise ValueError(f"path is not directory: {pars.output}")
    if not os.access(pars.output, os.W_OK):
        raise ValueError(f"output directory not writable: {pars.output}")
    if os.listdir(pars.output):
        logerr.warn(f"output directory not empty: {pars.output}")
    return pars
