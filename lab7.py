from PIL import Image
from PIL import ImageFilter
from PIL import ImageDraw
from PIL import ImageFont
import os
def z1():
    image=Image.open('smile/smile.jpg')
    image.show()
    print("Размер изображения:" ,image.size)
    print("Формат изображения: ",image.format)
    print("Цветовая модель: ", image.mode)

def z2():
    image=Image.open('smile/smile.jpg')
    image3=image.reduce(3)
    image3.save('smile/small smile.jpg')
    image_flip1=image.transpose(Image.FLIP_LEFT_RIGHT)
    image_flip1.save('smile/vertical smile.jpg')
    image_flip2=image.transpose(Image.FLIP_TOP_BOTTOM)
    image_flip2.save('smile/gorizont smile.jpg')

def z3():
    os.mkdir('new')
    for i in range(1,6):
        image=Image.open(f'{i}.jpg')
        image = image.filter(ImageFilter.EMBOSS)
        image.save(f'new/{i}{i}.jpg')
def z4():
    name=str(input("Введите название изображения: "))
    image=Image.open(f'{name}.jpg')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("ofont.ru_Futurespore.ttf", 100)
    draw.text((0,0),'ZHARKOVA',fill=(0,0,0), font=font)
    image.show()

print("---Задача 1---")
z1()
z2()
z3()
print("---Задача 4---")
z4()