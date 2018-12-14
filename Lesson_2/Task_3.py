import yaml


item_list = ['yaml', 'json', 'scv']
item_num = 42
item_dict = {'€': 1, '҈': 'Hello', 'ξ': 'E'}

dict_to_yaml = {'list': item_list, 'num': item_num, 'dict': item_dict}

with open('file.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(dict_to_yaml, f, allow_unicode=True, default_flow_style=False)
