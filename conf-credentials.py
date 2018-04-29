from argparse import ArgumentParser
from os import path
from settings.utils import find_ext_file
from settings.settings import APP_PATH
from shutil import copyfile
import re


# This file is to configure all the credentials in our project
if __name__ == "__main__":
    terminal_parser = ArgumentParser()
    terminal_parser.add_argument(
        '--json',
        '-j',
        required=True,
        nargs=1,
        help='Json file save credentials to connect to the google API',
        dest="json"
    )
    terminal_parser.add_argument(
        '--mainini',
        '-m',
        required=True,
        nargs=1,
        help='File main.ini where are the main credentials'
    )
    args = terminal_parser.parse_args()

    if path.exists(args.json[0]):
        list_json = find_ext_file("json", APP_PATH + "/config")
        if len(list_json) > 0:
            print(".json file already in")
        else:
            # https: // github.com / RnnySqrl / ETL - IM
            result = re.match(r"^(.+)\/([^\/]+)$", args.json[0])
            json_name = result.group(2)
            copyfile(args.json[0], "{0}/config/{1}".format(
                APP_PATH, json_name
            ))
    else:
        print("Directory .json not valid")
    if path.exists(args.mainini[0]):
        list_main_ini = find_ext_file("ini", APP_PATH + "/config")
        if len(list_main_ini) > 0:
            print(".ini already in")
        else:
            copyfile(args.mainini[0], "{0}/config/main.ini".format(APP_PATH))
    else:
        print("Directory main.ini not valid")
