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
        self.text

    def show(self):
        """Дія отримання інформації по статті

        Виводимо інформацію а саме заголовок текст і опис статті
        :return: Нічого
        :rtype: None
        """
        print(self.title)
        print(self.description)
        print(self.text)


