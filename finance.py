import files

fm = files.Filemanager()
encryption = files.Encryption()

files = fm.listDirectory()
for f in files:
    print(f)
