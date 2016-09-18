def verfiy_md5(file,verification_code):
    import hashlib
    # read contents of the file
    data = file.read()    
    # pipe contents of the file through
    md5_returned = hashlib.md5(data).hexdigest()
    if verification_code == md5_returned:
        return True
    else:
        return False