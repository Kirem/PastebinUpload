import urllib
import urllib2
from Tkinter import Tk

api_dev_key = "abe718e2cf6219ed10c4714bfd0e0a81"
api_user_key = "2f5aca3524fa22825fee981a6d308bf9"
url = "http://pastebin.com/api/api_post.php"


def uploadCodeAndReturnAddress(postData):
    request = urllib2.urlopen(url, urllib.urlencode(postData))
    response = str(request.read())
    return response


def PreparePasteCode():
    r = Tk()
    r.withdraw()
    code = r.clipboard_get()
    r.destroy()
    return code


def PutAddressIntoClipboard(address):
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(address)
    r.destroy()
    return

paste_code = PreparePasteCode()
postData = {
    'api_option': 'paste',
    'api_dev_key': api_dev_key,
    'api_paste_private': 0,  # paste as public
    'api_paste_expire': '1M',  # paste with 1M expire time
    'api_paste_code': paste_code
}
pastebin_paste_address = uploadCodeAndReturnAddress(postData)
PutAddressIntoClipboard(pastebin_paste_address)
