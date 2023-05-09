"""
Extract all the 6 training zipped files and 2 validation zipped files into data folder and then run this script
将所有 6 个训练压缩文件和 2 个验证压缩文件提取到数据文件夹中，然后运行此脚本
"""
import cv2
import numpy as np
import os
import zipfile

# Running a loop through all the zipped training file to extract all video and then extract 100 frames from each.
# 遍历所有压缩的训练文件以提取所有视频，然后从每个视频中提取 100 帧。
for i in range(13, 25):
    if i < 10:
        zipfilename = 'training80_0' + str(i) + '.zip'
    else:
        zipfilename = 'training80_' + str(i) + '.zip'
    # Accessing the zipfile i
    # 访问压缩文件 i
    archive = zipfile.ZipFile('C:/Users/l/Desktop/First_Impression_v2/train-2/' + zipfilename, 'r')
    zipfilename = zipfilename.split('.zip')[0]

    # Extracting all videos in it and saving it all to the new folder with same name as zipped one
    # 提取其中的所有视频并将其全部保存到与压缩文件夹同名的新文件夹中
    archive.extractall('unzippedData/' + zipfilename)

    # Running a loop over all the videos in the zipped file and extracting 100 frames from each
    # 对压缩文件中的所有视频运行循环，并从每个视频中提取 100 帧
    for file_name in archive.namelist():
        cap = cv2.VideoCapture('unzippedData/' + zipfilename + '/' + file_name)

        file_name = (file_name.split('.mp4'))[0]
        # Creating folder to save all the 100 frames from the video
        # 创建文件夹以保存视频中的所有100帧
        try:
            if not os.path.exists('ImageData/trainingData/' + file_name):
                os.makedirs('ImageData/trainingData/' + file_name)
        except OSError:
            print('Error: Creating directory of data')

        # Setting the frame limit to 100
        # 将帧限制设置为 100
        cap.set(cv2.CAP_PROP_FRAME_COUNT, 101)
        length = 101
        count = 0
        # Running a loop to each frame and saving it in the created folder
        # 对每个帧运行循环并将其保存在创建的文件夹中
        while (cap.isOpened()):
            count += 1
            if length == count:
                break
            ret, frame = cap.read()
            if frame is None:
                continue

            # Resizing it to 256*256 to save the disk space and fit into the model
            # 将其大小调整为256256以节省磁盘空间并适合模型
            frame = cv2.resize(frame, (256, 256), interpolation=cv2.INTER_CUBIC)
            # Saves image of the current frame in jpg file
            name = 'ImageData/trainingData/' + str(file_name) + '/frame' + str(count) + '.jpg'
            cv2.imwrite(name, frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Print the file which is done
        # 打印完成的文件
        print(zipfilename, ':', file_name)
qqqq = input()
# 测试集
for i in range(1, 26):
    if i < 10:
        zipfilename = 'validation80_0' + str(i) + '.zip'
    else:
        zipfilename = 'validation80_' + str(i) + '.zip'
    # Accessing the zipfile i
    archive = zipfile.ZipFile('data/' + zipfilename, 'r')
    zipfilename = zipfilename.split('.zip')[0]

    # Extracting all videos in it and saving it all to the new folder with same name as zipped one
    # 提取其中的所有视频并将其全部保存到与压缩文件夹同名的新文件夹中
    archive.extractall('unzippedData/' + zipfilename)

    # Running a loop over all the videos in the zipped file and extracting 100 frames from each
    # 对压缩文件中的所有视频运行循环，并从每个视频中提取 100 帧
    for file_name in archive.namelist():
        cap = cv2.VideoCapture('unzippedData/' + zipfilename + '/' + file_name)

        file_name = (file_name.split('.mp4'))[0]
        # Creating folder to save all the 100 frames from the video
        # 创建文件夹以保存视频中的所有100帧
        try:
            if not os.path.exists('ImageData/validationData/' + file_name):
                os.makedirs('ImageData/validationData/' + file_name)
        except OSError:
            print('Error: Creating directory of data')

        # Setting the frame limit to 100
        # 将帧限制设置为 100
        cap.set(cv2.CAP_PROP_FRAME_COUNT, 101)
        length = 101
        count = 0
        # Running a loop to each frame and saving it in the created folder
        # 对每个帧运行循环并将其保存在创建的文件夹中
        while (cap.isOpened()):
            count += 1
            if length == count:
                break
            ret, frame = cap.read()
            if frame is None:
                continue

            # Resizing it to 256*256 to save the disk space and fit into the model
            # 将其大小调整为256256以节省磁盘空间并适合模型
            frame = cv2.resize(frame, (256, 256), interpolation=cv2.INTER_CUBIC)
            # Saves image of the current frame in jpg file
            name = 'ImageData/validationData/' + str(file_name) + '/frame' + str(count) + '.jpg'
            cv2.imwrite(name, frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Print the file which is done
        # 打印完成的文件
        print(zipfilename, ':', file_name)
