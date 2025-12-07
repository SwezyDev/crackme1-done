from memory_patch import patch_mem
from server import start_server
from colorama import Fore
import pymem
import os

def main(): # main func to run the patcher
    os.system("cls") # clear 
    os.system("title DeadOverflow License Patcher") # title
    print(f"{Fore.LIGHTBLACK_EX}https://www.youtube.com/@deadoverflow{Fore.RESET}") # hello dead overflow :)

    pid = input(f"\n[{Fore.YELLOW}?{Fore.RESET}] PID:{Fore.YELLOW} ") # get process via pid input

    print(f"\n{Fore.RESET}[{Fore.CYAN}*{Fore.RESET}] Attaching to process with PID{Fore.CYAN} {pid}{Fore.RESET}...") # log info

    pm = pymem.Pymem() # create a pymem instance
    pm.open_process_from_id(int(pid)) # open the target process by pid
    patched = patch_mem(pm) # call the patching function

    if not patched: # if no patch was made
        print(f"{Fore.RESET}[{Fore.RED}-{Fore.RESET}] Failed to patch Memory") # log fail
        os.system("pause >nul") # pause before exit
        return 
    
    print(f"{Fore.RESET}[{Fore.GREEN}+{Fore.RESET}] Successfully bypassed License Check") # log success

    start_server() # start the fake server
