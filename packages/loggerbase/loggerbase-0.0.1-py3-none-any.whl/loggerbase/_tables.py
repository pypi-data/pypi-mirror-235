from datetime import datetime
from functools import lru_cache

from sqlalchemy import Column, Integer, String, Text, DateTime, Sequence

table_columns = {
    "__default__": (
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('level', String(10)),
        Column('message', Text),
        Column('logger', String(255)),
        Column('function', String(255)),
        Column('module', Text),
        Column('line_number', Integer),
        Column('file_name', String(255)),
        Column('frame_before', String(255)),
        Column('main_script', String(255)),
        Column('created_at', DateTime, default=datetime.utcnow)
    ),
    "oracle": (
        Column('id', Sequence('logger_sequence', start=1, increment=1)),
        Column('level', String(16)),
        Column('message', Text),
        Column('logger', String(255)),
        Column('function', String(255)),
        Column('module', Text),
        Column('line_number', Integer),
        Column('file_name', String(255)),
        Column('frame_before', String(255)),
        Column('main_script', String(255)),
        Column('created_at', DateTime, default=datetime.utcnow)
    )
}


@lru_cache()
def get_columns(engine: str):
    for engine_type, cols in table_columns.items():
        if engine_type in engine:
            return cols
    return table_columns["__default__"]
