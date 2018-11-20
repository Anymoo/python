import os
import shutil
import csv


column = [[], [], [], [], [], []]
with open('C:/Users/Administrator/Desktop/周报/ABIDE1_by_age_10.csv', 'r', encoding='UTF8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        for i in range(6):
            column[i].append(row[i])
    column[0] = column[0][:220]
    column[1] = column[1][:676]
    column[2] = column[2][:199]
    column[3] = column[3][:58]
    column[4] = column[4][:17]
    column[5] = column[5][:5]

# For ROISignals
'''
result_path = "ROISignals_FunImgARCWF/"
Age_file = ["Age_0-10/", "Age_11-20/", "Age_21-30/", "Age_31-40/", "Age_41-50/", "Age_51-64/"]

for i in range(6):
    for file_name in column[i]:
        if os.path.exists(r"E:/fMRI/ABIDE/Results/" + result_path + file_name):
            oldname = u"E:/fMRI/ABIDE/Results/" + result_path + file_name
            newname = u"E:/fMRI/ABIDE/Results/" + result_path + Age_file[i] + file_name
            shutil.copyfile(oldname, newname)
        else:
            continue
'''

#For DegreeCentrality
'''
result_path = "DegreeCentrality_FunImgARglobalCWF/"
Age_file = ["Age_0-10/", "Age_11-20/", "Age_21-30/", "Age_31-40/", "Age_41-50/", "Age_51-64/"]

for i in range(6):
    for file_name in column[i]:
        if os.path.exists(r"E:/fMRI/ABIDE/Results/" + result_path + file_name):
            oldname = u"E:/fMRI/ABIDE/Results/" + result_path + file_name
            newname = u"E:/fMRI/ABIDE/Results/" + result_path + Age_file[i] + file_name
            shutil.copyfile(oldname, newname)
        else:
            continue
'''

# For fALFF
'''
result_path = "fALFF_FunImgARglobalCW/"
Age_file = ["Age_0-10/", "Age_11-20/", "Age_21-30/", "Age_31-40/", "Age_41-50/", "Age_51-64/"]

for i in range(6):
    for file_name in column[i]:
        if os.path.exists(r"E:/fMRI/ABIDE/Results/" + result_path + file_name):
            oldname = u"E:/fMRI/ABIDE/Results/" + result_path + file_name
            newname = u"E:/fMRI/ABIDE/Results/" + result_path + Age_file[i] + file_name
            shutil.copyfile(oldname, newname)
        else:
            continue

'''
# For ALFF
'''
result_path = "ALFF_FunImgARglobalCW/"
Age_file = ["Age_0-10/", "Age_11-20/", "Age_21-30/", "Age_31-40/", "Age_41-50/", "Age_51-64/"]

for i in range(6):
    for file_name in column[i]:
        if os.path.exists(r"E:/fMRI/ABIDE/Results/" + result_path + file_name):
            oldname = u"E:/fMRI/ABIDE/Results/" + result_path + file_name
            newname = u"E:/fMRI/ABIDE/Results/" + result_path + Age_file[i] + file_name
            shutil.copyfile(oldname, newname)
        else:
            continue

# result_path = "ALFF_FunImgARCW/"
# Age_file = ["Age_0-10/", "Age_11-20/", "Age_21-30/", "Age_31-40/", "Age_41-50/", "Age_51-64/"]
#
# for i in range(6):
#     for file_name in column[i]:
#         if os.path.exists(r"E:/fMRI/ABIDE/Results/" + result_path + file_name):
#             oldname = u"E:/fMRI/ABIDE/Results/" + result_path + file_name
#             newname = u"E:/fMRI/ABIDE/Results/" + result_path + Age_file[i] + file_name
#             shutil.copyfile(oldname, newname)
#         else:
#             continue
'''
# For ReHo
'''
# ReHo 结果文件夹
result_path = "ReHo_FunImgARglobalCWF/"
# 各年龄段文件夹
Age_file = ["Age_0-10/", "Age_11-20/", "Age_21-30/", "Age_31-40/", "Age_41-50/", "Age_51-64/"]

# 6个年龄段
for i in range(6):
    # 一个年龄段一列，从csv中获取
    for file_name in column[i]:
        # 是否存在该名称的文件
        if os.path.exists(r"E:/fMRI/ABIDE/Results/" + result_path + file_name):
            # 待复制的文件路径
            oldname = u"E:/fMRI/ABIDE/Results/" + result_path + file_name
            # 复制后的文件路径
            newname = u"E:/fMRI/ABIDE/Results/" + result_path + Age_file[i] + file_name
            # 复制操作
            shutil.copyfile(oldname, newname)
        else:
            continue
'''