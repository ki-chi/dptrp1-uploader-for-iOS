import os
import appex
import dptrp1
from urllib.parse import quote

key_file = "./key.txt"
client_id_file = "./client_id.txt"

if not appex.is_running_extension():
    print("This script is intended to be run from the sharing extension.")
    exit()

localpath = appex.get_file_path()
if not localpath:
    print("No input PDF found.")
    exit()
print(localpath)

dp = dptrp1.DigitalPaper()
if os.path.exists(key_file) and os.path.exists(client_id_file):
    with open(key_file, 'rb') as fh:
        key = fh.read()

    with open(client_id_file, 'r') as fh:
        client_id = fh.readline().strip()
else:
    _, key, client_id = dp.register()

    with open(key_file, 'w') as f:
        f.write(key)

    with open(client_id_file, 'w') as f:
        f.write(client_id)

dp.authenticate(client_id, key)

filename = os.path.basename(localpath)
encoded_filename = quote(os.path.splitext(filename)[0]) + ".pdf"

remotepath = "Document/Received/"+encoded_filename
with open(localpath, 'rb') as fh:
    dp.upload(fh, remotepath)

print(remotepath)
print("Uploaded.")
