#importing installCommandsFunctions.py as a name of icf for accessing function in there easily 
import installCommandsFunctions as icf

print("This python script will require sudo permission to intall tools/apps and do update/upgrade/autoremove/reboot")

guard = input("Do you want to continue Y/N = ")

while(True):
    if (guard == 'y' or guard == 'Y'):
        print("So we will starting right now. \n After the make sure you give me permission, you can grab a coffee!")
        break
    elif(guard == 'n' or guard == 'N'):
        print("It's so sad I could help you, see you later then")
        exit()
    else:
        guard = input("You have to write y/Y or n/N, other things not matter = ")

#There is a lot of functions to install or do something
#Comment or uncomment to do what you want to install 

icf.systemUpdateAndUpgrade()
icf.systemAutoremove()
#icf.installGit()
#icf.installGitKraken()
#icf.installInkscape()
#icf.installSnapd()
#icf.installSnapStore()
#icf.installVim()
#icf.installVlc()
#icf.installZsh()
#icf.installGlimpse()
#icf.installCMake()
#icf.installSpotify()
#icf.installVSCode()
#icf.installTelegram()
#icf.installWhatsapp()
#icf.installSkype()
#icf.installSlack()
#icf.installOctave()
#icf.installExfatFuseUtils()
#icf.installOnlyOffice()
#icf.installBlender()
#icf.installFirefox()
#icf.installOpera()
#icf.installPostman()
#icf.systemReboot()