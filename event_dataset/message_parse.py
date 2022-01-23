import bs4



class Message_parsing:
    def __init__(self, messages_file):
        self.messages_file = messages_file        # Полный путь к файлу

    def parse_messages_telefram_file(self):
        with open(self.messages_file, encoding='utf-8') as inf:
            '''
            https://www.crummy.com/software/BeautifulSoup/bs4/doc/
            Beautiful Soup - это пакет Python для анализа документов HTML и XML. Он создает дерево синтаксического анализа 
            для проанализированных страниц, которое можно использовать для извлечения данных из HTML, что полезно для 
            парсинга веб-страниц.
            '''
            soup = bs4.BeautifulSoup(inf.read(), features="html.parser")
            text = soup.find_all('div', class_='text')
            from_name = soup.find_all('div', class_='from_name')
            for name_autor, message_text in zip(text, from_name):
                yield [name_autor.text, message_text.text]







