import re
print(dir(re))
# 从文件读取 Adcode ， 装入list
AdcList = []
with open('adcode.csv', 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        line = line.strip('\n')
        AdcList.append(list(map(str, line.split(','))))

# 打开待处理的POI文件，必须包含名称和地址两列
AOIList = []
with open('aoilist.csv', 'r', encoding='utf-8', errors='ignore') as af:
    for aline in af:
        aline = aline.strip('\n')
        AOIList.append(list(map(str, aline.split(','))))

for aoi in AOIList:
    for adc in AdcList:
        name = aoi[2]
        address = aoi[3]
        AdminName = adc[1]
        ff = address.find(AdminName)
        if ff > 0:
            print(name, address, AdminName, adc[0])
