
            # print(json.dumps(asdict(outinfo)))
            # outfile=solve_output_file(fsource)
            # print(f"kex {fsource} {outfile}")
            # logerr.debug(f"dstfile: {outfile}")
            # print(outfile)
            # json_data=parse_json_file(fsource)
            # print(json_data)
            # processed+=1

        # logerr.info(f"moved {processed} files")
            # logerr.debug(json.dumps(asdict(out)))
            # print(fn)
# def prepare_move_info():

# def compare_dates(from_file,from_field) -> int:
    # pass

# def parse_date(date_string: str, format_string: str) -> datetime:
    # parsed_date = datetime.strptime(date_string, format_string)
    # return parsed_date

# def parse_date(date: str):
    # date_string = "2023-05-22"
    # format_string = "%Y-%m-%d"
    # parsed_date = datetime.strptime(date_string, format_string)


# def parse_date(date_string: str) -> datetime:
    # try:
        # format_string = "%Y-%m-%d"
        # parsed_date = datetime.strptime(date_string, format_string)
        # return parsed_date
    # except ValueError:
        # return none

    # def count_files_norecurse():
        # return len(os.listdir(directory))
# def validate_files(directory):
    # for _,_,files in os.listdir(directory)


# def GetPathCmdEnvCwd(dirpath: str) -> str:
    # """
    # Get path from commandlie input, env variable, or current dir. In order of decreasing preference
    # """
    # if dirpath is None or dirpath == "":
        #### from environ
        # dirpath=os.environ.get('SOURCE_DIRECTORY')
        # if dirpath is None or dirpath == "":
            # #### from current dirpath
            # dirpath=os.getcwd()

        # dstdir=os.path.join(dstdir,"target")
    # return os.path.abspath(dirpath)

if os.path.exists(source_path) and not os.path.exists(target_path):
    print(f"Dry run: File '{filename}' will be moved from '{source_dir}' to '{target_dir}'.")
else:
    print(f"Dry run: File '{filename}' cannot be moved to '{target_dir}'.")
