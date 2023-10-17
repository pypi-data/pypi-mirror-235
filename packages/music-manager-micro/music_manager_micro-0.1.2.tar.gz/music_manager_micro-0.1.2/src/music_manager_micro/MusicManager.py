import os
from pathlib import Path
from .File import File as F
import logging
import sqlite3

logging.basicConfig(
    format='%(asctime)s | %(levelname)s | %(message)s', level=logging.DEBUG)
debug = False

def __debugMessage(message):
    global debug
    if debug:
        logging.debug(str(message))
        
app_environment = {}
app_environment['app_name'] = 'MusicManagerMicro'
app_environment['version'] = '0.1.2'

app_environment['root_dir'] = default_root_dir = os.path.join(
    str(Path.home()), ".config/", app_environment['app_name'])
app_environment['library_file'] = 'library.db'
active_library = '###TESTABC###'


def instantiate_sqlite_table(file_name: str) -> sqlite3.Cursor:
    global con
    con = sqlite3.connect(file_name)
    cur = con.cursor()
    res = cur.execute("SELECT ? FROM sqlite_master", ('music',))
    is_created = res.fetchone()
    if is_created is None:
        cur.execute("CREATE TABLE music(mtime, file_path type UNIQUE)")
    return cur

def db_get_all(cur: sqlite3.Cursor) -> list:
    res = cur.execute("SELECT * FROM music")
    ret_val = res.fetchall()
    #print(f'db_get_all ret val {ret_val}')
    return [] if ret_val is None else ret_val

def db_insert(cur: sqlite3.Cursor, entry: tuple) -> None:
    sub_obj = {
        'mtime':entry[0],
        'file_path': entry[1]
    }
    res = cur.execute("INSERT INTO music(mtime,file_path) VALUES (:mtime, :file_path) ON CONFLICT(file_path) DO UPDATE SET mtime=:mtime, file_path=:file_path", sub_obj)
    return

def db_delete(cur: sqlite3.Cursor) -> None:
    res = cur.execute("DELETE FROM music")
    pass

def db_commit(con: sqlite3.Connection) -> None:
    con.commit()

def db_close(con: sqlite3.Connection) -> None:
    con.close()

###
# Config manager
###

def set_library(library_id: str) -> None:
    global active_library
    active_library = library_id
    __updateRootDir()
    if active_library == '###TESTABC###':
        return

def __constructLibraryDir(library) -> str:
    return os.path.join(
        app_environment['root_dir'], library)

def __updateRootDir() -> None:
    global app_environment
    app_environment['library_dir'] = __constructLibraryDir(active_library)
    os.makedirs(app_environment['library_dir'],exist_ok=True)

set_library(active_library)

library_root = ''

###
#Utils
###
extensions = ('.mp3','.flac')
def __getFilesFromFolder(folder: str):
    retVal = []
    for r, d, f in os.walk(folder):
        for file in f:
            if file.endswith(extensions):
                retVal.append(f'{r}/{file}')
    return retVal

###
# Program Functions
###

library_list = []

def __build_entry(file_path: str) -> str:
    """docstring"""
    try:
        file = F(file_path,'','',os.path.getmtime(file_path))
        return (file.mtime,file.path)
    except Exception as err:
        error_log = f"Error in build_entry {err=}, {type(err)=}"
        pass


def __build_list(root_path: str) -> list:
    """Given a path string constructs a list of File objects"""
    try:
        global library_list
        library_list = []
        #return library_list
        files = __getFilesFromFolder(root_path)
        __debugMessage(f"Found {len(files)} files")
        for f in files:
            #__debugMessage(f)
            library_list.append(__build_entry(f))
        #__save_list()
        return library_list
    except Exception as err:
        __debugMessage(f"Error in build_list {err=}, {type(err)=}")
        pass

def execute(library: str, root_path: str) -> list:
    set_library(library)
    return_value = __build_list(root_path)
    __save_list()
    return return_value

def reset_library(library: str) -> None:
    set_library(library)
    _file = __build_file_path()
    cur = instantiate_sqlite_table(_file)
    db_delete(cur)
    db_commit(cur.connection)
    db_close(cur.connection)

def get_list() -> list:
    __load_list()
    return library_list

def __build_file_path() -> str:
    return os.path.join(app_environment['library_dir'],app_environment['library_file'])

def __load_list() -> None:
    _file = __build_file_path()
    global library_list
    cur = instantiate_sqlite_table(_file)
    library_list = db_get_all(cur)
    pass

def __save_list() -> None:
    """Uses a filepath + filename string and content string overwrites the resulting file"""
    try:
        content = library_list
        write_file = __build_file_path()
        if os.path.dirname(write_file) != '':
            os.makedirs(os.path.dirname(write_file), exist_ok=True)
        cur = instantiate_sqlite_table(write_file)
        for x in content:
            __debugMessage(f'Inserting {x}')
            db_insert(cur, x)
        db_commit(cur.connection)
        db_close(cur.connection)
    except Exception as e:
        print(f'caught {type(e)}: {e}')
        return False

