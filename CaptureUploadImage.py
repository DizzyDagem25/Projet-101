from tracemalloc import take_snapshot
import cv2 
import time 
import random 
import dropbox 
start_time = time.time()
def take_SnapShot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True 
    while (result):
        ret,frame = videoCaptureObject.read()
        image_name = "img"+str(number)+".png"
        cv2.imwrite(image_name,frame)
        start_time = time.time
        result = False 
    return image_name
    print("Snapshot Taken.")
    videoCaptureObject.release() 
    cv2.destroyAllWindows()
        
def upload_file(image_name):
    access_token = "sl.BHIV1-qSiE2ZloTdnadctO9JKgwA-p4BFyA_5mfgMVKXeupNB69o66G7lPR0jbzDekCUVTPj6aDUKmL1QGcZ01_jUStrKW6wo5IO0ocWEOGZkdAi2lmbJUGKr-11ZcQ2FGD0kFEX-eBF"
    file = image_name 
    file_from = file 
    file_to = "/testFolder"+(image_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while(True):
        if((time.time()-start_time)>= 5):
            name = take_SnapShot()
            upload_file(name)
main()
