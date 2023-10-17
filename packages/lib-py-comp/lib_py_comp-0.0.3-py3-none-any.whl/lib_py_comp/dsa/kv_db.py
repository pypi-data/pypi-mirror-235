import os
import leveldb

# key value database with bytes API exclusively
# (get, set, remove, batchWrite, iterate)
class KeyValueDB():
    def __init__(self, dataDir):
        self.dataDir = dataDir
        self.db = leveldb.LevelDB( self.dataDir, create_if_missing=True )

    def clear(self):
        os.system(f'rm -r {self.dataDir} && mkdir {self.dataDir}')
        self.db = leveldb.LevelDB( self.dataDir, create_if_missing=True )

    # return bytearray; bytes = bytes(bytearray)
    def get(self, key, default=None):
        if not isinstance(key, bytes):
            key = key.encode()
        return self.db.Get(key, default=default)

    def set(self, key, value):
        if not isinstance(key, bytes):
            key = key.encode()
        if not isinstance(value, bytes):
            value = value.encode()
        return self.db.Put(key, value)

    def put(self, key, value):
        if not isinstance(key, bytes):
            key = key.encode()
        if not isinstance(value, bytes):
            value = value.encode()
        return self.db.Put(key, value)

    def remove(self, key):
        if not isinstance(key, bytes):
            key = key.encode()
        return self.db.Delete(key)

    def delete(self, key):
        if not isinstance(key, bytes):
            key = key.encode()
        return self.db.Delete(key)

    def batchWrite(self, setValues, removeValues, sync=True):
        wb = leveldb.WriteBatch()

        for [key, value] in setValues:
            if not isinstance(key, bytes):
                key = key.encode()
            if not isinstance(value, bytes):
                value = value.encode()
            wb.Put(key, value)

        for key in removeValues:
            if not isinstance(key, bytes):
                key = key.encode()
            wb.Delete(key)

        return self.db.Write(wb, sync=sync)

    # iterates (key, value) as bytearray
    def iterate(
        self,
        key_from = None,
        key_to = None,
        include_value = True,
        reverse = False,
    ):
        return self.db.RangeIter(
            key_from = key_from,
            key_to = key_to,
            include_value = include_value,
            reverse = reverse
        )

    def __iter__(self):
        return self.iterate()
