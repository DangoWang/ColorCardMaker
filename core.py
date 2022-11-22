# -*- coding: UTF-8 -*-
import sys
import os

from PIL import ImageDraw, Image, ImageFont

'''
{'upper': '#5500ff', 'common': ['#aaaaff', '#55aa7f'], 'down': '#000000', 
'size': (60, 60, 10), 'path': 'D:', 'outline': True,
'font_size': 10,
'font_distance':0.3
}
'''

cwd = ''
if hasattr(sys, "_MEIPASS"):
    cwd = sys._MEIPASS
else:
    cwd = os.path.dirname(os.path.abspath(__file__))


def make_card(size_info, color):
    w, h = [int(size_info[0]), int(size_info[1])]
    image = Image.new('RGBA', (w, h), color)
    return image

#
# def draw_label(img, color):
#     # 创建可绘制的对象
#     draw = ImageDraw.Draw(img)
#     width, height = img.size
#     # 设置字体，将字体库复制到当前目录
#     font = ImageFont.truetype('simhei.ttf', int(width/4))
#     # 填充文字
#     draw.text((0, height/2.5), color, font=font, fill='#000000')
#     return img


def draw_outlines(img, color, width_info):
    # img = Image.open(pic)
    draw = ImageDraw.Draw(img)
    width, height = img.size
    draw.rectangle((0, 0, width-1, height-1), fill=None, outline=color, width=width_info)
    return img


def combine_color_card(info):
    upper, common, down, size, path, font_color, outline, font_size, font_distance = [info.get('upper'), info.get('common'),
                                       info.get('down'), info.get('size'), info.get('path'), info.get('font_color'),
                                       info.get('outline'), info.get('font_size'), info.get('font_distance')]
    if not outline:
        upper, down = ['', '']
    cw, ch, lw = [int(size[0]), int(size[1]), int(size[2])]
    # 生成一张空白图
    # 如果有描边：
    if down:
        final_img = make_card((cw*4, ch*(len(common) + 0.5)-lw*(len(common)-1)), None)
    else:
        final_img = make_card((cw * 4, ch * (len(common) + 0.5)), None)
    # final_img = make_card((1000, 1000), None)
    # 上面的小色块
    upper_card = make_card((cw/2, ch/2), upper) if upper else Image.open(cwd + '/icons/cross.jpg')
    upper_card = upper_card.resize((int(cw/2), int(ch/2)))
    upper_card = upper_card if not down else draw_outlines(upper_card, down, lw)
    # 下面的小色块
    down_card = make_card((cw/2, ch/2), down) if down else Image.open(cwd + '/icons/cross.jpg')
    down_card = down_card.resize((int(cw/2), int(ch/2)))
    common_cards = []
    if common:
        for i, each_common in enumerate(common):
            c_c = make_card((cw, ch), each_common)
            c_c = c_c if not down else draw_outlines(c_c, down, lw)
            common_cards.append(c_c)
    # 把中间的色块粘贴在一起
    # new_card = common_cards[0]
    label_height_info_common = []
    label_height_info = []  # 这个是字的高度信息
    for i, cc in enumerate(common_cards):
        if down:
            # 如果有描边
            card_height = ch*i-lw*i if i > 0 else 0
        else:
            # 如果没描边
            card_height = ch*i if i > 0 else 0
        final_img.paste(cc, (0, card_height + int(ch/4)))
        label_height_info_common.append(card_height + int(ch / 4))
    # 把上下的色块粘贴进来
    if outline:
        final_img.paste(upper_card, (int(cw*0.75), 0))
    label_height_info.append(ch/20)
    label_height_info.extend(label_height_info_common)
    # 粘贴下面小色块的时候需要判断是不是有边框
    if not down:
        x, y = [int(cw*0.75), len(common_cards)*ch]
    else:
        x, y = [int(cw * 0.75), len(common_cards) * ch - (len(common_cards) - 1) * lw]
    label_height_info.append(y)
    if outline:
        final_img.paste(down_card, (x, y))
    # 加上色码
    all_color_codes = [upper] + common + [down]# list(filter(lambda l: l != '', [upper] + common + [down]))
    blank_text_card = make_card(final_img.size, None)
    draw = ImageDraw.Draw(blank_text_card)
    font = ImageFont.truetype('simhei.ttf', font_size)
    # 填充文字
    single_label_height = int(blank_text_card.height / (len(all_color_codes) + 1))
    fc = '#ffffff' if font_color == u'㿟' else '#000000'
    min_height, *_, max_height = label_height_info
    average_height = (max_height - min_height) / (len(label_height_info)-1)
    for i, text in enumerate(all_color_codes):
        draw.text((0, min_height + average_height*i), text, font=font, fill=fc)
    final_img.paste(blank_text_card, (int(cw*(font_distance + 1)), 0))
    # 转成psd对象
    return final_img


if __name__ == '__main__':
    # img = Image.open('save.png')
    img = make_card((50, 50), None)
    img = draw_outlines(img, '#000000', 5)
    # img = draw_label(img, '#000000')
    img.save('D:\\save1.png')
    pass

