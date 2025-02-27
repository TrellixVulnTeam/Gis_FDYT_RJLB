# -*- coding: utf-8 -*-
import img2pdf
import os


# 房地一体项目组，pdf指定页面插入图片


def from_photo_to_pdf(photo_path):
    """
    pdf插入图片
    :param photo_path:
    :return:
    """
    # 1、生成地址列表
    photo_list = os.listdir(photo_path)
    photo_list = [os.path.join(photo_path, i) for i in photo_list]

    # 1、指定pdf的单页的宽和高
    # A4纸张
    # a4inpt = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
    # 我的自定义：
    a4inpt = (img2pdf.mm_to_pt(720), img2pdf.mm_to_pt(1080))
    layout_fun = img2pdf.get_layout_fun(a4inpt)
    with open(photo_path + '\\1result.pdf', 'wb') as f:
        f.write(img2pdf.convert(photo_list, layout_fun=layout_fun))


if __name__ == '__main__':
    print('作者：wjl，有事致电')
    photo_path = input('请输入pdf所在文件夹x') or r'D:\test'
    from_photo_to_pdf(photo_path)
