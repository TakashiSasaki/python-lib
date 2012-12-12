import uuid

if __name__ == "__main__":
    try:
        print("netbios", hex(uuid._netbios_getnode()))
    except ImportError:
        pass
    print("windll", hex(uuid._windll_getnode()))
    #print(hex(uuid._random_getnode()))
    print("ipconfig", hex(uuid._ipconfig_getnode()))
