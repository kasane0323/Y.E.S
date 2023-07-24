#!pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
#!pip install firebase-admin
#!pip install google-cloud-firestore

import requests
import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

from oauth2client.service_account import ServiceAccountCredentials
from httplib2 import Http
import json

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# Googleドライブへの画像保存
# 画像をダウンロードして保存する関数
def download_image(url, file_name):
    with open(file_name, 'wb') as file:
        response = requests.get(url)
        file.write(response.content)

# Google Driveに画像をアップロードする関数


def upload_image_to_drive(credentials, file_name, folder_id=None):
    service = build('drive', 'v3', credentials=credentials)
    file_metadata = {'name': os.path.basename(file_name)}
    if folder_id:
        file_metadata['parents'] = [folder_id]

    media = MediaFileUpload(file_name)
    file = service.files().create(body=file_metadata,
                                  media_body=media, fields='id').execute()
    print('Uploaded:', file.get('id'))
    global imageb_id
    imageb_id = file.get('id')
    global imageb_url
    imageb_url = 'https://drive.google.com/uc?id='+imageb_id


def main():
    # 画像URLとGoogleドライブへのアップロード先フォルダIDを設定
    # YESに入力された画像URL
    image_url = image_url
    #'https://drive.google.com/uc?id=11X5Imzd0Eybg4du6_zln1gqCzGHvPZwh'  # tweetImage
    folder_id = '1U0JA4mLIOngGoeFJMLZ6bBTzI1vqHIEW'  # Googleドライブ上のアップロード先フォルダのIDを指定

    # 画像をダウンロードして一時的なファイルに保存
    file_name = 'temp_image.jpg'
    download_image(image_url, file_name)

    # Google Driveへのアップロード
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'yesb-390408-6db61518f675.json', scopes=['https://www.googleapis.com/auth/drive'])
    upload_image_to_drive(credentials, file_name, folder_id)

    # 一時的なファイルを削除
    os.remove(file_name)


if __name__ == "__main__":
    main()


# GoogleドライブのID、URLを抽出
print('ID:', imageb_id)
print('URL:', imageb_url)


# CloudFirestoreを初期化
project_id = "yesb-9fea3"
key_path = "/content/drive/MyDrive/yes/yesb-9fea3-firebase-adminsdk-9b2ap-d1ba3a40d1.json"
cred = credentials.Certificate(key_path)
firebase_admin.initialize_app(cred, {
    'projectId': project_id,
})

db = firestore.client()


# ドキュメントを設定
data = {"beforeUrl": imageb_url, "beforeId": imageb_id, "afterUrl": "",
        "afterId": "", "text": messege, "twitterUrl": ""}
# "time": datetime.datetime.now(tz=datetime.timezone.utc)

data_ref = db.collection("yes_twitter").document(
    "00000001").collection("image").document("newid").set(data)
data_ref

# print(f"Added document with id {data_ref.id}")


# ドキュメントを追加
# 今回は00000001顧客のみに追加
# 加工後画像情報のDB保存
data_ref = db.collection("yes_twitter").document(
    "00000001").collection("image").document("newid")
data_after = data_ref.update({"afterUrl": imagea_url, "afterId": imagea_id})
data_after


# DBからTwitter投稿用情報を読み取り
data_ref = db.collection("yes_twitter").document(
    "00000001").collection("image")
docs = data_ref.stream()

for doc in docs:
    print(f"{doc.id} => {doc.to_dict()}")

# 情報のみプリント

# TwitterURLをDBに追加
#data_ref = db.collection("yes_twitter").document(
#    "00000001").collection("image").document("newid")
#data_twitter = data_ref.update({"twitterUrl": ""})  # URLの変数追加
#data_twitter
