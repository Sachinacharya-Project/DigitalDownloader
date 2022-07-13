# To be able to download private profile, not only you have to be logged in, \
    # but also you have to have followed that private account.

from instaloader import Instaloader
import instaloader
from instaloader.exceptions import LoginRequiredException, ConnectionException, ProfileNotExistsException, PrivateProfileNotFollowedException, BadCredentialsException
from colorama import init, Fore; init(autoreset=True)
from pwinput import pwinput
import os

print(f"{Fore.LIGHTCYAN_EX}Do you want to download videos too? (Y/N): ")
perm = input().lower()

isVideo = False
if perm == "y":
    isVideo = True

while True:
    profile_name = input("Enter username: ")
    if profile_name == "":
        print(f"{Fore.LIGHTRED_EX}Cannot accept empty username")
        continue
    break

with Instaloader(
    download_videos=isVideo, 
    download_video_thumbnails=isVideo, 
    download_geotags=False, 
    download_comments=False, 
    compress_json=False, 
    save_metadata=False,
    download_pictures=True,
) as downloader:
    print()
    print(f"{Fore.LIGHTCYAN_EX}Please ENTER your credentials to login, press ENTER to skip")
    username = input("Enter Username: ")
    password = pwinput("Enter Password: ")
    print()
    
    isCred = True
    if username == "" or password == "":
        print(f"{Fore.CYAN}You have skipped login. You will be able to download only public profiles.")
        isCred = False
    if isCred:
        try:
            downloader.login(username, password)
            print(f"{Fore.LIGHTGREEN_EX}Logged in Successfully")
        except BadCredentialsException:
            print(f"{Fore.LIGHTRED_EX}Credentials received are incorrect.")
            exit()
        except ConnectionException:
            print(f"{Fore.LIGHTMAGENTA_EX}Couldn't connect to Instagram. Please check your internet connection.")
            exit()
    while True:
        isSuccess = False
        try:
            downloader.download_profile(profile_name, profile_pic=True, profile_pic_only=False, fast_update=True)
            isSuccess = True
        except LoginRequiredException:
            print(f"{Fore.LIGHTRED_EX}This Profile is Private, login required")
        except ConnectionException:
            print(f"{Fore.LIGHTRED_EX}Sorry, count not connect to Instagram right now. Please TRY AGAIN LATER.")
        except PrivateProfileNotFollowedException:
            print(f"{Fore.LIGHTRED_EX}You have to follow this profile to download it's pictures.")
        except ProfileNotExistsException:
            print(f"{Fore.LIGHTRED_EX}Sorry, this profile does not exist. Please RECHECK THE USERNAME AND TRY AGAIN LATER.")
        except Exception as e:
            print(f"{Fore.LIGHTRED_EX}Something went wrong. Please try again later.")
        break
    if isSuccess:
        print(f"{Fore.LIGHTGREEN_EX}Download Completed and files are stored in Folder {profile_name}")
    else:
        print(f"{Fore.LIGHTRED_EX}Sorry, could not download the profile {profile_name}")
os.system("del {}\\*.txt".format(profile_name))
os.system("del {}\\id".format(profile_name))