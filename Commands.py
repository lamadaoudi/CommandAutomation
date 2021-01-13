import glob
import os
import shutil
import operator

# we can do a super class at the end

class Command:
    def __init__(self):
        self._finishStatus = True
        self._outputReport = ""

    def get_finishStatus(self):
        return self._finishStatus

    def get_outputReport(self):
        return self._outputReport


class GrepCommand(Command):
    """This class automates the Grep <file> <directory> command"""

    def __init__(self, file, path):
        super(GrepCommand, self).__init__()
        self.__set_path(path)
        self.__file = file

    def get_path(self):
        return self.__path

    def __set_path(self, path):
        if os.path.exists(path):
            self.__path = path
        else:
            self._finishStatus = False
            self._outputReport = "Fail: Could not find directory"

    def get_file(self):
        return self.__file

    def executeGrep(self):
        if self.get_finishStatus():
            text_files = glob.glob(self.__path + "/**/" + self.__file, recursive=True)
            self._finishStatus = True
            if len(text_files) != 0:
                self._outputReport = "File was successfully found: "+ str(text_files)
            else:
                self._outputReport = "Could not find the file in the directory or its subdirectories "

class Mv_lastCommand(Command):
    """This class automates the Mv_last <src_directory> <des_directory>"""
    def __init__(self, source, destination):
        super(Mv_lastCommand, self).__init__()
        self.__set_source(source)
        self.__set_destination(destination)

    def __set_source(self, source):
        if os.path.exists(source) :
            self.__source = source
        else:
            self._finishStatus = False
            self._outputReport = "Fail: Could not find directory"

    def __set_destination(self, destination):
        if os.path.exists(destination):
            self.__destination = destination
        else:
            self._finishStatus = False
            self._outputReport = "Fail: Could not find directory"

    def get_source(self):
        return self.__source

    def get_destination(self):
        return self.__destination


    def executeMv_last(self):
        if self.get_finishStatus():
            time_of_files = []
            for fname in os.listdir(self.get_source()):
                path = os.path.join(self.get_source(), fname)
                if os.path.isdir(path):
                    continue
                else:
                    time = os.path.getctime(os.path.join(self.get_source(), fname))
                    time_of_files.append(os.path.join(self.get_source(), fname))
            if len(time_of_files) != 0:
                time_of_files.sort(key=os.path.getctime, reverse=True)
                mostRecentFile = time_of_files[0]
                try:
                    shutil.move(mostRecentFile, self.get_destination())
                except:
                    self._finishStatus=False
                    self._outputReport="File already exists"
                    return
                self._finishStatus = True
                self._outputReport = "Successfully moved the most recent file"
            else:
                self._outputReport = "No files were found in source directory"

class CategorizeCommand(Command):
    def __init__(self,path):
        super(CategorizeCommand, self).__init__()
        self.__set_path(path)

    def __set_path(self, path):
        if os.path.exists(path):
            self.__path = path
        else:
            self._finishStatus = False
            self._outputReport = "Fail: Could not find directory"

    def get_path(self):
        return self.__path

#THIS WILL CAUSE EXCEPTION FOR MULTIPLE SCRIPTS
    def executeCategorize(self):
        if self.get_finishStatus():
            directory_files = []
            for fname in os.listdir(self.get_path()):
                path = os.path.join(self.get_path(), fname)
                if os.path.isdir(path):
                    continue
                else:
                    time = os.path.getctime(os.path.join(self.get_path(), fname))
                    directory_files.append(os.path.join(self.get_path(), fname))
            if len(directory_files) != 0:
                lessPath = os.path.join(self.get_path(), "lessThanThreshold")
                os.mkdir(lessPath)
                morePath = os.path.join(self.get_path(), "GreaterThanThreshold")
                os.mkdir(morePath)
                for file in directory_files:
                    print(os.stat(file).st_size)
                    if os.stat(file).st_size < 5:
                        shutil.move(file, lessPath)
                    else:
                        shutil.move(file, morePath)






















