goods = []
features = {'Название': '', 'Цена': '', 'Количество': '', 'Единица измерения': ''}
analytics = {'Название': [], 'Цена': [], 'Количество': [], 'Единица измерения': []}
num = 0
feature_ = None
control = None
while True:
    control = input("Для выхода нажмите '1', Для продолжения нажмите 'Enter', ДЛя анализа нажмите '0' : ").upper()
    if control == '1':
        break
    num += 1
    if control == '0':
        print(f'\n Current analytics \n {"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    for f in features.keys():
        feature_ = input(f'Введите "{f}"')
        features[f] = int(feature_) if (f == 'Введите цену товара:' or f == 'Введите количество товара:') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))
while True:
    control = input("Для выхода нажмите '1', Для продолжения нажмите 'Enter', ДЛя анализа нажмите '0' : ").upper()
    if control == '1':
        break
