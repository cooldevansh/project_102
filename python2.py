import dropbox
import os
arr = os.listdir('.')
print(arr)

class TransferData:
    def __init__(self, access):
        self.access = access
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access)


        file_upload = open(file_from, 'rb')
        dbx.files_upload(file_upload.read(), file_to)
for i in arr:        
        
        access = "sl.BdeEbZMT2Kko2JsOWiFhnG6bEDqDGQwUodw_0kYGIJw5LrL0yZ8B0Qxa9AWa_Y3ihrT_EDH4xdzsTwt7g93gXmimML_X0LPlpXEcPr5xidOTVTlSKYdsYqRjdTisVwOl_-aRqmH64jk"
        file_from=i
        print(file_from)
        transferData = TransferData(access)
        file_to = "/test_dropbox/test.txt"
        transferData.upload_file(file_from, file_to)
        print("File has been moved to dropbox.")

    