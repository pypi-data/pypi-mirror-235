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

# delimited writer/reader are inverses of each other

# delimited writer using format:
# [entry_1] [bin(delim)] [entry_2] [bin(delim)] ... [entry_n] [bin(delim)]
class DelimitedWriter():
    def __init__(self, filePath, bufferSize, delimiter):
        if not isinstance(delimiter, bytes):
            delimiter = delimiter.encode()
        self.filePath = filePath
        self.bufferSize = bufferSize
        self.delimiter = delimiter
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
        self.buffer += (entry + self.delimiter)
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

# delimited reader using format:
# [entry_1] [bin(delim)] [entry_2] [bin(delim)] ... [entry_n]
class DelimitedReader():
    def __init__(self, filePath, bufferSize, delimiter):
        if not isinstance(delimiter, bytes):
            delimiter = delimiter.encode()
        self.filePath = filePath
        self.bufferSize = bufferSize
        self.delimiter = delimiter
        self.buffer = b''
        self.iterComplete = False
        self.valueLoaded = False
        self.bufferIndex = 0
        self.entryStart = -1
        self.entryEnd = -1
        self.fileOffset = 0

    # append [numBytes] bytes to buffer; truncating value
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
        # assume start at: [entry_i] [bin(delim)] ...
        # load: [entry_i]
        i1 = self.buffer.find(self.delimiter, self.bufferIndex, len(self.buffer))
        # case: augment buffer until entry is found
        while i1 == -1:
            nr = self.updateBuffer(self.bufferSize)
            # case: [bin(delim)] not found in [self.buffer] and EOF => return NULL
            if nr == 0:
                self.iterComplete = True
                return False
            i1 = self.buffer.find(self.delimiter, self.bufferIndex, len(self.buffer))
        # case: i1 != -1 => entry found
        self.entryStart = self.bufferIndex
        self.entryEnd = i1
        self.bufferIndex = i1 + len(self.delimiter)
        self.valueLoaded = True
        return True

    def next(self):
        if not self.hasNext():
            return b''
        result = self.buffer[ self.entryStart : self.entryEnd ]
        self.entryStart = -1
        self.entryEnd = -1
        self.valueLoaded = False
        return result

    # pythonic API
    def __iter__(self):
        return self

    def __next__(self):
        if not self.hasNext():
            raise StopIteration
        result = self.buffer[ self.entryStart : self.entryEnd ]
        self.entryStart = -1
        self.entryEnd = -1
        self.valueLoaded = False
        return result
