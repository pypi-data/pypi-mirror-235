import lib_py_comp.dsa.buffered_io as buffered_io

fileName = '/home/algorithmspath/py_lib_dev/src/lib_py_comp/lib_py_comp/_data/A1'
bufferSize = 10000
bw = buffered_io.BufferedWriter(fileName, bufferSize)
bw.clear()
n = 100_000

print('--writing--')
for i in range(0, n):
    if i % 1000 == 0:
        print(i, n)
    # bw.write(str(i).encode(), sync=True)
    bw.write(str(i).encode())
del bw

print('--reading--')
br = buffered_io.BufferedReader(fileName, bufferSize)
for i, t in enumerate(br):
    v = int(t.decode())
    # if i % 1000 == 0:
    print(i, v, n)
    assert i == v
