import os

from PIL import Image   #PIL is the python image library which needs to be preinstalled before you can run this code
import random

chr_ascii={}        #dictionary conatining characters as keys and ascii values as values
ascii_chr={}        #dictionary containing ascii values as keys and characters as values

for i in range(0,256):
    chr_ascii[chr(i)]=i
    ascii_chr[i]=chr(i)
    
    
img=input("Enter the name of the image you want the message to be encoded in, with the extension\n\n")

path=os.path.abspath(img)    #this gives the absolute path of the given file

image=Image.open(path)

height=image.height
width=image.width
print(height,width)


password=input("\n\nEnter security key\n\n")

text=input("\n\nEnter the message you wanna encode\n\n")


p=0
j=0


z=0
text_length=len(text)
random.seed(password)
for i in range(text_length):
    x=random.randint(0,width)
    y=random.randint(0,height)
    RGB=image.getpixel((x,y))
    rgb_mutable=list(RGB)
    rgb_mutable[z]=chr_ascii[text[p]]^chr_ascii[password[j]]
    rgb_tuple=tuple(rgb_mutable)
    image.putpixel((x,y),rgb_tuple)
    
    
    
    
    
    
    
    z=(z+1)%3
    j=(j+1)%len(password)
    p+=1

    
image.show()
#image=image.save("encrypted.jpg")


print("\n\nData hiding in image is successful\n\n")



j1=0
z1=0
do_you_wanna_decrypt = input("\n\nType 'decrypt' if you wanna decrypt\n\n")
if do_you_wanna_decrypt=="decrypt":
    reenter_key=input("\n\nEnter your key\n\n")
    message=''
    random.seed(reenter_key)
    if reenter_key==password:
        for i in range(text_length):
            x1=random.randint(0,width)
            y1=random.randint(0,height)
            RGB2=image.getpixel((x1,y1))
            coded=RGB2[z1]
        
            message+=ascii_chr[coded^chr_ascii[password[j1]]]
            
            
            z1=(z1+1)%3
            j1=(j1+1)%len(password)
        print("\n\nEncrypted text was\n\n",message)
    else:
        print("\n\nkey doesnt match\n\n")