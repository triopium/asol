import os
import json
import sys
from dataclasses import dataclass, asdict
import logging
from typing import Optional, Any
from . import logger
logerr = logging.getLogger(__name__)
logerr.addHandler(logger.handler_stderr)

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
            fsource=os.path.join(self.params.input,f)
            ftarget=os.path.join(self.params.output,"hello")
            outinfo=filemove(source=fsource,target=ftarget)
            print(json.dumps(asdict(outinfo)))
            output_file(fsource)
            # json_data=parse_json_file(fsource)
            # print(json_data)
            processed+=1

        logerr.info(f"moved {processed} files")
            # logerr.debug(json.dumps(asdict(out)))
            # print(fn)
# def prepare_move_info():


def parse_json_file(file_path: str) ->Optional[Any]:
    try:
        with open(file_path, 'r') as file:
            json_data = json.load(file)
            return json_data
    except Exception as e:
        logerr.error(f"parsing json: {file_path}, {str(e)}")

def output_file(input_file: str) -> str:
    json_data=parse_json_file(input_file)
    print(json_data)

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
