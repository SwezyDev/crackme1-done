import ctypes

class utils: # utitlity class for memory stuff
    class mem_info(ctypes.Structure): # structure for mem info
        _fields_ = [ # fields of the structure
            ("BaseAddress", ctypes.c_void_p), # starting address of the region
            ("AllocationBase", ctypes.c_void_p), # base address of the allocation
            ("AllocationProtect", ctypes.c_ulong), # protection when the region was allocated
            ("RegionSize", ctypes.c_size_t), # size of the region in bytes
            ("State", ctypes.c_ulong), # state of the region
            ("Protect", ctypes.c_ulong), # current protection of the region
            ("Type", ctypes.c_ulong), # type of the region
        ]

    mem_inf = mem_info() # instance of mem info structure

    virt_query = ctypes.windll.kernel32.VirtualQueryEx # function to query memory information
    readx = {0x02, 0x04, 0x20, 0x40} # set of memory protection constants that allow reading
