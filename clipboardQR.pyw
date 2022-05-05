import global_hotkeys as hk
import time
keepAlive = True

def print_hello():
    print("Hello")
    
bindings = [
    [["control", "shift", "7"], None, print_hello]]

hk.register_hotkeys(bindings)
hk.start_checking_hotkeys()

while keepAlive:
    time.sleep(0.1)