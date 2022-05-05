import global_hotkeys as hk
import time
import win32clipboard as clip
from io import BytesIO
import qrcode
import win32con

def genQR():
    try:
        clip.OpenClipboard()
        clipInput = clip.GetClipboardData(clip.CF_TEXT)
        clip.CloseClipboard()
    except:
        print('Data in clipboard is NOT text!')
    
    image = qrcode.make(clipInput)
    output = BytesIO()
    image.convert('RGB').save(output, 'BMP')
    data = output.getvalue()[14:]
    output.close()
    
    clip.OpenClipboard()
    clip.EmptyClipboard()
    clip.SetClipboardData(win32con.CF_DIB, data)
    clip.CloseClipboard()




keepAlive = True
    
bindings = [
    [["control", "shift", "q"], None, genQR]]

hk.register_hotkeys(bindings)
hk.start_checking_hotkeys()

while keepAlive:
    time.sleep(0.1)