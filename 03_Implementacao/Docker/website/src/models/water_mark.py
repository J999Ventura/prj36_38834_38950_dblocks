from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from . import APP_ROOT, os


FONT_PATH = os.path.join(APP_ROOT, 'static\\fonts\\Magazine.ttf')


def water_mark_image(file, path_to_save):
    photo = Image.open(file)

    # Store image width and height
    w, h = photo.size

    # make the image editable
    drawing = ImageDraw.Draw(photo)
    font = ImageFont.truetype(FONT_PATH, 68)

    # get text width and height
    text = 'Capture'
    text_w, text_h = drawing.textsize(text, font)
    pos = (w-text_w), (h-text_h)-50

    c_text = Image.new('RGB', (text_w, (text_h) ), color='#000000')
    drawing = ImageDraw.Draw(c_text)
    drawing.text((0, 0), text, fill="#ffffff", font=font)
    c_text.putalpha(100)

    photo.paste(c_text, pos, c_text)
    rgb_im = photo.convert('RGB')
    rgb_im.save(path_to_save)
    #photo.save(path_to_save)
