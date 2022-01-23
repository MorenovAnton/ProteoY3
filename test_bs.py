import bs4

path = "../ProteoY3/message_pool/telegram/messages.html"

with open(path, encoding='utf-8') as inf:
    '''
    https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    Beautiful Soup - это пакет Python для анализа документов HTML и XML. Он создает дерево синтаксического анализа 
    для проанализированных страниц, которое можно использовать для извлечения данных из HTML, что полезно для 
    парсинга веб-страниц.
    '''
    soup = bs4.BeautifulSoup(inf.read(), features="html.parser")
    #print(soup.prettify())
    so = soup.find_all('div', class_='text')
    s2 = soup.find_all('div', class_='from_name')
    for s2, s in zip(so, s2):
        print(s2.text, s.text)
