import os.path
import sys
from PIL import Image

'''
1. 使用argparse进行优化
2. 判断是否为gif动图
3. 将分离图片放置到默认default文件夹中,或指定文件夹
4. 设置保存图片的格式，png，jpg
5. 判断是否为文件，判断文件是否可读
6. 判断是否可以将程序模块化
7. 
'''
if len(sys.argv) == 2:
    filename = sys.argv[1]
    if not os.path.isfile(filename): 		#判断是否是文件
        print('[-] ' + filename +' does not exist.')
        exit(0)
            
    if not os.access(filename, os.R_OK):   #判断文件是否可读
        print('[-] ' + filename +' access denied.')
        exit(0)
else:   
    print('[-] Usage: ' + str(sys.argv[0]) +' <vuln filename>')
    exit(0)

path = ".\\default\\"

# 创建default文件夹
if not os.path.exists(path):
	os.mkdir(path)

# 重要部分
im = Image.open(filename)

name,filetype = os.path.splitext(filename)

try:
	im.save("{}{}{:02d}.png".format(path,name,im.tell()))
	while True:
		im.seek(im.tell()+1)
		im.save("{}{}{:02d}.png".format(path,name,im.tell()))
except Exception as e:
	print(e)
	print("处理结束")
