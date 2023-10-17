import lib_py_comp.dsa.kv_db as kv_db

fileName = '/home/algorithmspath/py_lib_dev/src/lib_py_comp/lib_py_comp/_data/A3'
n = 100_000
kv = kv_db.KeyValueDB(fileName)
# kv.clear()

print('--writing--')
for i in range(0, n):
    if i % 1000 == 0:
        print(i, n)
    # bw.write(str(i).encode(), sync=True)
    kv.put(str(i).encode(), str(2*i).encode())

print('--reading--')
for i, t in enumerate(kv):
    k, v = t
    print(t)
    k = int(bytes(k).decode())
    v = int(bytes(v).decode())
    # if i % 1000 == 0:
    print(i, v, n)
    assert 2 * k == v
