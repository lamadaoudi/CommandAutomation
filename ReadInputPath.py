import main
import os
import ReadScripts
import logging
import csv
import glob
from main import *
import main

def writeOutput(fname, status, passedPath, failedPath):
    option = main.configurations[" output "]
    counter = 0
    if status:
        filename = os.path.join(passedPath, fname) + "_Output_Passed"
    else:
        filename = os.path.join(failedPath, fname) + "_Output_Failed"
    if option.strip() == "log":
        temp=filename
        filename = filename + "_" + str(counter) + ".log"
        while os.path.exists(filename):
            counter += 1
            filename = temp + "_" + str(counter) + ".log"
    elif option.strip() == "csv":
        temp=filename
        filename = filename + "_" + str(counter) + ".csv"
        while os.path.exists(filename):
            counter += 1
            filename = temp + "_" + str(counter) + ".csv"
    return filename


def checkThreshold(path):
    logCounter = len(glob.glob1(path, "*.log"))
    csvCounter = len(glob.glob1(path, "*.csv"))
    totalLogFiles = logCounter + csvCounter
    if totalLogFiles >= int(main.configurations[" Max_log_files "]):
        deleteOldest(path)

def deleteOldest(path):
    time_of_files = []
    for fname in os.listdir(path):
        fpath = os.path.join(path, fname)
        if os.path.isdir(fpath):
            continue
        else:
            if fname.endswith(".log") or fname.endswith(".csv"):
                time_of_files.append(os.path.join(path, fname))
    if len(time_of_files) != 0:
        time_of_files.sort(key=os.path.getctime, reverse=False)
        oldestFile = time_of_files[0]
        try:
            os.remove(os.path.join(path, oldestFile))
        except OSError:
            print("Error in deleting the oldest log file")


def readFullPath(input_output_dictionary):
    countDirectories = 0
    inputPath = input_output_dictionary["scripts_path"]
    if main.configurations[" Same_dir "] == "True":
        passedPath = input_output_dictionary["output_path"]
        failedPath = input_output_dictionary["output_path"]
    else:
        passedPath = os.path.join(input_output_dictionary["output_path"], "Passed_" + str(countDirectories))
        while os.path.exists(passedPath):
            countDirectories += 1
            passedPath = os.path.join(input_output_dictionary["output_path"], "Passed_" + str(countDirectories))
        try:
            os.mkdir(passedPath)
            failedPath = os.path.join(input_output_dictionary["output_path"], "Failed_" + str(countDirectories))
            os.mkdir(failedPath)
        except OSError:
            print("Cannot create a separate directory")
    for fname in os.listdir(inputPath):
        path = os.path.join(inputPath, fname)
        if os.path.isdir(path):
            continue
        else:
            if os.path.join(inputPath, fname).lower().endswith("txt"):
                reader = ReadScripts.Reader(os.path.join(inputPath, fname))
                reader.readScript()
                file=writeOutput(fname, reader.scriptStatus, passedPath, failedPath)
                if (file.endswith("log")):
                    checkThreshold(passedPath)
                    checkThreshold(failedPath)
                    print(file)
                    logging.basicConfig(level=logging.DEBUG, filename=file)
                    for item in reader.resultDictionary:
                        string = "Command: " + str(item) + "\n          Output: " + str(reader.resultDictionary[item])
                        logging.info(string)
                elif (file.endswith("csv")):
                    checkThreshold(passedPath)
                    checkThreshold(failedPath)
                    a_file = open(file, "w")
                    writer = csv.writer(a_file)
                    for key, value in reader.resultDictionary.items():
                        writer.writerow([key, value])
                    a_file.close()


