def fwrite(fileName, fileRepr, mode='w'):
    fp = open(fileName, mode)
    fp.write(fileRepr)
    fp.close()

def fread(fileName, mode='r'):
    fp = open(fileName, mode)
    result = fp.read()
    fp.close()
    return result
