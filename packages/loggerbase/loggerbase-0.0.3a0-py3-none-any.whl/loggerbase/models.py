from collections import namedtuple

LoggerDBSettings = namedtuple('LoggerSettings', [
    'engine',
    'database',
    'host',
    'port',
    'username',
    'password',
    'table'
])

ConsoleHandlerConf = namedtuple('ConsoleHandlerConf', [
    'level',
    'text_format'
])

FileHandlerConf = namedtuple('FileHandlerConf', [
    'level',
    'text_format',
    'file_path',
    'prefix',
])

LoggerFrame = namedtuple('LoggerFrame', [
    'module',
    'function',
    'line_number',
    'file_name',
    'frame_before',
    'is_exception'
])
