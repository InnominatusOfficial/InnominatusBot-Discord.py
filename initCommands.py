import yaml
import commandsHandle


class command(object):
    registeredCommands = {}
    def __init__(self, name, permsLevel):
        self.name = name
        self.permsLevel = permsLevel
        with open("config.yml") as ymlIn:
            data = yaml.load(ymlIn)

        if  data["command"] is None:
                data["command"] = {self.name: {"command-level": self.permsLevel}}

        else:
            listDict = []
            listDict.append(data["command"])
            listDict.append({self.name : {"command-level" : self.permsLevel}})
            for i in listDict:
                commandName = ""
                commandDict = ""
                for a in i:
                    commandName = a
                    commandDict = i[a]
                data["command"][commandName] = commandDict


        with open("config.yml", "w") as ymlOut:
            yaml.dump(data, stream=ymlOut, default_flow_style=False, indent=3)

        self.__class__.registeredCommands[self.name] = self

    async def runCommand(self, message, args, client):
        func = getattr(commandsHandle, self.name)
        with open("config.yml") as ymlIn:
            data = yaml.load(ymlIn)
        try:
            userPermissions = data["user"][str(message.author)]["permissionlevel"]
        except:
            userPermissions = 1
        commandLevel = data["command"][self.name]["command-level"]

        if int(commandLevel) <= int(userPermissions):
            await func(message, args, client)

    async def runBypass(self, message, args, client):
        func = getattr(commandsHandle, self.name)
        await func(message, args, client)

def init_commands():
    help = command("help", 1)
    connect = command("connect", 1)
    roll = command("roll", 1)
    ping = command("ping", 1)
    pong = command("pong", 1)
    progress = command("progress", 1)
    verify = command("verify", 2)



