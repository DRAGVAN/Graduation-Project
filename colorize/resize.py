import os
import cv2

# linedir = "D:Study/Code/Python/Qt/colorize/background/user"
PICdir = "D:\\Study\\Code\\Python\\Qt\\colorize\\background\\user"
# img_size = 256
path = os.path.join(PICdir)

img_list = os.listdir(path)
# ind = 1
# print(path)
# print(path)
for filename in img_list:
    img_array = cv2.imread(path+'\\'+filename)
    print(filename)
    new_array = cv2.resize(img_array, (596, 417))
    save_path = path+'\\'+filename +'.jpg'
    cv2.imwrite(save_path, new_array)
# print(ind)
#     ind = ind + 1