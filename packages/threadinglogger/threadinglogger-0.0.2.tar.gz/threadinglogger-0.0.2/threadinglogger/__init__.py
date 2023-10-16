import inspect
import multiprocessing
import ctypes
import sys
import os
from datetime import datetime
import threading
import queue
import enum

__is_module_psycopg2 = False
try:
    import psycopg2
    __is_module_psycopg2 = True
except ModuleNotFoundError as e:
    print(f"{e}, __is_module_psycopg2:{__is_module_psycopg2}")

from contextlib import contextmanager

####################################################################################################################
####################################################################################################################
####################################################################################################################
# Variables - Common ###############################################################################################
__is_running = multiprocessing.Value(ctypes.c_bool, False)
__command_thread : threading.Thread = None
__command_queue : queue.Queue = None

__DEFAULT_FILE_EXTENSION = 'log'
__DEFAULT_FILE_DATE_FORMAT = '%Y%m%d%H%M%S'
__DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S.%f'
__DEFAULT_LOG_FORMAT = "{date_str} " +\
                    "{thread_id:0{thread_id_length}d}:TID " +\
                    "{log_type:{log_type_length}} " +\
                    "{file_name:>{file_name_length}}:{file_lineno:<{file_lineno_length}} " +\
                    "{text}"

__DEFAULT_THREAD_ID_LENGTH = 6
__DEFAULT_LOG_TYPE_LENGTH = 4
__DEFAULT_FILE_NAME_LENGTH = 4
__DEFAULT_FILE_LINENO_LENGTH = 5

class __LogType:
    NONE = ''
    FINISH = 'FINISH'    
    INFORMATION = 'INFORMATION'

def __get_log_dict(
        command: str = "log",
        log_type : str = "",
        log_type_length : int = 0,
        timestamp : float = 0,
        date_format : str = "",
        thread_id : int = 0,
        thread_id_length : int = 0,
        process_id : int = 0,
        file_name : str =  "",
        file_name_length : int = 0,
        file_lineno : int = 0,
        file_lineno_length : int = 0,
        text : str = "",
        output_format : str = "",
        is_print : bool = None,
        is_write : bool = None,
        is_insert : bool = None,
    ):
    
    if timestamp == 0:
        timestamp = datetime.now().timestamp()
        
    if thread_id == 0:
        thread_id = threading.current_thread().ident
        
    if process_id == 0:
        process_id = os.getpid()
    
        
    return {
        'command' : command,
        'log_type' : log_type,
        'log_type_length' : log_type_length,
        'timestamp' : timestamp,
        'date_format' : date_format,
        'thread_id' : thread_id,
        'thread_id_length' : thread_id_length,
        'process_id' : process_id,
        'file_name' : file_name,
        'file_name_length' : file_name_length,
        'file_lineno' : file_lineno,
        'file_lineno_length' : file_lineno_length,
        'text' : text,
        'output_format' : output_format,
        'is_print' : is_print,
        'is_write' : is_write,
        'is_insert' : is_insert
    }


####################################################################################################################
# Variables - Print Console ########################################################################################
__is_print_console = multiprocessing.Value(ctypes.c_bool, True)

__print_date_formatter = multiprocessing.Value(ctypes.c_wchar_p, __DEFAULT_DATE_FORMAT)
__print_thread_id_length = multiprocessing.Value(ctypes.c_int, __DEFAULT_THREAD_ID_LENGTH)
__print_log_type_length = multiprocessing.Value(ctypes.c_int, __DEFAULT_LOG_TYPE_LENGTH)
__print_file_name_length = multiprocessing.Value(ctypes.c_int, __DEFAULT_FILE_NAME_LENGTH)
__print_file_lineno_length = multiprocessing.Value(ctypes.c_int, __DEFAULT_FILE_LINENO_LENGTH)
                    
__print_formatter = __DEFAULT_LOG_FORMAT

####################################################################################################################
# Variables - Write File ###########################################################################################
__is_write_file = multiprocessing.Value(ctypes.c_bool, True)

__write_file_name = ""
__write_file_extension = ""
__write_file_path = ""

__write_file_max_size = multiprocessing.Value(ctypes.c_int, 100*1024)
__write_date_formatter = multiprocessing.Value(ctypes.c_wchar_p, __DEFAULT_DATE_FORMAT)
__write_thread_id_length = multiprocessing.Value(ctypes.c_int, __DEFAULT_THREAD_ID_LENGTH)
__write_log_type_length = multiprocessing.Value(ctypes.c_int, __DEFAULT_LOG_TYPE_LENGTH)
__write_file_name_length = multiprocessing.Value(ctypes.c_int, __DEFAULT_FILE_NAME_LENGTH)
__write_file_lineno_length = multiprocessing.Value(ctypes.c_int, __DEFAULT_FILE_LINENO_LENGTH)

__write_formatter = __DEFAULT_LOG_FORMAT

####################################################################################################################
# Variables - Insert PostgreSQL ####################################################################################
__is_insert_postgresql = multiprocessing.Value(ctypes.c_bool, False)
__pg_conn = None
__pg_dsn = None
__pg_table_name:str = ""


__log_column_type_dict = {
    'log_type' : 'text',
    'timestamp' : 'numeric(18, 6)',
    'thread_id' : 'bigint',
    'process_id' : 'integer',
    'file_name' : 'text',
    'file_lineno' : 'integer',
    'text' : 'text'
}
    
class __LogRow:
    log_type:str = ''
    timestamp : float = 0
    thread_id : int = 0
    process_id : int = 0
    file_name : str =  ""
    file_lineno : int = 0
    text : str = ""


####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
# Common

def is_running():
    return __is_running.value

def is_foreground_running():
    is_foreground_running = False
    try:
        fileno = sys.stdout.fileno()
        pgrp = os.getpgrp()
        tcpgrp = os.tcgetpgrp(fileno)
        if pgrp == tcpgrp:
            is_foreground_running = True
    except IOError:
        is_foreground_running = False
    return is_foreground_running    

def start():
    global __command_thread
    global __command_queue
    
    __is_running.value = True
    __is_print_console.value = is_foreground_running()
    
    __command_queue = queue.Queue()
    __command_thread = threading.Thread(target=__command_threading)
    __command_thread.start()
    
    if is_print_console() or is_write_file() or is_insert_postgresql():
        information("Logger start.")
    else:
        information("Logger pending start. All log is disabled.")
    
def stop():
    if __is_running.value:
        __is_running.value = False
    __command_queue.put(None)
    __command_thread.join()
    
    if __pg_conn:
        __pg_conn.close()
    
    __log_for_logger("Logger stop")
    
def information(*values:object, is_print : bool = None, is_write : bool = None, is_insert : bool = None):
    __put_log(__LogType.INFORMATION, *values, is_print=is_print, is_write=is_write, is_insert=is_insert)

def __put_log(log_type:str, *values:object, is_print : bool = None, is_write : bool = None, is_insert : bool = None):
    str_list = []
    for t in values:
        str_list.append(str(t))
    text = ' '.join(str_list)
    
    frame_stack = inspect.stack()
    caller_frame = frame_stack[2]
    splitted_caller_filename = caller_frame.filename.split('/')
    caller_filename = splitted_caller_filename[-1]
    if caller_filename == '__init__.py':
        caller_filename = '/' + splitted_caller_filename[-2]
    
    log_dict = __get_log_dict(
        log_type= log_type,
        text= text,
        file_name= caller_filename,
        file_lineno= caller_frame.lineno,
        is_print= is_print,
        is_write= is_write,
        is_insert= is_insert
    )
    __command_queue.put(log_dict)


####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
# Logger


def __logging(log_dict:dict):
    is_print = is_print_console()
    if log_dict['is_print'] is not None:
        is_print = log_dict['is_print']
    
    is_write = is_write_file()
    if log_dict['is_write'] is not None:
        is_write = log_dict['is_write']
    
    is_insert = is_insert_postgresql()
    if log_dict['is_insert'] is not None:
        is_insert = log_dict['is_insert']
    
    if log_dict['date_format'] != "":
        date_str = datetime.fromtimestamp(log_dict['timestamp']).strftime(log_dict['date_format'])
        log_dict['date_str'] = date_str
        
    if is_print: __print(log_dict.copy())
    if is_write: __write(log_dict.copy())
    if is_insert: __insert_pg_row(log_dict)
        

def __command_work(command_dict:dict):
    global __print_formatter
    global __write_formatter
    
    if command_dict['command'] == "log":
        __logging(command_dict)
    
    elif command_dict['command'] == "change_formatter":
        if command_dict['formatter_type'] == 'print':
            __print_formatter = command_dict['formatter']
        
        elif command_dict['formatter_type'] == 'write':
            __write_formatter = command_dict['formatter']
            
    elif command_dict['command'] == "change_file_name":
        pass

def __command_threading():
    while is_running():
        command_dict:dict = __command_queue.get()
        if not command_dict:
            continue
        __command_work(command_dict)
        
    while not __command_queue.empty():
        command_dict:dict = __command_queue.get()
        if not command_dict:
            continue
        __command_work(command_dict)
    
    __log_for_logger("Finish Log Thread")

def __log_for_logger(*values:object):
    str_list = []
    for t in values:
        str_list.append(str(t))
    text = ' '.join(str_list)
    
    frame_stack = inspect.stack()
    caller_frame = frame_stack[1]
    splitted_caller_filename = caller_frame.filename.split('/')
    caller_filename = splitted_caller_filename[-1]
    if caller_filename == '__init__.py':
        caller_filename = '/' + splitted_caller_filename[-2]
    
    finish_message = __get_log_dict(text= text, log_type=__LogType.FINISH, file_name=caller_filename, file_lineno= caller_frame.lineno)
    __logging(finish_message)

####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
# Print Console

def is_print_console(): return __is_print_console.value
def enable_print_console(): __is_print_console.value = True
def disable_print_console(): __is_print_console.value = False

def change_print_format(output_format:str):
    '''
    Change console print format string\n
    No sync with logging.\n
    Parameters
    -
    output_format (str): new formatting string\n
    
    Formatting Example
    -
    "{date_str} {log_type:{log_type_length}} {thread_id:0{thread_id_length}d} {text}"\n
    Variables
    -
    log_type\n
    log_type_length\n
    date_str\n
    thread_id\n
    thread_id_length\n
    process_id\n
    file_name\n
    file_name_length\n
    file_lineno\n
    file_lineno_length\n
    text\n
    '''
    __command_queue.put({
        'command' : 'change_formatter',
        'formatter_type' : 'print',
        'formatter' : output_format
    })

#########################
#########################
#########################
#########################
#########################
#########################
#########################
def __print(log_dict:dict):
    if log_dict['date_format'] == "":
        date_str = datetime.fromtimestamp(log_dict['timestamp']).strftime(__print_date_formatter.value)
        log_dict['date_str'] = date_str
    
    if log_dict['thread_id_length'] == 0:
        thread_id = log_dict['thread_id']
        thread_id_length = __print_thread_id_length.value
        log_dict['thread_id'] = thread_id%(10**thread_id_length)
        log_dict['thread_id_length'] = thread_id_length
    
    if log_dict['log_type_length'] == 0:
        log_type_split_length = len(log_dict['log_type']) if len(log_dict['log_type']) < __print_log_type_length.value else __print_log_type_length.value
        log_dict['log_type'] = log_dict['log_type'][:log_type_split_length]
        log_dict['log_type_length'] = __print_log_type_length.value
    
    if log_dict['file_name_length'] == 0:
        file_name = log_dict['file_name']
        if __print_file_name_length.value < len(file_name):
            __print_file_name_length.value = len(file_name)
        log_dict['file_name_length'] = __print_file_name_length.value
        
    if log_dict['file_lineno_length'] == 0:
        file_lineno_str = str(log_dict['file_lineno'])
        if __print_file_lineno_length.value < len(file_lineno_str):
            __print_file_lineno_length.value = len(file_lineno_str)
        log_dict['file_lineno_length'] = __print_file_lineno_length.value
                                
    log_text = ""
    if log_dict['output_format'] == "":
        log_text = __print_formatter.format(**log_dict)
    else:
        log_text = log_dict['output_format'].format(**log_dict)
    print(log_text, flush=True)
        



####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
# Write File
def init_file_writer(write_file_name:str, write_file_path:str='.', write_file_extension:str=__DEFAULT_FILE_EXTENSION):
    '''
    Parameters
    -
    write_file_name (str): file name.
    write_file_path (str): file path. default is '.'(current dir)
    write_file_extension (str): file extension. default is 'log'
    '''

    if not isinstance(write_file_name, str):
        raise TypeError(f"file_name('{write_file_name}') type error. {type(write_file_name)} to {str}")
    if not isinstance(write_file_path, str):
        raise TypeError(f"file_path('{write_file_path}') type error. {type(write_file_path)} to {str}")
    if not isinstance(write_file_extension, str):
        raise TypeError(f"file_extension('{write_file_extension}') type error. {type(write_file_extension)} to {str}")
    
    global __write_file_name
    global __write_file_extension
    global __write_file_path
    
    enable_write_file()
    
    __write_file_name = write_file_name
    __write_file_extension = write_file_extension
    __write_file_path = __get_absolute_path_from_caller(write_file_path)
    if not os.path.exists(__write_file_path):
        raise FileExistsError(f"not exists '{__write_file_path}'")
    if not os.path.isdir(__write_file_path):
        raise NotADirectoryError(f"not a directory '{__write_file_path}'")
        
def enable_write_file():
    '''
    Enable write file.
    No sync with logging.\n
    If need sync, change this before 'start' or set 'is_write' each log.\n
    '''
    __is_write_file.value = True
    
def disable_write_file(): 
    '''
    Disable write file.\n
    No sync with logging.
    If need sync, change this before 'start' or set 'is_write' each log. 
    '''
    __is_write_file.value = False
    
def is_write_file() -> bool: return __is_write_file.value

def change_file_name(file_name:str):
    __command_queue.put({
        'command' : 'change_file_name',
        'file_name' : file_name
    })
    
def change_write_format(output_format:str):
    '''
    Change file write format string\n
    No sync with logging.\n
    Parameters
    -
    output_format (str): new formatting string\n
    
    Formatting Example
    -
    "{date_str} {log_type:{log_type_length}} {thread_id:0{thread_id_length}d} {text}"\n
    Variables
    -
    log_type\n
    log_type_length\n
    date_str\n
    thread_id\n
    thread_id_length\n
    process_id\n
    file_name\n
    file_name_length\n
    file_lineno\n
    file_lineno_length\n
    text\n
    '''
    __command_queue.put({
        'command' : 'change_formatter',
        'formatter_type' : 'write',
        'formatter' : output_format
    })

def change_file_max_size(max_size:int):
    __write_file_max_size.value = max_size

def __get_absolute_path_from_caller(src_path:str) -> str:
    dst_path = src_path
    if dst_path == '':
        dst_path = '.'
        
    spiltted_dst_path = dst_path.split('/')
    
    if spiltted_dst_path[0] == '~':
        dst_path = os.path.expanduser(dst_path)
        
    elif spiltted_dst_path[0] == '..':
        stacks = inspect.stack()
        caller_frame = stacks[2]
        splited_frame_path = caller_frame.filename.split('/')
        joined_frame_path = '/'.join(splited_frame_path[:-2])
        dst_path = joined_frame_path + (dst_path[2:] if 2<len(dst_path) else "")
        
    elif spiltted_dst_path[0] == '.':
        stacks = inspect.stack()
        caller_frame = stacks[2]
        splited_frame_path = caller_frame.filename.split('/')
        joined_frame_path = '/'.join(splited_frame_path[:-1])
        dst_path = joined_frame_path + (dst_path[1:] if 1<len(dst_path) else "")
    
    return dst_path

#########################
#########################
#########################
#########################
#########################
#########################
#########################
def __write(log_dict:dict):
    if log_dict['date_format'] == "":
        date_str = datetime.fromtimestamp(log_dict['timestamp']).strftime(__write_date_formatter.value)
        log_dict['date_str'] = date_str
        
    if log_dict['thread_id_length'] == 0:
        thread_id = log_dict['thread_id']
        thread_id_length = __write_thread_id_length.value
        log_dict['thread_id'] = thread_id%(10**thread_id_length)
        log_dict['thread_id_length'] = thread_id_length
    
    if log_dict['log_type_length'] == 0:
        log_type_split_length = len(log_dict['log_type']) if len(log_dict['log_type']) < __write_log_type_length.value else __write_log_type_length.value
        log_dict['log_type'] = log_dict['log_type'][:log_type_split_length]
        log_dict['log_type_length'] = __write_log_type_length.value
    
    if log_dict['file_name_length'] == 0:
        file_name = log_dict['file_name']
        if __write_file_name_length.value < len(file_name):
            __write_file_name_length.value = len(file_name)
        log_dict['file_name_length'] = __write_file_name_length.value
        
    if log_dict['file_lineno_length'] == 0:
        file_lineno_str = str(log_dict['file_lineno'])
        if __write_file_lineno_length.value < len(file_lineno_str):
            __write_file_lineno_length.value = len(file_lineno_str)
        log_dict['file_lineno_length'] = __write_file_lineno_length.value
                                
    log_text = ""
    if log_dict['output_format'] == "":
        log_text = __write_formatter.format(**log_dict)
    else:
        log_text = log_dict['output_format'].format(**log_dict)
    
    logging_file_full_path = f"{__write_file_path}/{__write_file_name}.logging.{__write_file_extension}"
    with open(logging_file_full_path, 'a') as logging_file:
        logging_file.write(f"{log_text}\n")
    
    if __write_file_max_size.value < os.path.getsize(logging_file_full_path):
        save_date_str = datetime.strftime(datetime.now(), f"{__DEFAULT_FILE_DATE_FORMAT}")
        change_path = f"{__write_file_path}/{__write_file_name}.{save_date_str}.{__write_file_extension}"
        os.rename(logging_file_full_path, change_path)


####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
# insert PostrgreSQL

def is_insert_postgresql(): return __is_insert_postgresql.value
def enable_insert_postgresql(): __is_insert_postgresql.value = True
def disable_insert_postgresql(): __is_insert_postgresql.value = False

def init_postgresql(host:str, port:int, database_name:str, table_name:str, user_id:str, password:str):
    if __is_module_psycopg2:
        global __pg_conn
        global __pg_dsn
        global __pg_table_name
        
        __dsn = psycopg2.extensions.make_dsn(host=host, port=port, dbname=database_name, user=user_id, password=password)
        psycopg2.connect(__dsn)
        __pg_conn = psycopg2.connect(__dsn)
        __pg_conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        __pg_table_name = table_name.replace(' ', '')
        
        if not is_exist_pg_table(table_name):
            create_pg_table(table_name)
        
        enable_insert_postgresql()
        
    else:
        __log_for_logger(f"Ignore initialize postgresql. Need 'psycopg2' module.")
        disable_insert_postgresql()
        
@contextmanager
def __get_pg_conn():
    cursor = __pg_conn.cursor()
    try:
        yield cursor, __pg_conn
    finally:
        cursor.close()

def is_exist_pg_table(table_name:str, table_schema = 'public') -> bool:
    result = False
    query = f"SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = '{table_schema}' AND table_name = '{table_name}');"
    with __get_pg_conn() as (_cursor, _):
        _cursor.execute(query)
        result_fetch = _cursor.fetchone()
        result = result_fetch[0]
    return result
    
def create_pg_table(table_name:str):
    query = f"CREATE TABLE {table_name} ("
    for column_name in __log_column_type_dict:
        query += f"{column_name} {__log_column_type_dict[column_name]},"
    query = query[:-1] + ")"
    with __get_pg_conn() as (_cursor, _):
        _cursor.execute(query)

def drop_pg_table(table_name:str):
    query = f"DROP TABLE {table_name}"
    with __get_pg_conn() as (_cursor, _):
        _cursor.execute(query)

def __convert_value_to_query(value, is_in_list = False) -> str:
    value_query = ''
    
    is_value_list = isinstance(value, list)
    if is_value_list:
        if not is_in_list:
            value_query += "'"
        value_query += "{"
        for v in value:
            value_query += f"{__convert_value_to_query(v, True)},"
            
        value_query = value_query[:-1]
        value_query += "}"
        if not is_in_list:
            value_query += "'"
        value_query += ","
    else:
        if isinstance(value, str):
            if is_in_list:
                value_query += f'"{value}",'
            else:
                value_query += f"'{value}',"
        elif isinstance(value, bool):
            if value:
                value_query += f'true,'
            else:
                value_query += f'false,'
        else:
            value_query += f"{value},"
        
    return value_query[:-1]

def __insert_pg_row(log_dict:dict):
    insert_dict = {}
    for column_name in __log_column_type_dict:
        if column_name in log_dict:
            insert_dict[column_name] = log_dict[column_name]
    
    column_names = ''
    values = ''
    for column_name in insert_dict:
        if insert_dict[column_name] is not None:
            column_names += f"{column_name},"
            values += f"{__convert_value_to_query(insert_dict[column_name])},"
            
    query = f"INSERT INTO {__pg_table_name} ({column_names[:-1]}) VALUES ({values[:-1]});"
    with __get_pg_conn() as (_cursor, _):
        _cursor.execute(query)