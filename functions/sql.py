import sqlite3

def connect_db(db_name: str):
    """_summary_
    connect to an existent data base.
    if ont exist, it will create one. 

    Args:
        db_name (str):  a data base name.

    Returns:
        _type_: _description_
    """
    conn = sqlite3.connect(db_name)

    return conn