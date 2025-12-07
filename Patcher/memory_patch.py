from memory_utils import utils
from config import REAL, FAKE
from colorama import Fore
import ctypes

addy = 0 # starting address for memory scanning

def patch_mem(pm): # func to patch the target process memory
    global addy # use the global address variable

    while addy < 0x7FFFFFFFFFFF: # loop until the maximum user-mode address
        result = utils.virt_query( # query memory information for the current address
            pm.process_handle, # handle to the target process
            ctypes.c_void_p(addy), # address to query
            ctypes.byref(utils.mem_inf), # pointer to the MEMORY_BASIC_INFORMATION structure
            ctypes.sizeof(utils.mem_inf) # size of the structure
        )

        if not result: # if the query fails, move to the next page
            addy += 0x1000 # move to the next memory page
            continue # continue to the next iteration

        if utils.mem_inf.State == 0x1000 and utils.mem_inf.Protect in utils.readx: # if the region is committed and readable
            try: # attempt to read and patch the memory region
                data = pm.read_bytes(addy, utils.mem_inf.RegionSize) # read the memory region
                i = data.find(REAL) # search for the real url in the data
                if i != -1: # found lets gooooo xD
                    wanted = addy + i # calc the target address
                    pm.write_bytes(wanted, FAKE, len(FAKE)) # write the fake url to the target address
                    print(f"{Fore.RESET}[{Fore.GREEN}+{Fore.RESET}] Patched at {Fore.GREEN}{hex(wanted)}{Fore.RESET}") # log success
                    return True # exit after patching

            except: # handle any exceptions during memory r/w
                pass # ignore errors and continue

        addy += utils.mem_inf.RegionSize # move to the next memory region