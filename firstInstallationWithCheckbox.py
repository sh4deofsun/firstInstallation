#importing installCommandsFunctions.py as a name of icf for accessing function in there easily 
import installCommandsFunctions as icf

#for showing checkbox results
from pprint import pprint

#need for checkbox selection
import inquirer

print("This python script will require sudo permission to intall tools/apps and do update/upgrade/autoremove/reboot")

guard = input("Do you want to continue Y/N = ")

while(True):
    if (guard == 'y' or guard == 'Y'):
        print("So we will starting right now. \n After select the tool/s you want to install and make sure you give me permission, you can grab a coffee!")
        break
    elif(guard == 'n' or guard == 'N'):
        print("It's so sad I could help you, see you later then")
        exit()
    else:
        guard = input("You have to write y/Y or n/N, other things not matter = ")

questions = [
  inquirer.Checkbox('installationList',
                    message="What do you want to install or do?",
                    choices=[
                      'doUpgrade',
                      'doAutoremove',
                      'doReboot',
                      'Vim', 
                      'Git', 
                      'GitKraken', 
                      'VLC', 
                      'Snapstore', 
                      'ZSH',
                      'Inkscape',
                      'Glimpse',
                      'CMake',
                      'Spotify',
                      'VSCode',
                      'Telegram',
                      'Whatsapp',
                      'Skype',
                      'Slack',
                      'GNUOctave',
                      'Exfat',
                      'Onlyoffice',
                      'Blender',
                      'Firefox',
                      'Opera',
                      'Postman'
                      ],
                    ),
]

answers = inquirer.prompt(questions)
pprint(answers)

print(questions)

#icf.updateAndUpgrade()