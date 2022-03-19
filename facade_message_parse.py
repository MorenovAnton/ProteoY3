import bs4
import re
import os
import pandas as pd
import string
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import KFold
import header_variable
nltk.download('stopwords')

class Facade:
    def __init__(self, subsystem_message) -> None:
        self.subsystem_message = subsystem_message or Message()
        # здесь объявление еще одного класса, который будет обрабатывать сообщения, если препроцессинг который
        # объявлен в https://www.kaggle.com/morenovanton/test-getting-started-with-chatbot пункт Pre-processing all
        # будет реализован в отдельном классе, если он в итоге будет реализован в Message классе, то еще одного субсистемы объвленно не будет
        # при этом пункт приведения к нижнему регистру будет реализован в  Message классе, методе message_filtering_by_source

    def operation_message_preprocessing(self):
        collection_dialogues = self.subsystem_message.create_csv_file()
        return collection_dialogues


class Message:
    def __init__(self, message_pool, token_length):
        self.message_pool = message_pool
        self.token_length = token_length

    def create_csv_file(self):
        # listd_message это свойство сделай приватным
        listd_message = os.listdir(self.message_pool)      # лист с названиями html файлов в которых содержится
        for message in listd_message:
            print("---------------------------------------------------------------------------------->", message)
            messages_file = self.message_pool + message         # Полный путь к файлу
            parse = self.parse_messages_telefram_file(messages_file)
            datafreme_message = self.create_datafreme(parse)
            #datafreme_message = self.strat_Fold(datafreme_message)
            # кроме самого сформированного датафрейма, возвращаем еще и название файла из которого они вытяны
            yield (datafreme_message, message)
            #yield parse


    def parse_messages_telefram_file(self, messages_file):
        with open(messages_file, encoding='utf-8') as inf:
            '''
            https://www.crummy.com/software/BeautifulSoup/bs4/doc/
            Beautiful Soup - это пакет Python для анализа документов HTML и XML. Он создает дерево синтаксического анализа 
            для проанализированных страниц, которое можно использовать для извлечения данных из HTML, что полезно для 
            парсинга веб-страниц.
            '''
            soup = bs4.BeautifulSoup(inf.read(), features="html.parser")
            text = soup.find_all('div', class_='text')
            from_name = soup.find_all('div', class_='from_name')

            filtering = self.message_filtering_by_source(text, from_name)

            for name_autor, message_text in filtering:
                yield [name_autor, message_text]


    def message_filtering_by_source(self, text, from_name):
        remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation) # это свойство сделай приватным
        stopword_list = nltk.corpus.stopwords.words('russian')                       # тож приватное свойство
        tokenizer = ToktokTokenizer()                                                # тож приватное свойство
        for name_autor, message_text in zip(text[1:], from_name):
            ''' Removing control character  '''
            ''' ^ начало строки; \s flags юникодные символы '''
            name_autor = re.sub("^\s+|\n|\r|\s+$", '', name_autor.text)
            message_text = re.sub("^\s+|\n|\r|\s+$", '', message_text.text)
            ''' Removing special char  '''
            name_autor = name_autor.translate(remove_punct_dict)
            message_text = message_text.translate(remove_punct_dict)
            ''' Lower case '''
            name_autor, message_text = name_autor.lower() , message_text.lower()
            ''' Removing Stop Words only messages'''
            tokens = tokenizer.tokenize(message_text)
            tokens = [token.strip() for token in tokens]
            filtered_tokens = [token for token in tokens if token not in stopword_list]
            message_text = ' '.join(filtered_tokens)
            if len(message_text) <= header_variable.TOKEN_LENGTH:
                yield [name_autor, message_text]

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
        #skfolds = StratifiedKFold(n_splits=5, random_state=42, shuffle = True)
        kfolds = KFold(n_splits=header_variable.N_SPLITS, shuffle=True, random_state=header_variable.RANDOM_STATE)

        for num_fold, (train_index, val_index) in enumerate(kfolds.split(datafreme_message)):
            datafreme_message.loc[val_index, 'fold'] = int(num_fold)

        return datafreme_message






















































