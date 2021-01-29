import json
import convert_sizes
import optparse
import os
import ReadInputPath
from ReadInputPath import *

input_output_dictionary = {}
configurations = {}
# Assumptions:
# The first option (-s) of the option parser is the path of the directory containing the list of scripts to be read and executed
# If the csv option was chosen from the json file, a separate csc file is created for each script. However, if it was log
# one log file is shared among all scripts to show the output
def intialize_parser():
    parser = optparse.OptionParser()
    parser.add_option('-s', dest='scripts_path', type='string', help='Enter the path of the input scripts')
    parser.add_option('-o', dest='output_path', type='string', help='Enter the path of the output files')
    (options, args) = parser.parse_args()
    if options.scripts_path == None:
        print("Error: no input path specified")
        exit(1)
    if options.output_path == None:
        print("Error: no output path specified")
        exit(1)
    if not check_path(options.scripts_path, options.output_path):
        print("The parser option arguments are invalid")
        return False
    else:
        print("Successfully entered input and output paths")
        input_output_dictionary["scripts_path"] = options.scripts_path
        input_output_dictionary["output_path"] = options.output_path
        return input_output_dictionary


def check_path(input_path, output_path):
    if os.path.exists(input_path):
        if not os.path.exists(output_path):
            try:
                os.mkdir(output_path)
                return True
            except OSError:
                return False
        else:
            return True
    else:
        return False


if __name__ == '__main__':
    # Reading the configuration.json file
    jsonFile = open('configuration.json', )
    configurations = json.load(jsonFile)
    try:
        threshold_size = convert_sizes.convert(configurations[" Threshold_size "])
    except AttributeError:
        print("Error in threshold size")
        exit(1)
    dictionary = intialize_parser()
    if not dictionary is None and dictionary:
        readFullPath(dictionary)

jsonFile = open('configuration.json', )
configurations = json.load(jsonFile)
try:
    threshold_size = convert_sizes.convert(configurations[" Threshold_size "])
except AttributeError:
    print("Error in threshold size")
    exit(1)
