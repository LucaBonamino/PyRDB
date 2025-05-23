import struct

from PyRDB.settings import DB_PATH


def create_index_file():

    # Build a single leaf node with 2 entries for keys=1,2
    node = struct.pack(
        ">B H I I Q Q",
        1,  # is_leaf
        2,  # num_keys
        1,  # key[0]
        2,  # key[1]
        0,  # ptr[0] = row_number 0 * 64
        64  # ptr[1] = row_number 1 * 64
    )

    f_name = DB_PATH / "employers_id.idx"
    with f_name.open("wb") as f:
        f.write(node)



def parse_btree_leaf():
    f_name = DB_PATH / "employers_id.idx"
    with f_name.open("rb") as f:
        data = f.read()
    print(data)
    # Header: is_leaf , num_keys
    is_leaf, num_keys = struct.unpack_from(">BH", data, 0)
    assert is_leaf == 1, "Not a leaf node"

    # Keys: num_keys × 4‐byte uint
    offset = 3
    keys_fmt  = ">" + "i"*num_keys
    keys_size = 4 * num_keys
    keys = struct.unpack_from(keys_fmt, data, offset)
    print(keys)
    offset += keys_size

    # Ptrs: num_keys × 8‐byte uint
    ptrs_fmt  = ">" + "Q"*num_keys
    ptrs_size = 8 * num_keys
    ptrs = struct.unpack_from(ptrs_fmt, data, offset)

    print(f"Leaf node with {num_keys} keys:\n")
    print(f"{'Index':>5} │ {'Key':>8} │ {'Ptr (byte offset)':>16}")
    print("──────┼──────────┼────────────────────")
    for i, (k, p) in enumerate(zip(keys, ptrs)):
        print(f"{i:5d} │ {k:8d} │ {p:16d}")






create_index_file()
parse_btree_leaf()
