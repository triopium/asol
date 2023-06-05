import os
import json
import sys
from dataclasses import dataclass, asdict
import logging
from typing import Optional, Any
from . import logger
logerr = logging.getLogger(__name__)
logerr.addHandler(logger.handler_stderr)
import re
from datetime import datetime

def count_files_norecurse(directory):
    return len(os.listdir(directory))

### stdout
@dataclass
class filemove:
    source: str
    target: str


class Runner:
    def __init__(self,pars):
        self.params=pars
        files=os.listdir(pars.input)
        self.files=files
        self.filescount=len(files)
    def params_debug(self):
        print(json.dumps(self.params.__dict__))
    def params_check(self):
        logerr.info("checking parameters")
        self.params=params_check(self.params)
        logerr.info(f"Processing {self.filescount} files")

    def simulate(self):
        logerr.info("simulate run")
        self.params_check()
        processed=0
        for f in self.files:
            fdate=date_from_filename(f)
            print("fdate",fdate)
            fsource=os.path.join(self.params.input,f)
            ftarget=os.path.join(self.params.output,"hello")
            outinfo=filemove(source=fsource,target=ftarget)

            jdate=date_from_json(fsource)
            print("jdate",jdate)

def date_from_filename(filename: str) -> str:
    # Use regular expression to extract date from filename
    pattern = r"\d{4}-\d{2}-\d{2}"
    match = re.search(pattern, filename)
    if match:
        return match.group()
    else:
        return None


def parse_date(date_string: str) -> datetime:
    try:
        format_string = "%Y-%m-%d"
        parsed_date = datetime.strptime(date_string, format_string)
        return parsed_date
    except ValueError:
        return none

def date_from_json(input_file: str) -> datetime:
    err_json=f"input_file: {input_file}, error parsing file:"
    try:
        with open(input_file, 'r') as file:
            print(input_file)
            try:
                json_data = json.load(file)
                jdatestr=json_data['date']
                if jdatestr is None:
                    logerr.error(f"{err_json} json.date: None")
                    return None
                jdate=parse_date(jdatestr)
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



# def solve_output_file(input_file: str) -> str:
    # try:
        # with open(input_file, 'r') as file:
            # json_data = json.load(file)
            # print("hello",json_data.date)
            # return json_data
    # except Exception as e:
        # logerr.error(f"parsing json: {input_file}, {str(e)}")
        # return None
    # json_data=parse_json_file(input_file)
    # print(json_data)

# def compare_dates(fdate,jsondate):
# def parse_json_file(file_path: str) ->Optional[Any]:
    # try:
        # with open(file_path, 'r') as file:
            # json_data = json.load(file)
            # return json_data
    # except Exception as e:
        # logerr.error(f"parsing json: {file_path}, {str(e)}")
        # return None

        # return json_data
    # except json.JSONDecodeError as e:
        # print(f"Error while parsing JSON file: {file_path}")
        # print(f"Error message: {str(e)}")
        # return None
    # with open(file_path, 'r') as file:
        # json_data = json.load(file)
    # return json_data

# def validate_filedate(filaneme: str) -> bool:

# def process_file():
    # fsource=os.path.join(file,f)
    # ftarget=os.path.join(self.params.output,"hello")
    # out=filemove(source=fsource,target=ftarget)
    # return json.dumps(asdict(out))

        

def params_check(pars):
    """ Check that parametrs are valid """
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
        # print("oedea")
        # pars.output=os.path.join(pars.output,"target")
    # if os.listdir(pars.output):
        # logerr.warn(f"directory not empty: {pars.output}")
    return pars


    # def count_files_norecurse():
        # return len(os.listdir(directory))
# def validate_files(directory):
    # for _,_,files in os.listdir(directory)
