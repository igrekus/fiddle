import os
import cv2 as cv
import pandas as pd
import pytesseract


def process_file(filename):
    print('process', filename)
    img = cv.imread(filename)
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    img_meas = img_gray[370:730, 660:990]
    img_stat = img_gray[110:325, 800:1000]

    _, img_meas_norm = cv.threshold(img_meas, 0, 255, cv.THRESH_BINARY)
    _, img_stat_norm = cv.threshold(img_stat, 0, 255, cv.THRESH_BINARY)

    meas = pytesseract.image_to_string(img_meas_norm)
    stat = pytesseract.image_to_string(img_stat_norm)

    meas_tmp = [v for v in meas.split('\n')[19:-1] if v]
    meas_tmp = [v.replace('pm', 'um').replace('°', 'deg').replace('oc', 'DC -').replace('O Hz', '0 Hz').split() for v in meas_tmp]
    meas_tmp = [[float(v[0]) if v[0].isdigit() else v[0], v[1]] for v in meas_tmp]

    meas_head = [
        'red_surf_dist', 'red_horiz_dist', 'red_vert_dist', 'red_angle',
        'green_surf_dist', 'green_horiz_dist', 'green_vert_dist', 'green_angle',
        'white_surf_dist', 'white_horiz_dist', 'white_vert_dist', 'white_angle',
        'spec_period', 'spec_freq', 'spec_rms_amp'
    ]

    meas_head = [f'{h}, {v[1]}' for h, v in zip(meas_head, meas_tmp)]
    meas_tmp = [v for v, _ in meas_tmp]

    stat_tmp = [v for v in stat.split('\n')[11:-2] if v]
    stat_tmp[0] = stat_tmp[0][:-3]
    stat_tmp[2] = stat_tmp[2].replace('pc', 'DC')
    stat_tmp = [float(v) if v != 'DC' else v for v in stat_tmp]

    stat_head = ['L, um', 'RMS, nm', 'lc, -', 'Ra(lc), nm', 'Rmax, nm', 'Rz, nm', 'Rz cnt', 'Radius, nm', 'sigma, nm']

    meas_tmp = [filename] + meas_tmp + stat_tmp
    meas_head = ['file'] + meas_head + stat_head
    return meas_head, meas_tmp


path = r'D:\work\python\grating_measure\screen_data'

data = []
head = []
for file in os.listdir(path):
    head, row = process_file(f'{path}\\{file}')
    data.append(row)

df = pd.DataFrame(data, columns=head)
df.to_excel('cvd.xlsx')

# cv.imshow('image', img_meas_norm)
# cv.imshow('image', img_stat_norm)
# k = cv.waitKey(0)
