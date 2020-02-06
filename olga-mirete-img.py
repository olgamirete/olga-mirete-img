from PIL import Image, ImageDraw, ImageFont

mode = 'RGB'
scale = 300
width = scale
height = scale
size = (width, height)
font_path = 'fonts/atwriter.ttf'
font = ImageFont.truetype(font_path, 28)
min_margin = 0.2
# base_color = '#0000ff'

def rgb2hex(red, green, blue):
    
    # The standard hex(arg) function returns a string with the hex value of the
    # arg, prefixed with '0x'.

    # [2:] is used to get rid of the '0x' prefix.

    # % 256 is used to keep the integer values between 0 and 255, as requested
    # by the rgb pattern.

    # Floats are converted to integers with the standard int() function.

    # If something fails, raise the following error message (with ValueError or
    # TypeError):

    # "The arguments 'red', 'green' and 'blue' in the function rgb2hex() must be
    # either integers or floats.'"

    error_message = "The arguments 'red', 'green' and 'blue' in the function " \
                  + "rgb2hex() must be either integers or floats."

    try:
        hex_value = '#'
        hex_value += hex(int(red) % 256)[2:].zfill(2)
        hex_value += hex(int(green) % 256)[2:].zfill(2)
        hex_value += hex(int(blue) % 256)[2:].zfill(2)
        return hex_value
    except ValueError as err:
        err.args = (error_message,)
        raise
    except TypeError as err:
        err.args = (error_message,)
        raise

base_color = rgb2hex(200, 100, 0)

im = Image.new(mode, size, base_color)

draw = ImageDraw.Draw(im)

for row in range(height):
    for col in range(width):
        draw.point((row, col), rgb2hex(row*3*100/scale, col*3*100/scale, (row+col)*100/scale))

text_to_draw = 'This is a test.'
text_to_draw = 'This is a longer test that will help see how this is going to be handled.'
draw.text((10, 10), text_to_draw, rgb2hex(255, 255, 255), font)

im.show()
# im.save('output/test.png')