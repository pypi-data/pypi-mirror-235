import logging
import os
from datetime import datetime

import cv2
from quickverifyimg.log.logger import get_logger

logger = get_logger(__name__)


def corp_margin_row(img, sum_thr=600):
    """
    上下切割 计算同一行像素的颜色强度，小于sum_thr 的判断为有效内容，
    :param img:
    :param sum_thr:
    :return:
    """
    img2 = img.sum(axis=2)
    (row, col) = img2.shape
    row_top = 0
    raw_down = 0
    row_top_first = False
    raw_down_first = False

    for r in range(0, row):
        if img2.sum(axis=1)[r] < sum_thr * col:
            row_top = r
            if row_top_first:
                break
                continue
        # 当出现白色后才进行下一行检测
        row_top_first = True

    for r in range(row - 1, 0, -1):
        if img2.sum(axis=1)[r] < sum_thr * col:
            raw_down = r
            if raw_down_first:
                break
            else:
                continue
        # 当出现白色后才进行下一行检测
        raw_down_first = True
    if row_top < raw_down:
        new_img = img[row_top:raw_down, 0:col, 0:3]
    else:
        new_img = img
    return new_img


def corp_margin_col(img, sum_thr=600):
    """
    左右切割 计算同一列像素的颜色强度，小于sum_thr 的判断为有效内容，
    :param img:
    :param sum_thr:
    :return:
    """
    img2 = img.sum(axis=2)
    col_top = 0
    col_down = 0
    (row, col) = img2.shape
    col_top_first = False
    col_down_first = False
    for c in range(0, col):
        if img2.sum(axis=0)[c] < sum_thr * row:
            col_top = c
            if col_top_first:
                break
            else:
                continue
        # 当出现白色后才进行下一列检测
        col_top_first = True

    for c in range(col - 1, 0, -1):
        if img2.sum(axis=0)[c] < sum_thr * row:
            col_down = c
            if col_down_first:
                break
            else:
                continue
        col_down_first = True

    if col_top < col_down:
        new_img = img[0:row, col_top:col_down, 0:3]
    else:
        new_img = img
    return new_img


def resize_img(img1, img2):
    # 确保两张图像大小一致
    h = min(img1.shape[0], img2.shape[0])
    w = min(img1.shape[1], img2.shape[1])
    # img1 = img1[0:h, 0:w]
    # img2 = img2[0:h, 0:w]
    # 调整图像尺寸为相同的形状
    img1 = cv2.resize(img1, (w, h))
    img2 = cv2.resize(img2, (w, h))
    return img1, img2


def get_auto_crop_image(img1, img2, col_sum_thr=600, row_sum_thr=600):
    start_time = datetime.now()
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

    toRGB_time = datetime.now()
    logger.debug(f'转RGB耗时：{toRGB_time - start_time}')

    img_re1 = corp_margin_row(img1, sum_thr=row_sum_thr)
    img_re1 = corp_margin_col(img_re1, sum_thr=col_sum_thr)
    crop_time1 = datetime.now()
    logger.debug(f'裁剪耗时：{crop_time1 - toRGB_time}')
    img_re2 = corp_margin_row(img2, sum_thr=row_sum_thr)
    img_re2 = corp_margin_col(img_re2, sum_thr=col_sum_thr)

    crop_time = datetime.now()
    logger.debug(f'裁剪耗时：{crop_time - crop_time1}')

    img_re1, img_re2 = resize_img(img_re1, img_re2)

    resize_time = datetime.now()
    logger.debug(f'缩放耗时：{resize_time - crop_time}')
    logger.debug(f'总耗时：{resize_time - start_time}')
    return img_re1, img_re2


if __name__ == '__main__':
    from tests import TEST_PATH

    # img1 = cv2.imread(os.path.join(TEST_PATH, "images", "cat修改1697183575", "1.png"))  # queryImage
    # img1 = cv2.imread('E:\python_project\quickverifyimg\\tests\images\cat修改1697183575\\1.png')
    # img2 = cv2.imread(os.path.join(TEST_PATH, "images", "cat修改1697183575", "2.png"))  # trainImage
    logger.setLevel(logging.DEBUG)
    img1 = cv2.imread('1.png')  # queryImage
    img2 = cv2.imread('2.png')  # trainImage
    img_re1, img_re2 = get_auto_crop_image(img1, img2)

    crop_time = datetime.now()
    cv2.imwrite('result.png', cv2.cvtColor(img_re1, cv2.COLOR_BGR2RGB))
    cv2.imwrite('result2.png', cv2.cvtColor(img_re2, cv2.COLOR_BGR2RGB))
    resize_time = datetime.now()
    logger.debug(f'写入耗时：{resize_time - crop_time}')
    # import math
    # print(math.ceil(0.1 / 30))
