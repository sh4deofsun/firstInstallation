#importing installCommandsFunctions.py as a name of icf for accessing function in there easily 
import installCommandsFunctions as icf

#for showing checkbox results
#from pprint import pprint

#need for checkbox selection
import inquirer

#just for to sleep method
import time

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
                      'Postman',
                      'doReboot'
                      ],
                    ),
]

answers = inquirer.prompt(questions)
#pprint(answers)

for elementOfList in answers['installationList']:
  if elementOfList == 'doUpgrade':
    icf.systemUpdateAndUpgrade()
  elif elementOfList == 'doAutoremove':
    icf.systemAutoremove()
  elif elementOfList == 'doReboot':
    icf.systemReboot()
  elif elementOfList == 'Vim':
    icf.installVim()
  elif elementOfList == 'Git':
    icf.installGit()
  elif elementOfList == 'GitKraken':
    icf.installGitKraken()
  elif elementOfList == 'VLC':
    icf.installVlc()
  elif elementOfList == 'Snapstore':
    icf.installSnapd()
    icf.installSnapStore()
  elif elementOfList == 'ZSH':
    icf.installZsh()
  elif elementOfList == 'Inkscape':
    icf.installInkscape()
  elif elementOfList == 'Glimpse':
    icf.installGlimpse()
  elif elementOfList == 'CMake':
    icf.installCMake()
  elif elementOfList == 'Spotify':
    icf.installSpotify()
  elif elementOfList == 'VSCode':
    icf.installVSCode()
  elif elementOfList == 'Telegram':
    icf.installTelegram()
  elif elementOfList == 'Whatsapp':
    icf.installWhatsapp()
  elif elementOfList == 'Skype':
    icf.installSkype()
  elif elementOfList == 'Slack':
    icf.installSlack()
  elif elementOfList == 'GNUOctave':
    icf.installOctave()
  elif elementOfList == 'Exfat':
    icf.installExfatFuseUtils()
  elif elementOfList == 'Onlyoffice':
    icf.installOnlyOffice()
  elif elementOfList == 'Blender':
    icf.installBlender()
  elif elementOfList == 'Firefox':
    icf.installFirefox()
  elif elementOfList == 'Opera':
    icf.installOpera()
  elif elementOfList == 'Postman':
    icf.installPostman()


print("Well then it is over... I installed all of your stuff or at least try. \n One more thing before i go.")
print("I suggest to reboot your computer, cause some tools/apps may need this")

guard2 = input("Will you take my advice y/n = ")

while(True):
    if (guard2 == 'y' or guard2 == 'Y'):
        print("Thank you for that. I will do it for you, get ready for action in \n5..")
        time.sleep(1)
        print("4..")
        time.sleep(1)
        print("3..")
        print("...Bravo six going dark...")
        time.sleep(2)
        icf.systemReboot()
        exit()
    elif(guard2 == 'n' or guard2 == 'N'):
        print("Okey then, see you later ")
        exit()
    else:
        guard2 = input("You have to write y/Y or n/N, other things not matter = ")