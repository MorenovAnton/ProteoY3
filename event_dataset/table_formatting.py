
import os
import message_parse
import threading
import pandas as pd
'''
Возможно стоит сделать класс csv_table наследуемым от класса dataset, если в dataset будет метод
кросс валидации и определения fold то в классе  csv_table можно будет его переопределеить
'''
class Csv_table:
    def __init__(self, message_pool):
        self.message_pool = message_pool                        # ../ProteoY3/message_pool/telegram/

    def create_csv_file(self):
        listd_message = os.listdir(self.message_pool)           # лист с названиями html файлов в которых содержится мообщения
        for message in listd_message:
            print("----------------------------------------------------------------------------------------->", message)
            messages_file = self.message_pool + message         # Полный путь к файлу
            class_parse = message_parse.Message_parsing(messages_file)
            parse = class_parse.parse_messages_telefram_file()  # generator parsing file
            #parse = threading.Thread(target = class_parse.parse_messages_telefram_file, args = ())
            #parse.start()
            datafreme_message = self.create_datafreme(parse)
            yield datafreme_message

    def create_datafreme(self, parse):
        dataset_message = pd.DataFrame()
        for i, step_dataset in enumerate(parse):
            #print(i, step_dataset[0], step_dataset[1])
            dataset_message.loc[i, 'from_name'] = step_dataset[1]
            dataset_message.loc[i, 'text'] = step_dataset[0]

        return dataset_message












