from PIL import Image
im = Image.open("car.jpg") 
pix = im.load()
print im.size

x = 0
y = 0
 
print pix[x,y] 
pix[x,y] = (100,100,100,1)