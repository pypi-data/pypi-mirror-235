import random
from PIL import Image
import os
__version__="1.5.1"
text="hello world"
carac=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","&","é","~",'"',"#","{","}","(",")","[","]","-","è","_","\\","ç","^","à","@","°","+","=","ê","ë","$","£","%","ù","µ","*",",","?",".",";",":","/","!","§"]
class CodeError(Exception):
    pass
class DecodeError(Exception):
    pass
class KeyElementError(Exception):
    pass
class KeyLengthError(Exception):
    pass
class ImageNotFoundError(Exception):
    pass
def generate_key(seed:int=None):
    if seed==None:
        carac=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","&","é","~",'"',"#","{","}","(",")","[","]","-","è","_","\\","ç","^","à","@","°","+","=","ê","ë","$","£","%","ù","µ","*",",","?",".",";",":","/","!","§"]
        random.shuffle(carac)
        key=""
        for i in range(len(carac)):
            key=key+carac[i]
        return key
    else:
        carac=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","&","é","~",'"',"#","{","}","(",")","[","]","-","è","_","\\","ç","^","à","@","°","+","=","ê","ë","$","£","%","ù","µ","*",",","?",".",";",":","/","!","§"]
        random.Random(seed).shuffle(carac)
        key=""
        for i in range(len(carac)):
            key=key+carac[i]
        return key
def code(text:str,key:str):
    newtext=""
    incode={}
    if not type(text)==str:
        raise TypeError("text argument must be a string")
    if not type(key)==str:
        raise TypeError("key argument must be a string")
    keylist=list(key)
    if not len(keylist)==len(carac):
        raise KeyLengthError("the key is not of the expected length.")
    for i in range(len(keylist)):
        if not keylist[i] in carac:
            raise KeyElementError("'"+keylist[i]+"' must not be in the key.")
    for i in range(len(key)):
        incode.update({carac[i]:key[i]})
    incode.update({" ":" "})
    incode.update({"'":"'"})
    for i in range(len(text)):
        if not text[i] in incode:
            raise CodeError("'"+text[i]+"' is not encodable.")
        newtext=newtext+incode[text[i]]
    return newtext
def decode(text:str,key:str):
    newtext=""
    uncode={}
    if not type(text)==str:
        raise TypeError("text argument must be a string")
    if not type(key)==str:
        raise TypeError("key argument must be a string")
    keylist=list(key)
    if not len(keylist)==len(carac):
        raise KeyLengthError("the key is not of the expected length.")
    for i in range(len(keylist)):
        if not keylist[i] in carac:
            raise KeyElementError("'"+keylist[i]+"' must not be in the key.")
    for i in range(len(key)):
        uncode.update({key[i]:carac[i]})
    uncode.update({" ":" "})
    uncode.update({"'":"'"})
    for i in range(len(text)):
        if not text[i] in uncode:
            raise DecodeError("'"+text[i]+"' is not decodable.")
        newtext=newtext+uncode[text[i]]
    return newtext
def get_key_with_img(image:str):
    if os.path.exists(image):
        img=Image.open(image)
        seed=int(img.width)/10*300+int(img.height)/20*600
        return generate_key(seed)
    else:
        raise ImageNotFoundError("'"+image+"' not found.")
if __name__=="__main__":
    keya=get_key_with_img("img.png")
    print(keya)
    icode=code(text,keya)
    print(icode)
    decod=decode(icode,keya)
    print(decod)