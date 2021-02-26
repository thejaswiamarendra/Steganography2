import os

from PIL import Image   #PIL is the python image library which needs to be preinstalled before you can run this code
import random

chr_ascii={}        #dictionary conatining characters as keys and ascii values as values
ascii_chr={}        #dictionary containing ascii values as keys and characters as values

for i in range(0,256):
    chr_ascii[chr(i)]=i
    ascii_chr[i]=chr(i)
    
    
img=input("Enter the name of the image you want the message to be encoded in, with the extension\n\n")

input_1=input("Enter the name for the encrypted image(WITHOUT EXTENSION)")
path=os.path.abspath(img)    #this gives the absolute path of the given file

image=Image.open(path)
image.save("_.png")
image1=Image.open(os.path.abspath("_.png"))
height=image1.height
width=image1.width
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
    RGB=image1.getpixel((x,y))
    rgb_mutable=list(RGB)
    print(rgb_mutable)
    rgb_mutable[z]=chr_ascii[text[p]]^chr_ascii[password[j]]
    rgb_tuple=tuple(rgb_mutable)
    image1.putpixel((x,y),rgb_tuple)
    
    
    
    
    
    
    
    z=(z+1)%3
    j=(j+1)%len(password)
    p+=1

    
image1.show()

image1.save(input_1+".png")
#image=image.save("encrypted.jpg")


print("\n\nData hiding in image is successful\n\n")
