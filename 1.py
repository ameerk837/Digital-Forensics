import requests
import tarfile
import hashlib
usb1=open("/dev/sdb",'rb')
output=open('Image','wb')
_size=512
arr1=b'x00'
hashobj=hashlib.sha256()
while arr1:
    arr1=usb1.read(_size)
    output.write(arr1)
    hashobj.update(arr1)
usb1.close()
output.close()
compressedfile=tarfile.open('compressefile','w:gz')
compressedfile.add('Image')
compressedfile.close()
print(hashobj.hexdigest())
url = 'https://eoo3cw0omlzr33t.m.pipedream.net'
final=str(hashobj.hexdigest())
myo = {'Hash': final}

x = requests.post(url, verify=False, json = myo)

print(x.text)
