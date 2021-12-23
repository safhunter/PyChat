import json
from json.decoder import JSONDecodeError
import datetime


def write_order_to_json(item: str, quantity: int = 0, price: float = 0.0, buyer: str = '',
                        date: str = str(datetime.date.today())):
    new_item = {
        'товар ': item,
        'количество': quantity,
        'цена': price,
        'покупатель': buyer,
        'дата': date,
    }

    with open('orders.json', 'r+', encoding='utf-8') as json_file:
        try:
            orders_dict = json.load(json_file)
            orders_dict['orders'].append(new_item)
        except (KeyError, TypeError, JSONDecodeError):
            orders_dict = {
                'orders': [new_item]
            }
        json_file.seek(0)
        json.dump(orders_dict, json_file, indent=4, ensure_ascii=False)


write_order_to_json('Стол', 1, 2000.0, 'anonymous')
