import bs4






class Message_parsing:
    def __init__(self, messages_file):
        self.messages_file = messages_file

    def parse_messages_file(self):
        print(self.messages_file)



with open('/media/anton/home2/ProteoY3/message_pool_module/messages.html', encoding='utf-8') as inf:
    '''
    https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    Beautiful Soup - это пакет Python для анализа документов HTML и XML. Он создает дерево синтаксического анализа 
    для проанализированных страниц, которое можно использовать для извлечения данных из HTML, что полезно для 
    парсинга веб-страниц.
    '''
    soup = bs4.BeautifulSoup(inf.read(), features="html.parser")
    #print(soup)



