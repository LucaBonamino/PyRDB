from typing import Optional, List

import pydantic


class Column(pydantic.BaseModel):
    column_name: str
    column_memory_offset: int
    data_type: str
    size: int
    struct_type: str
    nullable: Optional[bool] = None

class ForeignKey(pydantic.BaseModel):
    references: str

class Table(pydantic.BaseModel):
    table_name: str
    row_size: int
    struct_type: str
    columns: List[Column]