from Commands import *
import shlex


class CommandFactory:

    @staticmethod
    def indicateCommand(line):
        commandParameters = shlex.split(line)
        argumentsList = []
        try:
            if commandParameters[0] == "Grep" or commandParameters[0] == "Mv_last":
                argumentsList.append(commandParameters[0])
                if (not commandParameters[1] is None) and (not commandParameters[2] is None) and (len(commandParameters) == 3):
                    argumentsList.append(commandParameters[1])
                    argumentsList.append(commandParameters[2])
                else:
                    argumentsList = None
            elif commandParameters[0] == "Categorize":
                argumentsList.append(commandParameters[0])
                if (not commandParameters[1] is None) and (len(commandParameters) == 2):
                    argumentsList.append(commandParameters[1])
                else:
                    argumentsList = None
            else:
                argumentsList = None
            return argumentsList
        except IndexError:
            return None

    @staticmethod
    def create_command(line):
        arguments = CommandFactory.indicateCommand(line)
        if not arguments is None:
            if arguments[0] == 'Grep':
                return GrepCommand(arguments[1], arguments[2])
            elif arguments[0] == 'Mv_last':
                return Mv_lastCommand(arguments[1], arguments[2])
            elif arguments[0] == 'Categorize':
                return CategorizeCommand(arguments[1])
        else:
            return None

# object = CommandFactory.create_command("Mv_last C:\\Users\\Main\\Documents\\BZU_LamaDaoudi\\LinuxLab\\Resources.txt C:\\Users\\Main\\Documents\\BZU_LamaDaoudi\\LinuxLab\\Test\\Source\\lama.txt")
# object.execute()
# print(type(object))
# print((object.get_finishStatus()))
# print(object.get_outputReport())
