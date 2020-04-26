from selenium.webdriver import Chrome, Firefox
from page_object.video_page import YouTubePageVideo
from bs4 import BeautifulSoup
import time
import csv


def browser():
    driver = Chrome(executable_path='/home/hitruk/dir/chromedriver')
    # driver = Firefox(executable_path='/home/hitruk/dir/geckodriver')
    driver.implicitly_wait(10)
    return driver


def parser_page(driver):
    youtube_page = YouTubePageVideo(driver)
    youtube_page.load_page()
    time.sleep(5)
    youtube_page.scroll_page_down()
    youtube_page.select_comments()
    youtube_page.new_comments()
    youtube_page.scroll_comments_down()
    youtube_page.quantity_username_page()


    max_users = 60  # максимальное количество пользователей/комментариев
    x = 20  # сохранить данные, когда кол-во записей на странице достигнет x
    y = 20  # пересохранять данные через каждые y вновь появившихся записей
    save_list = []  # количество сохранений/сохранений
    data_parser = []  # список users, links, comments

    while (max_users > youtube_page.quantity_username_page()):
        youtube_page.scroll_comments_down()
        youtube_page.quantity_username_page()  #количество вновь подгруженных комментариев

        if youtube_page.quantity_username_page() == x:
            save_list.append(x)
            x = x+y  # следующая запись
            print('===')  # отладка
            print('Кол-во записей ', save_list[-1])  # отладка

            soup = BeautifulSoup(driver.page_source, 'html.parser')
            content = soup.find('div', id='contents').find_all('div', id='main')

            for row in content:
                # user пользователи оставившие комментарии
                user = row.find('div', id='header').find('a', id='author-text').find('span').text.strip()
                # link_user ссылки на страницы пользователей
                link_user = row.find('div', id='header').find('a', id='author-text').get('href')
                # comments комментарии пользователей
                comments = row.find('div', id='content').text.strip()

                if [user, link_user, comments] not in data_parser:
                    data_parser.append([user, link_user, comments])

                with open('some.csv', 'w', newline='') as f:
                    writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)
                    writer.writerows(data_parser)
    driver.close()

    print(len(data_parser))
    print(data_parser)


def main():
    parser_page(browser())

if __name__ == "__main__":
    main()
