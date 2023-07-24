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
    global imagea_id
    imagea_id = file.get('id')
    global imagea_url
    imagea_url = 'https://drive.google.com/uc?id='+imagea_id


def main():
    # 画像URLとGoogleドライブへのアップロード先フォルダIDを設定
    # tweet用ステガノグラフィ付き画像URL
    image_url = 'https://drive.google.com/uc?id=11X5Imzd0Eybg4du6_zln1gqCzGHvPZwh'
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
print('ID:', imagea_id)
print('URL:', imagea_url)
