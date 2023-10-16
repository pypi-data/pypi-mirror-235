class Article:
    """Клас для опису статті

    :param title: Заголовок статті
    :type title: str
    :param description: Опис статті
    :type description: str
    :param text: Текст статті
    :type text: str    
    """
    def __init__(self,
                 title,
                 description,
                 text):
        self.title=title
        self.description=description
        self.text = text
        
    def show(self):
        """Дія отримання інформації по статті

        :return: Нічого
        :rtype: None

        """
        print(self.title)
        print(self.description)
        print(self.text)


class SiteArticle(Article):
    """Клас для опису статті Для Сайту

    :param title: Заголовок статті
    :type title: str
    :param description: Опис статті
    :type description: str
    :param text: Текст статті
    :type text: str    
    """
    def __init__(self,
                 title,
                 description,
                 text,
                 site):
        super().__init__(title,description,text)
        self.site=site



class PapperArticle(Article):
    def __init__(self,
                 title,
                 description,
                 text,
                 site):
        super().__init__(title,description,text)
        self.papper=papper


class NewsArticle(Article):
    def __init__(self,
                 title,
                 description,
                 text,
                 news):
        super().__init__(title,description,text)
        self.news=news



#print(type(SiteArticle(1,2,3,4).__doc__))
