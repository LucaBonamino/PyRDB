import json
import struct
from typing import List

from PyRDB.entities.schema import Table, Column
from PyRDB.settings import DB_PATH, ROOT_PATH

def get_table(table_name: str) -> Table:
    with (ROOT_PATH / "schema.json").open('r') as f:
        schema = json.load(f)
    table = schema["tables"].get(table_name)
    return Table.model_validate(table)

def pad_value(value: int | str, size: int):
    return str(value).encode('utf-8').ljust(size, b'\x00')

def unpad_value(value: bytes) -> str:
    return value.decode("utf-8").rstrip('\x00')

def prepare_item(item: int | str , idx: int, columns: List[Column]):
    if columns[idx].data_type == "integer":
        return item
    elif columns[idx].data_type == 'varchar':
        return pad_value(item, columns[idx].size)


class DBQuerier:

    @staticmethod
    def insert_into(table_name, data: List[dict]):
        table = get_table(table_name)
        table_file = DB_PATH / f"{table.table_name}.bin"
        with table_file.open("ab") as f:
            for item in data:
                row = [prepare_item(v, idx, table.columns) for idx, (k,v) in enumerate(item.items())]
                packed = struct.pack(table.struct_type, *row)
                f.write(packed)

    @staticmethod
    def select_from(table_name: str):
        table = get_table(table_name)
        table_file = DB_PATH / f"{table.table_name}.bin"
        out = []
        with table_file.open("rb") as f:
            while chunck := f.read(table.row_size):
                id, name = struct.unpack(table.struct_type, chunck)
                out.append((id, unpad_value(name)))
        return out

