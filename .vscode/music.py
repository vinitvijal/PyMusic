from playsound import playsound
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

cred = credentials.Certificate("popup-766d7-firebase-adminsdk-yay84-2ce9f0396a.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'popup-766d7.appspot.com'
})
bucket = storage.bucket()

# playsound('https://firebasestorage.googleapis.com/v0/b/popup-766d7.appspot.com/o/Toh%20Phir.mp3?alt=media&token=431f99cb-b1e1-4541-a6e8-58be2df69fd5')
file = "/Users/vinit/Desktop/PyMusic/TohPhirAao.mp3"
print('playing sound using native player')
os.system("afplay " + file)

# Functions Of Music Player !!!!!
def options():
    print("1. Upload Music")
    print("2. Music List")
    todo = input("")
    if todo == "1":
        uploadMusic()
    elif todo == "2":
        playMusic()

def playMusic():

    playsound('https://firebasestorage.googleapis.com/v0/b/popup-766d7.appspot.com/o/Toh%20Phir.mp3?alt=media&token=431f99cb-b1e1-4541-a6e8-58be2df69fd5')

def uploadMusic():
    fileName = input("Enter Your Songs Name : ")
    filePath = input("Path of Your Song : ")
    confirm = input("Confirm Y/N/exit : ")
    if confirm == "y" or "Y":
        blob = bucket.blob(fileName + '.mp3')
        blob.upload_from_filename(filePath)
        print("Upload Successfully!!!")
        print("")
        options()
    if confirm == "n" or "N":
        options()
    if confirm == "exit":
        options()



def exit():
    options()


# options()
