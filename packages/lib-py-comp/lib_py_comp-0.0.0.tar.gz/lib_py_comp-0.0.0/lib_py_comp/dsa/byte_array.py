import os
import lib_py_comp.alg.typon_math as typon_math

def makeVba(base_path):
    return VariableBytesArray(base_path)

def mergeVbas(vba1, vba2, out_path):
    result = VariableBytesArray(out_path)
    result.extend(vba1.slice(0, vba1.item_count))
    result.extend(vba2.slice(0, vba2.item_count))
    return result

# file format:
# index_file: [offset_1] [length_1] [offset_2] [length_2] ... [offset_n] [length_n]
# data_file: [entry_1] [entry_2] ... [entry_n]

class VariableBytesArray():

    def __init__(self, base_path: str):
        self.base_path = base_path
        self.index_fspath = f'{base_path}/index'
        self.data_fspath = f'{base_path}/data'
        self.item_count = 0
        self.total_bytes = 0

        if not os.path.isdir(self.base_path):
            os.mkdir(self.base_path)

        if not os.path.exists(self.index_fspath):
            open(self.index_fspath, 'wb').close()

        if not os.path.exists(self.data_fspath):
            open(self.data_fspath, 'wb').close()

        self.size_fxn = os.path.getsize
        self.item_count = self.size_fxn(self.index_fspath) // 16
        self.total_bytes = self.size_fxn(self.data_fspath)

    def index_size(self) -> int:
        return self.size_fxn(self.index_fspath)

    def data_size(self) -> int:
        return self.size_fxn(self.data_fspath)

    def read_index_bytes(self, offset: int, limit: int) -> str:
        fptr = open(self.index_fspath, 'rb')
        fptr.seek(offset, 0)
        result = fptr.read(limit)
        fptr.close()
        return result

    def read_data_bytes(self, offset: int, limit: int) -> str:
        fptr = open(self.data_fspath, 'rb')
        fptr.seek(offset, 0)
        result = fptr.read(limit)
        fptr.close()
        return result

    def count(self):
        return self.item_count

    def append(self, target_bytes) -> int:
        size_repr = typon_math.serialize_int( len(target_bytes) )
        offset_repr = typon_math.serialize_int( self.total_bytes )
        index_bytes = offset_repr + size_repr

        fptr = open(self.index_fspath, 'ab')
        # fptr.write(offset_repr)
        # fptr.write(size_repr)
        fptr.write(index_bytes)
        fptr.close()

        fptr1 = open(self.data_fspath, 'ab')
        fptr1.write(target_bytes)
        fptr1.close()

        self.total_bytes += len(target_bytes)
        self.item_count += 1
        return self.item_count - 1

    # memory conservative approach
    def extendConserve(self, target_bytes_L1) -> int:
        current_offset = 0
        fptr = open(self.index_fspath, 'ab')
        fptr1 = open(self.data_fspath, 'ab')

        for i in range(0, len(target_bytes_L1)):
            size_repr = typon_math.serialize_int( len(target_bytes_L1[i]) )
            offset_repr = typon_math.serialize_int(self.total_bytes + current_offset)

            fptr.write(offset_repr)
            fptr.write(size_repr)
            fptr1.write( target_bytes_L1[i] )
            current_offset += len(target_bytes_L1[i])

        fptr.close()
        fptr1.close()

        self.total_bytes += current_offset
        self.item_count += len(target_bytes_L1)
        return self.item_count - 1

    # memory liberal approach
    def extendLiberal(self, target_bytes_L1) -> int:
        current_offset = 0
        indexBytes = b''
        dataBytes = b''

        for i in range(0, len(target_bytes_L1)):
            size_repr = typon_math.serialize_int( len(target_bytes_L1[i]) )
            offset_repr = typon_math.serialize_int(self.total_bytes + current_offset)
            indexBytes += (offset_repr + size_repr)
            dataBytes += target_bytes_L1[i]
            current_offset += len(target_bytes_L1[i])


        fptr = open(self.index_fspath, 'ab')
        fptr1 = open(self.data_fspath, 'ab')

        fptr.write(indexBytes)
        fptr1.write(dataBytes)

        fptr.close()
        fptr1.close()

        self.total_bytes += current_offset
        self.item_count += len(target_bytes_L1)
        return self.item_count - 1

    def extend(self, target_bytes_L1, conserve=False) -> int:
        if len(target_bytes_L1) == 0:
            return self.item_count - 1
        if conserve == True:
            return self.extendConserve(target_bytes_L1)
        self.extendLiberal(target_bytes_L1)

    def get(self, item_id: int) -> str:
        if item_id < 0 or item_id >= self.item_count:
            return ''

        fptr = open(self.index_fspath, 'rb')
        fptr.seek(16 * item_id, 0)
        index_repr = fptr.read(16)
        fptr.close()

        item_offset = typon_math.deserialize_int(index_repr[ 0 : 8 ])
        item_size = typon_math.deserialize_int(index_repr[ 8 : 16 ])

        fptr = open(self.data_fspath, 'rb')
        fptr.seek(item_offset, 0)
        result = fptr.read(item_size)
        fptr.close()
        return result

    def slice(self, id_lower_bound: int, id_upper_bound: int):
        if id_lower_bound < 0 or id_upper_bound > self.item_count or id_lower_bound >= id_upper_bound:
            return []

        fptr = open(self.index_fspath, 'rb')
        fptr.seek(16 * id_lower_bound, 0)
        index_repr = fptr.read(16 * (id_upper_bound - id_lower_bound))
        fptr.close()

        fptr = open(self.data_fspath, 'rb')
        result: vec[str] = []

        for i in range(id_lower_bound, id_upper_bound):
            index_offset = 16 * (i - id_lower_bound)
            item_offset = typon_math.deserialize_int(index_repr[ index_offset + 0 : index_offset + 8 ])
            item_size = typon_math.deserialize_int(index_repr[ index_offset + 8 : index_offset + 16 ])

            fptr.seek(item_offset, 0)
            item_repr = fptr.read(item_size)
            result.append(item_repr)

        fptr.close()

        return result

    def popK(self, k: int) -> int:
        if k <= 0 or k > self.item_count:
            return 0
        item_id = self.item_count - k

        fptr = open(self.index_fspath, 'rb+')
        fptr.seek(16 * item_id, 0)
        index_repr = fptr.read(16)

        item_offset = typon_math.deserialize_int(index_repr[ 0 : 8 ])
        # item_size = typon_math.deserialize_int(index_repr[ 8 : 16 ])

        fptr.truncate(16 * item_id)
        fptr.close()

        fptr1 = open(self.data_fspath, 'rb+')
        fptr1.truncate(item_offset)
        fptr1.close()

        self.item_count -= k
        return item_id

    def clear(self):
        open(self.index_fspath, 'wb').close()
        open(self.data_fspath, 'wb').close()
        self.item_count = 0
        self.total_bytes = 0
