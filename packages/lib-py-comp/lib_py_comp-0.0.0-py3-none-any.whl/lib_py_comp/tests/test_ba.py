import lib_py_comp.dsa.byte_array as byte_array

fileName = '/home/algorithmspath/py_lib_dev/src/lib_py_comp/lib_py_comp/_data/A2'
n = 100_000
vba = byte_array.VariableBytesArray(fileName)
vba.clear()

print('--writing--')
for i in range(0, n):
    if i % 1000 == 0:
        print(i, n)
    # bw.write(str(i).encode(), sync=True)
    vba.append(str(i).encode())

print('--reading--')
for i, t in enumerate(vba.slice(0, vba.count())):
    v = int(t.decode())
    # if i % 1000 == 0:
    print(i, v, n)
    assert i == v
