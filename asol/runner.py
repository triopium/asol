import os


# def ActOnParams(pars):
    # if pars.write:

    # print(pars)

# class Runner:
    # def __init__(self):
        # print("hello_init")
    # def run(self):
        # return "hello"

def count_files_norecurse(directory):
    return len(os.listdir(directory))

# def validate_files(directory):
    # for _,_,files in os.listdri(directory)
class Runner:
    def __init__(self,pars):
        self.params=pars
        files=os.listdir(pars.input)
        self.files=files
        self.filescount=len(files)
    def debug_pars(self):
        print(self.params)
    # def count_files_norecurse():
        # return len(os.listdir(directory))
