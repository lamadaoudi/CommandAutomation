import glob
import os
import shutil
import main
import convert_sizes

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
            self._outputReport += "\nFail: Could not find directory"

    def get_file(self):
        return self.__file

    def execute(self):
        if self.get_finishStatus():
            text_files = glob.glob(self.__path + "/**/" + self.__file, recursive=True)
            self._finishStatus = True
            if len(text_files) != 0:
                self._outputReport += "\nFile was successfully found: "+ str(text_files)
            else:
                self._finishStatus = True
                self._outputReport += "\nCould not find the file in the directory or its subdirectories "

class Mv_lastCommand(Command):
    """This class automates the Mv_last <src_directory> <des_directory>"""
    def __init__(self, source, destination):
        super(Mv_lastCommand, self).__init__()
        self.__set_source(source)
        self.__set_destination(destination)

    def __set_source(self, source):
        if os.path.exists(source) and os.path.isdir(source):
                self.__source = source
        else:
            self._finishStatus = False
            self._outputReport += "\nFail: Could not find source directory"

    def __set_destination(self, destination):
        if os.path.exists(destination) and os.path.isdir(destination):
                self.__destination = destination
        else:
            self._finishStatus = False
            self._outputReport += "\nFail: Could not find destination directory"

    def get_source(self):
        return self.__source

    def get_destination(self):
        return self.__destination

    def execute(self):
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
                    self._outputReport += "Moving "+mostRecentFile+" to"+ self.get_destination()
                    shutil.move(mostRecentFile, self.get_destination())
                except:
                    self._finishStatus=False
                    self._outputReport +="\nFile already exists"
                    return
                self._finishStatus = True
                self._outputReport += "\nSuccessfully moved the most recent file"
            else:
                self._outputReport += "\nNo files were found in source directory"

class CategorizeCommand(Command):
    countDirectory = 0
    def __init__(self, path):
        super(CategorizeCommand, self).__init__()
        self.__set_path(path)

    def __set_path(self, path):
        if os.path.exists(path):
            self.__path = path
        else:
            self._finishStatus = False
            self._outputReport += "\nFail: Could not find directory"

    def get_path(self):
        return self.__path

    def execute(self):
        if self.get_finishStatus():
            CategorizeCommand.countDirectory += 1
            lessPath = os.path.join(self.get_path(), "lessThanThreshold_"+str(CategorizeCommand.countDirectory))
            # When we rerun the script multiple types, this will handle the duplicate names
            while os.path.exists(lessPath):
                CategorizeCommand.countDirectory += 1
                lessPath = os.path.join(self.get_path(), "lessThanThreshold_" + str(CategorizeCommand.countDirectory))
            try:
                os.mkdir(lessPath)
                self._outputReport+="\n %s directory created" %lessPath
                morePath = os.path.join(self.get_path(), "GreaterThanThreshold_" + str(CategorizeCommand.countDirectory))
                os.mkdir(morePath)
                self._outputReport += "\n %s directory created" % morePath
                for fname in os.listdir(self.get_path()):
                    path = os.path.join(self.get_path(), fname)
                    if os.path.isdir(path):
                        continue
                    else:
                        if os.stat((os.path.join(self.get_path(),fname))).st_size < convert_sizes.convert(main.configurations[" Threshold_size "]):
                            shutil.move((os.path.join(self.get_path(), fname)), lessPath)
                            self._outputReport += "\n Moved " + fname + " to " + lessPath
                        else:
                            shutil.move((os.path.join(self.get_path(),fname)), morePath)
                            self._outputReport += "\n Moved " + fname + " to " + morePath
            except OSError:
                self._outputReport += "\nCreation of directory failed"
                self._finishStatus = False
            else:
                self._outputReport += "\nCommand failed"























