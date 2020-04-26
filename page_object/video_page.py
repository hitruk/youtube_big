from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class YouTubePageVideo:

    URL = 'https://www.youtube.com/watch?v=sRwXMnLgcK4'
    PAGE_DOWN = (By.TAG_NAME, 'body')  # прокрутить страницу до меню
    SELECT_COMMENTS = (By.ID, 'icon-label')  # меню комментариев
    NEW_COMMENTS = (By.LINK_TEXT, 'Сначала новые')  # выбрать новые комментарии
    POPULAR_COMMENTS = (By.LINK_TEXT, 'Сначала популярные')  # выбрать популярные комментарии
    SCROLL_COMMENTS_DOWN = (By.TAG_NAME, 'body')  # прокрутить комментарии вниз страницы
    QUANTITY_USERNAME_PAGE = (By.CSS_SELECTOR, '#author-text')  # количество пользователей/комментариев на странице


    def __init__(self, driver):
        self.driver = driver

    def load_page(self):
        self.driver.get(self.URL)

    def scroll_page_down(self):
        page_down_scroll = self.driver.find_element(*self.PAGE_DOWN)
        page_down_scroll.send_keys(Keys.PAGE_DOWN)

    def select_comments(self):
        comments_select = self.driver.find_element(*self.SELECT_COMMENTS)
        comments_select.click()

    def new_comments(self):
        comments_new = self.driver.find_element(*self.NEW_COMMENTS)
        comments_new.click()

    def popular_comments(self):
        comments_popular = self.driver.find_element(*self.POPULAR_COMMENTS)
        comments_popular.click()

    def scroll_comments_down(self):
        scroll_comments = self.driver.find_element(*self.SCROLL_COMMENTS_DOWN)
        scroll_comments.send_keys(Keys.PAGE_DOWN)

    def quantity_username_page(self):
        comments_username = self.driver.find_elements(*self.QUANTITY_USERNAME_PAGE)
        return len(comments_username)