import main
import CommandFactory


class Reader:
    # This input is for a script
    def __init__(self, input_path):
        self.__input_path = input_path
        self.resultDictionary = {}
        self.scriptStatus = True

    def readScript(self):
        file = open(self.__input_path, "r")
        countCommands = 0
        with file as f:
            for line in f:
                if line.strip():
                    countCommands += 1
                    if (countCommands <= int(main.configurations[" Max_commands "])):
                        commandObject = CommandFactory.CommandFactory.create_command(line.rstrip())
                        if not commandObject is None:
                            commandObject.execute()
                            self.resultDictionary[line.rstrip()] = commandObject.get_finishStatus()
                            if commandObject.get_finishStatus() == False:
                                self.scriptStatus = False
                        else:
                            self.resultDictionary[line] = "False because more"
                            self.scriptStatus = False
                    else:
                        self.resultDictionary[line] = "Command not executed. File exceeded maximum commands threshold"
                        self.scriptStatus = False
        file.close()

# object = Reader("C:\\Users\\Main\\Documents\\BZU_LamaDaoudi\\LinuxLab\\Test\\InputScriptPath\\script1.txt")
# object.readScript()
# print(object.resultDictionary)