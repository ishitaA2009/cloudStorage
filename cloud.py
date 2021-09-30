import dropbox

class TransferData:
     def __init__(self, access_token):
         self.access_token = access_token

     def upload_file(self, file_from, file_to):
         dbx = dropbox.Dropbox(self.access_token)

         f = open(file_from, 'rb')
         dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'HVtYfKsy6dAAAAAAAAAAAYsyW5H4_jGgr3T0ht9g6rIR0tkH-Cp6aEa23949avIy'
    transferData = TransferData(access_token)

    file_from = input("Enter the file to be uploaded: ")
    file_to = input("Enter the file path to upload to the dropbox: ")

    transferData.upload_file(file_from, file_to)

    print("Your file has been uploaded")

main()
                     