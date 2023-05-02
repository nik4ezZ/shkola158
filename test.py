import json

with open('news_dict.json') as file:
    news_dict = json.load(file)

seatch_id = 'd0bfd0bed0b4d02bdd18fd182d0b8d18f'

if seatch_id in news_dict:
    print('Новость уже есть')
else:
    print('ERROR')