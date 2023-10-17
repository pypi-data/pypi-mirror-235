import lib_py_comp.dsa.delimited_io as delimited_io

fileName = '/home/algorithmspath/py_lib_dev/src/lib_py_comp/lib_py_comp/_data/A1'
bufferSize = 10000
delimiter = ','
bw = delimited_io.DelimitedWriter(fileName, bufferSize, delimiter)
bw.clear()
n = 100_000

print('--writing--')
for i in range(0, n):
    if i % 1000 == 0:
        print(i, n)
    bw.write(str(i).encode())
del bw

print('--reading--')
br = delimited_io.DelimitedReader(fileName, bufferSize, delimiter)
for i, t in enumerate(br):
    v = int(t.decode())
    # if i % 1000 == 0:
    print(i, v, n)
    assert i == v
