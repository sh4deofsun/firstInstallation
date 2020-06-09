import os

#Update, Upgrade, Autoremove, Reboot
def systemUpdateAndUpgrade():
    os.system('sudo apt-get update')
    os.system('sudo apt full-upgrade -y')

def systemAutoremove():
    os.system('sudo apt autoremove -y')

def systemReboot():
    os.system('reboot')

#Git
def installGit():
    os.system('sudo apt-get install git')

#Vim
def installVim():
    os.system('sudo apt-get install vim')

#Snapstore
def installSnapd():
    print("After this installation may require restart")
    os.system('sudo apt install snapd')
def installSnapStore():
    os.system('sudo snap install snap-store')

#GitKraken
def installGitKraken():
    os.system('sudo snap install gitkraken --classic')

#Zsh
def installZsh():
    os.system('sudo apt-get install zsh')
    os.system('sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)" ')

#VLC
def installVlc():
    os.system('sudo snap install vlc')

#Inkscape
def installInkscape():
    os.system('sudo snap install inkscape')

#Glimpse
def installGlimpse():
    os.system('sudo snap install glimpse-editor')

#Cmake
def installCMake():
    os.system('sudo snap install cmake --classic')

#Spotify
def installSpotify():
    os.system('sudo snap install spotify')

#VScode
def installVSCode():
    os.system('sudo snap install code --classic')

#Telegram
def installTelegram():
    os.system('sudo snap install telegram-desktop')

#Whatsapp
def installWhatsapp():
    os.system('sudo snap install whatsdesk')

#Skype
def installSkype():
    os.system('sudo snap install skype --classic')

#Slack
def installSlack():
    os.system('sudo snap install slack --classic')

#GNU Octave
def installOctave():
    os.system('sudo snap install octave')

#Exfat fuse, Exfat utils
def installExfatFuseUtils():
    os.system('sudo add-apt-repository universe')
    os.system('sudo apt update')
    os.system('sudo apt install exfat-fuse exfat-utils')

#OnlyOffice
def installOnlyOffice():
    os.system('sudo snap install onlyoffice-desktopeditors')

#Blender
def installBlender():
    os.system('sudo snap install blender --classic')

#Firefox
def installFirefox():
    os.system('sudo snap install firefox')

#Opera
def installOpera():
    os.system('sudo snap install opera')

#Postman
def installPostman():
    os.system('sudo snap install postman')