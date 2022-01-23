
import os
import message_parse
import threading
import pandas as pd
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import KFold
'''
Возможно стоит сделать класс csv_table наследуемым от класса dataset, если в dataset будет метод
кросс валидации и определения fold то в классе  csv_table можно будет его переопределеить
'''
class Table_csv_formation:
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
            datafreme_message = self.strat_Fold(datafreme_message)
            '''
            Если мы сдесть переопределяем fold  то именно функцию create_csv_file мы сделаем в классе которую будет в классе который наследуется от Csv_table
            '''
            yield datafreme_message

    def create_datafreme(self, parse):
        dataset_message = pd.DataFrame()
        for i, step_dataset in enumerate(parse):
            #print(i, step_dataset[0], step_dataset[1])
            dataset_message.loc[i, 'from_name'] = step_dataset[1]
            dataset_message.loc[i, 'text'] = step_dataset[0]
        return dataset_message

    def strat_Fold(self, datafreme_message):
        '''
        Мы должны предпочесть StratifiedKFold, а не KFold, когда имеем дело с задачами классификации с несбалансированным
        распределением классов
        '''
        # n_splits=5, random_state=42 они должны определяться в файле header_variable
        #skfolds = StratifiedKFold(n_splits=5, random_state=42, shuffle = True)
        kfolds = KFold(n_splits=5, shuffle=True, random_state=42)

        for num_fold, (train_index, val_index) in enumerate(kfolds.split(datafreme_message)):
            datafreme_message.loc[val_index, 'fold'] = int(num_fold)

        return datafreme_message


class Table_csv_alternative_form(Table_csv_formation):

    def strat_Fold(self, datafreme_message):

        kfolds = KFold(n_splits=3, shuffle=True, random_state=42)
        # мы должны вызвать метод родительсткого класса для формирования datafreme_message для этого используем super
        for num_fold, (train_index, val_index) in enumerate(kfolds.split(datafreme_message)):
            datafreme_message.loc[val_index, 'fold'] = int(num_fold)

        return datafreme_message


