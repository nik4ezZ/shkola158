import requests
from bs4 import BeautifulSoup

print('Здравствуйте! Бот создан для успешного поиска участников стима с маленьким lvl-ом! Создатель - telegram - '
      '@nik4ez')
def get_accs():
    id_group = input('Введите ID группы: ')
    page_cnt = int(input('Введите число страниц, которое хотите отсортировать: '))
    page_cnt = page_cnt + 1
    headers = {
        'User-Agent': 'GG_WP'
    }
    page = 1
    acc_id = []
    while page != page_cnt:
        url = f'https://steamcommunity.com/groups/{id_group}/members/?p={page}'
        r = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        member_group_info = soup.find_all('div', class_='member_block_content')
        for link in member_group_info:
            link_user = link.find("a", class_="linkFriend").get("href")
            acc_id.append([link_user.split('/')[3],link_user.split('/')[4]])
        page += 1
    print(f'Завершен сбор id участников.\nВсего нашлось {len(acc_id)} id.\nНачинаем подбор по вашим параметрам!')
    acc_info = []
    c = 0
    for id in range(len(acc_id) - 1):
        #print(id,acc_id[id][0],acc_id[id][1])
        url = f'https://steamcommunity.com/{acc_id[id][0]}/{acc_id[id][1]}/inventory/#730'
        r = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        count_itm = soup.find_all('span', class_='games_list_tab_number')
        game_pars = soup.find_all('span', class_='games_list_tab_name')
        for game in game_pars:
            for item in count_itm:
                item_cnt = item.text
                print(item_cnt, game.text,f'https://steamcommunity.com/{acc_id[id][0]}/{acc_id[id][1]}/\n')
                #print(f'(ID: {acc_id[id][1]})\n'
                      #f'{game.text} сколько предметов: {item_cnt}\n'
                         # f'Ссылка: https://steamcommunity.com/{acc_id[id][0]}/{acc_id[id][1]}/\n'
                          #f'Уровень: {item_cnt}\n')
    print('Спасибо за использование, удачи! Промокод: NIK4EZ2023')
    input()




def main():
    get_accs()

if __name__ == '__main__':
    main()