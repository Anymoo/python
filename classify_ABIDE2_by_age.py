import os
import shutil
import csv

organization_name = ["_ABIDEII-BNI_1_", "_ABIDEII-EMC_1_", "_ABIDEII-ETH_1_", "_ABIDEII-GU_1_", "_ABIDEII-IP_1_",
                     "_ABIDEII-IU_1_", "_ABIDEII-KKI_1_", "_ABIDEII-KUL_3_", "_ABIDEII-NYU_1_", "_ABIDEII-NYU_2_",
                     "_ABIDEII-OHSU_1_", "_ABIDEII-OILH_2_", "_ABIDEII-SDSU_1_", "_ABIDEII-TCD_1_", "_ABIDEII-UCD_1_",
                     "_ABIDEII-UCLA_1_", "_ABIDEII-USM_1_"]
Age_file = ["Age_0-10/", "Age_11-20/", "Age_21-30/", "Age_31-40/", "Age_41-50/", "Age_51-64/"]
column = [[], [], [], [], [], []]
with open('C:/Users/Administrator/Desktop/周报/ABIDE2_by_age_10.csv', 'r', encoding='UTF8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        for i in range(6):
            column[i].append(row[i])
    column[0] = column[0][:482]
    column[1] = column[1][:436]
    column[2] = column[2][:138]
    column[3] = column[3][:18]
    column[4] = column[4][:23]
    column[5] = column[5][:17]
# for i in range(6):
#     print(column[i])


# For ROISignals
'''
result_path = "ROISignals_FunImgARglobalCWF/"

for j in range(len(organization_name)):
    for i in range(6):
        for file_name in column[i]:
            if os.path.exists(r"E:/fMRI/ABIDE II/Results/" + result_path + "ROISignals" + organization_name[j] + file_name + ".mat"):
                oldname = u"E:/fMRI/ABIDE II/Results/" + result_path + "ROISignals" + organization_name[j] + file_name + ".mat"
                newname = u"E:/fMRI/ABIDE II/Results/" + result_path + Age_file[i] + "ROISignals" + organization_name[j] + file_name + ".mat"
                shutil.copyfile(oldname, newname)
            else:
                continue
'''

#For DegreeCentrality
'''
result_path = "DegreeCentrality_FunImgARCWF/"

for j in range(len(organization_name)):
    for i in range(6):
        for file_name in column[i]:
            if os.path.exists(r"E:/fMRI/ABIDE II/Results/" + result_path + "DegreeCentrality_PositiveBinarizedSumBrainMap" + organization_name[j] + file_name + ".nii.gz"):
                oldname = u"E:/fMRI/ABIDE II/Results/" + result_path + "DegreeCentrality_PositiveBinarizedSumBrainMap" + organization_name[j] + file_name + ".nii.gz"
                newname = u"E:/fMRI/ABIDE II/Results/" + result_path + Age_file[i] + "DegreeCentrality_PositiveBinarizedSumBrainMap" + organization_name[j] + file_name + ".nii.gz"
                shutil.copyfile(oldname, newname)
            else:
                continue
'''

# For fALFF
'''
# result_path = "fALFF_FunImgARglobalCW/"
# for j in range(len(organization_name)):
#
#     for i in range(6):
#         for file_name in column[i]:
#             if os.path.exists(r"E:/fMRI/ABIDE II/Results/" + result_path + "fALFFMap" + organization_name[j] + file_name + ".nii.gz"):
#                 oldname = u"E:/fMRI/ABIDE II/Results/" + result_path + "fALFFMap" + organization_name[j] + file_name + ".nii.gz"
#                 newname = u"E:/fMRI/ABIDE II/Results/" + result_path + Age_file[i] + "fALFFMap" + organization_name[j] + file_name + ".nii.gz"
#                 shutil.copyfile(oldname, newname)
#             else:
#                 continue

result_path = "fALFF_FunImgARCW/"

for j in range(len(organization_name)):
    for i in range(6):
        for file_name in column[i]:
            if os.path.exists(r"E:/fMRI/ABIDE II/Results/" + result_path + "fALFFMap" + organization_name[j] + file_name + ".nii.gz"):
                oldname = u"E:/fMRI/ABIDE II/Results/" + result_path + "fALFFMap" + organization_name[j] + file_name + ".nii.gz"
                newname = u"E:/fMRI/ABIDE II/Results/" + result_path + Age_file[i] + "fALFFMap" + organization_name[j] + file_name + ".nii.gz"
                shutil.copyfile(oldname, newname)
            else:
                continue
'''

# For ALFF
'''
# result_path = "ALFF_FunImgARglobalCW/"
#
# for j in range(len(organization_name)):
#     for i in range(6):
#         for file_name in column[i]:
#             if os.path.exists(r"E:/fMRI/ABIDE II/Results/" + result_path + "ALFFMap" + organization_name[j] + file_name + ".nii.gz"):
#                 oldname = u"E:/fMRI/ABIDE II/Results/" + result_path + "ALFFMap" + organization_name[j] + file_name + ".nii.gz"
#                 newname = u"E:/fMRI/ABIDE II/Results/" + result_path + Age_file[i] + "ALFFMap" + organization_name[j] + file_name + ".nii.gz"
#                 shutil.copyfile(oldname, newname)
#             else:
#                 continue

result_path = "ALFF_FunImgARCW/"

for j in range(len(organization_name)):
    for i in range(6):
        for file_name in column[i]:
            if os.path.exists(r"E:/fMRI/ABIDE II/Results/" + result_path + "ALFFMap" + organization_name[j] + file_name + ".nii.gz"):
                oldname = u"E:/fMRI/ABIDE II/Results/" + result_path + "ALFFMap" + organization_name[j] + file_name + ".nii.gz"
                newname = u"E:/fMRI/ABIDE II/Results/" + result_path + Age_file[i] + "ALFFMap" + organization_name[j] + file_name + ".nii.gz"
                shutil.copyfile(oldname, newname)
            else:
                continue
'''

# For VMHC
'''
result_path = "VMHC_FunImgARglobalCWFsymS/"

for j in range(len(organization_name)):
    for i in range(6):
        for file_name in column[i]:
            if os.path.exists(r"E:/fMRI/ABIDE II/Results/" + result_path + "zVMHCMap" + organization_name[j] + file_name + ".nii.gz"):
                oldname = u"E:/fMRI/ABIDE II/Results/" + result_path + "zVMHCMap" + organization_name[j] + file_name + ".nii.gz"
                newname = u"E:/fMRI/ABIDE II/Results/" + result_path + Age_file[i] + "zVMHCMap" + organization_name[j] + file_name + ".nii.gz"
                shutil.copyfile(oldname, newname)
            else:
                continue
'''

# For ReHo
'''
# ReHo 结果文件夹
result_path = "ReHo_FunImgARCWF/"
# 各年龄段文件夹

# 6个年龄段
for j in range(len(organization_name)):
    for i in range(6):
        for file_name in column[i]:
            if os.path.exists(r"E:/fMRI/ABIDE II/Results/" + result_path + "ReHoMap" + organization_name[j] + file_name + ".nii.gz"):
                oldname = u"E:/fMRI/ABIDE II/Results/" + result_path + "ReHoMap" + organization_name[j] + file_name + ".nii.gz"
                newname = u"E:/fMRI/ABIDE II/Results/" + result_path + Age_file[i] + "ReHoMap" + organization_name[j] + file_name + ".nii.gz"
                shutil.copyfile(oldname, newname)
            else:
                continue
'''