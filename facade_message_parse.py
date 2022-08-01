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
from accessify import protected
nltk.download('stopwords')

class Facade:
    def __init__(self, subsystem_message) -> None:
        self.subsystem_message = subsystem_message or Message()

    def operation_message_preprocessing(self):
        collection_dialogues = self.subsystem_message.create_csv_file()
        return collection_dialogues


class Message:
    def __init__(self, message_pool, token_length):
        self.message_pool = message_pool
        self.token_length = token_length

    def create_csv_file(self):
        __listd_message = os.listdir(self.message_pool)
        for message in __listd_message:
            print("---------------------------------------------------------------------------------->", message)
            messages_file = self.message_pool + message
            parse = self.parse_messages_telefram_file(messages_file)
            datafreme_message = self.create_datafreme(parse)
            datafreme_message = self.strat_Fold(datafreme_message)
            yield (datafreme_message, message)

    @protected
    def parse_messages_telefram_file(self, messages_file):
        with open(messages_file, encoding='utf-8') as inf:

            soup = bs4.BeautifulSoup(inf.read(), features="html.parser")
            text = soup.find_all('div', class_='text')
            from_name = soup.find_all('div', class_='from_name')

            filtering = self.message_filtering_by_source(text, from_name)

            for name_autor, message_text in filtering:
                yield [name_autor, message_text]

    @protected
    def message_filtering_by_source(self, text, from_name):
        remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
        stopword_list = nltk.corpus.stopwords.words('russian')
        tokenizer = ToktokTokenizer()
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

    @protected
    def create_datafreme(self, parse):
        dataset_message = pd.DataFrame()
        for i, step_dataset in enumerate(parse):
            dataset_message.loc[i, 'from_name'] = step_dataset[1]
            dataset_message.loc[i, 'text'] = step_dataset[0]
        return dataset_message

    @protected
    def strat_Fold(self, datafreme_message):
        kfolds = KFold(n_splits=header_variable.N_SPLITS, shuffle=True, random_state=header_variable.RANDOM_STATE)

        for num_fold, (train_index, val_index) in enumerate(kfolds.split(datafreme_message)):
            datafreme_message.loc[val_index, 'fold'] = int(num_fold)

        return datafreme_message






















































