import header_variable
import os
import sys
import threading

list_message = header_variable.MESSAGE_PATH
parse_module = header_variable.PARSE_MODULE_PATH
listd_message = os.listdir(list_message)               # лист с названиями html файлов в которых содержится мообщения
# после определения пути к модулю message_parse_import_module который определен в header_variable добавляем его
sys.path.append(parse_module)
from message_parse_import_module import message_parse





def create_csv_file(listd_message):
    for message in listd_message[:1]:
        messages_file = list_message + message
        class_parse = message_parse.Message_parsing(messages_file)
        #print(class_parse.parse_messages_file(messages_file))
        t = threading.Thread(target = class_parse.parse_messages_file, args = ())
        t.start()





create_csv_file(listd_message)

