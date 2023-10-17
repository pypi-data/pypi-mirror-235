# threadinglogger
Logger using a thread.  
Log Type : print console, write file, insert postgresql

## Start and Stop
```python
import threadinglogger
threadinglogger.start()
# code...
threadinglogger.stop()
```

## Log
Default is print console only.
```python  
threadinglogger.information("Hello, world!")
threadinglogger.exception("Hello, world!")
# exception() output 'traceback.format_exc()' next line of message if exists.
threadinglogger.signal("Hello, world!")
threadinglogger.other("OTHER", "Hello, world!")
```

## Initialize Print console.
Default is enable.  
Set disable auto if process run background.  
Excute before 'start()'.  
```python  
import threadinglogger
threadinglogger.enable_print_console()
# or
threadinglogger.disable_print_console()
```
## Initialize Write file.
Default is disable.  
Set enable auto if success run 'init_write_file()'.  
Excute before 'start()'.  
```python  
# {write_file_name}.logging.log
threadinglogger.init_write_file(write_file_name= "test")
# change path. default is '.'(current path)
threadinglogger.init_write_file(write_file_name= "test", write_file_path='./logs')
# change extension. default is 'log'
threadinglogger.init_write_file(write_file_name= "test", write_file_path='./logs', write_file_extension= 'txt')
```
## Initialize Insert PostgreSQL.
Default is disable.  
Set enable auto if success run 'init_postgresql()'.  
Excute before 'start()'.  
```python
def init_postgresql(host:str, port:int, database_name:str, table_name:str, user_id:str, password:str):
```

## Change Format
Change format string.  
No sync with logging.  

Format Variables:  
log_type  
log_type_length  
date_str  
thread_id  
thread_id_length  
process_id  
file_name  
file_name_length  
file_lineno  
file_lineno_length  
text  
  
Default:
```python  
"{date_str} {thread_id:0{len_thread_id}d}:TID {log_type:{len_log_type}} {file_name:>{maxlen_file_name}}:{file_lineno:<{maxlen_file_lineno}} {text}"
```
Output:  
'2100-01-01 18:02:47.047984 123456:TID INFO /dir:272 Message'  

Change:
```python
output_format = "{date_str} {log_type:{log_type_length}} {text}"
threadinglogger.change_print_format(output_format)
threadinglogger.change_write_format(output_format)
```
Output:  
'2100-01-01 18:02:47.047984 INFO Message'  

### Change Date Format
Default is '%Y-%m-%d %H:%M:%S.%f'
```python  
threadinglogger.change_date_format_print_console('%H:%M:%S')
threadinglogger.change_date_format_write_file('%H:%M:%S')
```

### Change Thread ID Lenght Format
Default is 6
```python  
threadinglogger.change_thread_id_length_print_console(4)
threadinglogger.change_thread_id_length_write_file(4)
```  

### Change Log Type Length
Default is 4
```python
threadinglogger.change_log_type_length_print_console(5)
threadinglogger.change_log_type_length_write_file(5)
```  