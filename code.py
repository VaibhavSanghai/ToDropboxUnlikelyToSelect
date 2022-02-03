import cv2
import dropbox
import time
import random

#access token
start_time = time.time()

def take_snapshot(start_time):
    number = random.randint(0, 100)
    videoCapObj = cv2.VideoCapture(0)
    result = True
    while (result, start_time):
        ret, frame = videoCapObj.read()
        image_name = "img" + str(number) + ".png"
        cv2.imwrite(image_name, frame)
        start_time = time.time()
        result = False
    
    videoCapObj.release()
    cv2.destroyAllWindows()

    print("Snapshot taken")
    return image_name


take_snapshot(start_time)

def upload_file(image_name):
        access_token = '2wDLu2UCAvoAAAAAAAAAAQxCDznUUBFtih-Yglp-adrk8MvrOT8_R6OvTdTp9XcD'
        file = image_name
        file_from = file
        file_to = "/newFolder1" + (image_name)
        dbx = dropbox.Dropbox()

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overWrite)
            print("file uploaded")

def main(start_time):
    while(True):
        if((time.time() - start_time) >=30):
            name = take_snapshot()
            upload_file(name)

main(start_time)
