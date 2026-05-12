import os
import shutil
############################designed for yolov5 train#############################
path = './1' #存放数据集文件夹，包含images（jpg＆png）labels（txt＆xml）
result = os.listdir(path)
train_file = './data' #更改为你的数据集名称
ratio = 2/3 #训练集占数据集的比例
if not os.path.exists(train_file):
    os.mkdir(train_file)

if not os.path.exists(train_file + '/train'):
    os.mkdir(train_file + '/train')
if not os.path.exists(train_file + '/train/images'):
    os.mkdir(train_file + '/train/images')
if not os.path.exists(train_file + '/train/labels'):
    os.mkdir(train_file + '/train/labels')

if not os.path.exists(train_file + '/valid'):
    os.mkdir(train_file + '/valid')
if not os.path.exists(train_file + '/valid/images'):
    os.mkdir(train_file + '/valid/images')
if not os.path.exists(train_file + '/valid/labels'):
    os.mkdir(train_file + '/valid/labels')

if not os.path.exists(train_file + '/test'):
    os.mkdir(train_file + '/test')
if not os.path.exists(train_file + '/test/images'):
    os.mkdir(train_file + '/test/images')
if not os.path.exists(train_file + '/test/labels'):
    os.mkdir(train_file + '/test/labels')

jpg,png,txt,xml =[],[],[],[]

try:
    for i in result:
        if i[-3:] == 'jpg':
            jpg.append(i[:-4])
        if i[-3:] == 'png':
            png.append(i[:-4])
        if i[-3:] == 'txt':
            txt.append(i[:-4])
        if i[-3:] == 'xml':
            xml.append(i[:-4])

    if len(txt) >= len(xml):
        xml = []
    else:
        txt = []

    if len(jpg) >= len(png):
        png = []
    else:
        jpg = []
except:
    print(path + '是个空文件夹')

if jpg != []:
    train_num = 0
    for i in jpg:
        train_num += 1
        if (i in txt or i in xml) and train_num <= int(len(jpg)*ratio):
            shutil.copyfile(path + '/' + i + '.jpg', train_file + '/train/images/' + i + '.jpg')
            try:
                shutil.copyfile(path + '/' + i + '.txt', train_file + '/train/labels/' + i + '.txt')
            except:
                pass
            try:
                shutil.copyfile(path + '/' + i + '.xml', train_file + '/train/labels/' + i + '.xml')
            except:
                pass
        if (i in txt or i in xml) and train_num > int(len(jpg)*ratio):
            shutil.copyfile(path + '/' + i + '.jpg', train_file + '/valid/images/' + i + '.jpg')
            try:
                shutil.copyfile(path + '/' + i + '.txt', train_file + '/valid/labels/' + i + '.txt')
                shutil.copyfile(path + '/' + i + '.txt', train_file + '/test/labels/' + i + '.txt')
            except:
                pass
            try:
                shutil.copyfile(path + '/' + i + '.xml', train_file + '/valid/labels/' + i + '.xml')
                shutil.copyfile(path + '/' + i + '.xml', train_file + '/test/labels/' + i + '.xml')
            except:
                pass

if png != []:
    train_num = 0
    for i in png:
        train_num += 1
        if (i in txt or i in xml) and train_num <= int(len(png)*ratio):
            shutil.copyfile(path + '/' + i + '.png', train_file + '/train/images/' + i + '.png')
            try:
                shutil.copyfile(path + '/' + i + '.txt', train_file + '/train/labels/' + i + '.txt')
            except:
                pass
            try:
                shutil.copyfile(path + '/' + i + '.xml', train_file + '/train/labels/' + i + '.xml')
            except:
                pass
        if (i in txt or i in xml) and train_num > int(len(png)*ratio):
            shutil.copyfile(path + '/' + i + '.png', train_file + '/valid/images/' + i + '.png')
            try:
                shutil.copyfile(path + '/' + i + '.txt', train_file + '/valid/labels/' + i + '.txt')
                shutil.copyfile(path + '/' + i + '.txt', train_file + '/test/labels/' + i + '.txt')
            except:
                pass
            try:
                shutil.copyfile(path + '/' + i + '.xml', train_file + '/valid/labels/' + i + '.xml')
                shutil.copyfile(path + '/' + i + '.xml', train_file + '/test/labels/' + i + '.xml')
            except:
                pass
