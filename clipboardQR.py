import global_hotkeys as hk
import time
import win32clipboard as clip
from io import BytesIO
import qrcode as qr
import win32con

version = 'v0.3.0'
keepAlive = True

print(f'''clipboardQR ({version}) by Quantlyx
Licence: MIT
DO NOT run more than one instance simultaneously!
------------------------------------------------------------
    - Ctrl + Shift + q: Converts text in clipboard to QRCode
    - Ctrl + Shift + e: Exits Application
    Hotkeys are global.
    ''')

def genQR():
    if clip.IsClipboardFormatAvailable(1) == True:
        clip.OpenClipboard()
        clipInputBinary = clip.GetClipboardData(clip.CF_TEXT)
        clipInputString = clipInputBinary.decode('utf-8')
        
        image = qr.make(clipInputString, box_size = 32)
        output = BytesIO()
        image.convert('RGB').save(output, 'BMP')
        data = output.getvalue()[14:]
        output.close()
        
        clip.EmptyClipboard()
        clip.SetClipboardData(win32con.CF_DIB, data)
        clip.CloseClipboard()
        
        print(f'LOG: QRCode (\'{clipInputString}\') has been copied to clipboard!')
    else:
        print('ERROR: Data in clipboard is NOT text!')

def exitApp():
    global keepAlive
    hk.stop_checking_hotkeys()
    keepAlive = False
    print('\nShutting down...')

hotkeyBindings = [
[['control', 'shift', 'q'], None, genQR],
[['control', 'shift', 'e'], None, exitApp]]
hk.register_hotkeys(hotkeyBindings)
hk.start_checking_hotkeys()

while keepAlive:
    time.sleep(1)