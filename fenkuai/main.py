from PIL import Image



img = Image.open("test.png") 

adv = Image.open("uap1-1.png") 
im = img.load()
ad = adv.load()


# 获得某个像素点的 RGB 值，像素点坐标由 [x, y] 指定
for a in range(0,112):
    for b in range(0,112):
        im[2*a,2*b] = ad[a,b] 



img.show()