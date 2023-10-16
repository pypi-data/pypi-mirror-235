import os
import lib_py_comp.alg.typon_math as typon_math

def fwrite(fileName, fileRepr, mode='w'):
    fp = open(fileName, mode)
    fp.write(fileRepr)
    fp.close()

def fread(fileName, mode='r'):
    fp = open(fileName, mode)
    result = fp.read()
    fp.close()
    return result

# buffered writer using format:
# [len(entry_1)] [entry_1] [len(entry_2)] [entry_2] ...
class BufferedWriter():
    def __init__(self, filePath, bufferSize):
        self.filePath = filePath
        self.bufferSize = bufferSize
        self.buffer = b''

    def __del__(self):
        self.commit()

    def commit(self):
        fp = open(self.filePath, 'ab')
        fp.write(self.buffer)
        fp.close()
        result = len(self.buffer)
        self.buffer = b''
        return result

    # entry: bytes
    def writeF1(self, entry):
        if not isinstance(entry, bytes):
            entry = entry.encode()
        entryRepr = typon_math.serialize_int( len(entry) ) + entry
        self.buffer += entryRepr
        if len(self.buffer) >= self.bufferSize:
            return self.commit()
        return 0

    def write(self, entry, sync=False):
        self.writeF1(entry)
        if sync:
            self.commit()

    def close(self):
        self.commit()

    def clear(self):
        open(self.filePath, 'wb').close()

# buffered reader using format:
# [len(entry_1)] [entry_1] [len(entry_2)] [entry_2] ...
class BufferedReader():
    def __init__(self, filePath, bufferSize):
        self.filePath = filePath
        self.bufferSize = bufferSize
        self.buffer = b''
        self.iterComplete = False
        self.valueLoaded = False
        self.bufferIndex = 0
        self.entrySize = -1
        self.fileOffset = 0

    # append [numBytes] bytes to buffer; truncating previously read data
    def updateBuffer(self, numBytes):
        fp = open(self.filePath, 'rb')
        fp.seek(self.fileOffset, 0)
        buf = fp.read(numBytes)
        if len(buf) == 0:
            self.iterComplete = True
            return len(buf)
        # if self.bufferIndex > (self.bufferSize) // 2:
        if self.bufferIndex > 0:
            self.buffer = self.buffer[self.bufferIndex:]
            self.bufferIndex = 0
        self.buffer += buf
        self.fileOffset += len(buf)
        return len(buf)

    # preload value
    def hasNext(self):
        if self.iterComplete:
            return False
        if self.valueLoaded:
            return True
        # assume start at: [len(entry_i)] [entry_i] ...
        # load: [len(entry_i)]
        if self.bufferIndex + 8 > len(self.buffer):
            x = self.updateBuffer(max(8, self.bufferSize))
        if self.bufferIndex + 8 > len(self.buffer):
            self.iterComplete = True
            return False
        entryLen = typon_math.deserialize_int(self.buffer[self.bufferIndex:self.bufferIndex+8])
        # load: [entry_i]
        if self.bufferIndex + 8 + entryLen > len(self.buffer):
            self.updateBuffer(max(entryLen, self.bufferSize))
        if self.bufferIndex + 8 + entryLen > len(self.buffer):
            self.iterComplete = True
            print(self.buffer[self.bufferIndex+8:self.bufferIndex+8+entryLen])
            return False
        self.bufferIndex += 8
        self.entrySize = entryLen
        self.valueLoaded = True
        return True

    def next(self):
        if not self.hasNext():
            return b''
        result = self.buffer[self.bufferIndex:self.bufferIndex+self.entrySize]
        self.bufferIndex += self.entrySize
        self.entrySize = -1
        self.valueLoaded = False
        return result

    # pythonic API
    def __iter__(self):
        return self

    def __next__(self):
        if not self.hasNext():
            raise StopIteration
        result = self.buffer[self.bufferIndex:self.bufferIndex+self.entrySize]
        self.bufferIndex += self.entrySize
        self.entrySize = -1
        self.valueLoaded = False
        return result
