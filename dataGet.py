import csv
import yaml

def csvRead(csvFile):
    with open(csvFile, 'r', newline ='') as fp:
        reader = csv.reader(fp, delimiter=',', quotechar='"')
        # next(reader, None)  # skip the headers
        data_read = [row for row in reader]
        return data_read

def ymlLoad(ymlFile):
    with open(ymlFile, 'r') as f:
        return yaml.load(f)

def hasPermission(user, command):
    config = ymlLoad('config.yml')
    try:
        userPermissions = config["user"][str(user)]["permissionlevel"]
    except:
        userPermissions = 1
        
    commandLevel = config["command"]["commandlevel"][str(command)]
    if commandLevel <= userPermissions:
        print("True")
        return True
    else:
        print("False")
        return False
