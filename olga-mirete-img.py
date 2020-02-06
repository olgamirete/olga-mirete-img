from PIL import Image, ImageDraw, ImageFont
from utils.rgb import rgb2hex

mode = 'RGB'
scale = 300
width = scale
height = scale
size = (width, height)
font_path = 'fonts/atwriter.ttf'
font_size_as_percentage_of_height = 0.08
font_size = int(height * font_size_as_percentage_of_height) # 28
font = ImageFont.truetype(font_path, font_size)
min_margin = 0.2
base_color = rgb2hex(200, 100, 0)

im = Image.new(mode, size, base_color)

draw = ImageDraw.Draw(im)

for row in range(height):
    for col in range(width):
        draw.point((row, col), rgb2hex(row*3*100/scale, col*3*100/scale, (row+col)*100/scale))

text_to_draw = 'This is a test.'
text_to_draw = 'This is a longer test that will help see how this is going to be handled.'
draw.text((10, 10), text_to_draw, rgb2hex(255, 255, 255), font)

line_size = font.getsize('hg')
line_size_2 = font.getsize('abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ¿¡?!",.|<>°^*+-~$%&/[()]öäüÖÄÜ_—')

im.show()
# im.save('output/test.png')