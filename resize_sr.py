import PIL
from PIL import Image
import glob
import shutil, os
from time import sleep

def emptydir(dirname):  #清空資料夾
    if os.path.isdir(dirname):  #資料夾存在就刪除
        shutil.rmtree(dirname)
        sleep(3)  #需延遲,否則會出錯
    os.mkdir(dirname)  #建立資料夾

def dirResize(src, dst):
    myfiles = glob.glob(src + '/*.JPG')  #讀取資料夾全部jpg檔案
    emptydir(dst)
    print(src + ' 資料夾：')
    print('開始轉換圖形尺寸！')
    for i, f in enumerate(myfiles):
        img = Image.open(f)
        img_new = img.resize((300, 225), Image.Resampling.LANCZOS)  # 使用LANCZOS
        outname = f"resizejpg{str(i+1).zfill(3)}.jpg"
        img_new.save(os.path.join(dst, outname))
    print('轉換圖形尺寸完成！\n')


dirResize('carPlate_sr', 'carPlate')
dirResize('realPlate_sr', 'realPlate')