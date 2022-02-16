import header_variable
import facade_message_parse
import sys

# в дальнейшем систему источник должен указывать клиент, мы должны переопределять эту переменую в зависимости от того что указал клиент
# поэтому указываем ее не в файле с переменными header_variable, а тут
source_system = 'telegram'
# объединяем базовый путь к файлам сообщений с папкой которая определяет сисстему источник из которой сообщения полученны
message_pool = header_variable.MESSAGE_PATH + '{}/'.format(source_system)
# папка в которую будем сохранять датасет с диалогами
collection_dialogues = header_variable.COLLECTION_DIALOGUES
# Длина сообщения
token_length = header_variable.TOKEN_LENGTH




def client_code(facade: facade_message_parse):
    return facade.operation_message_preprocessing()


if __name__ == "__main__":
    message = facade_message_parse.Message(message_pool, token_length)
    facade_message = facade_message_parse.Facade(message)
    collection = client_code(facade_message)
    print(collection)
    for j in collection:
       print(j)
        #for k in j:
            #print(k)





