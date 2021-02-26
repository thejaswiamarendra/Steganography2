import os
import random
from PIL import Image

j1=0
z1=0
input_2 = input("\n\n Enter the name of the image with extension")
image=Image.open(os.path.abspath(input_2))
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
    