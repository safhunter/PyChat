import yaml

data_to_yaml = {
    'list': [1, 2, 3],
    '2': 2,
    'dict': {
        'key_1': '123₽',
        'key_2': '23€',
    }
}

with open('file.yaml', 'w', encoding='utf-8') as f_n:
    yaml.dump(data_to_yaml, f_n, default_flow_style=True, allow_unicode=True)

with open('file.yaml', encoding='utf-8') as f_n:
    print(f_n.read())

