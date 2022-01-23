import header_variable
import sys

# в дальнейшем систему источник должен указывать клиент, мы должны переопределять эту переменую в зависимости от того что указал клиент
# поэтому указываем ее не в файле с переменными header_variable, а тут
source_system = 'telegram'


# объединяем базовый путь к файлам сообщений с папкой которая определяет сисстему источник из которой сообщения полученны
message_pool = header_variable.MESSAGE_PATH + '{}/'.format(source_system)
parse_module = header_variable.DATASET_MODULE_PATH
print(message_pool)
print(parse_module)
sys.path.append(parse_module)
from event_dataset import table_formatting



f = table_formatting.Table_csv_formation(message_pool)
dat = f.create_csv_file()
print(dat)
for j in dat:
    print(max(j.fold))

# добавь в файле table_formatting.py класс который будет наследоваться от table_formatting.Csv_table (Csv_table - класс),
# но в негм будет переопределена функция которая заполняет fold
# в итоге половина из message_pool будет передаваться в table_formatting.Csv_table(message_pool/2) а вторая часть
# в класс который будет наследоваться от table_formatting и в котором будет переопределена функция заполняющая кросс-вализацию fold
# возможно придется убрать конкурентеность из create_csv_file
# мы должны переопределять ту функцию которую будем вызывать

'''
test_nasl = table_formatting.Table_csv_alternative_form(message_pool)
dat2 = test_nasl.create_csv_file()
print(dat2)
for j in dat2:
    print(max(j.fold)) # 2
'''
