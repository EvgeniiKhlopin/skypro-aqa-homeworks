from address import Address
from mailing import Mailing

mailing = Mailing()
mailing.to_address = Address(3333, 'Москва', 'Пушкино', 20, 33)
mailing.from_address = Address(5678, 'Архангельск', 'Пр-кт Ломоносова', 112, 5)
mailing.cost = 400
mailing.track = '1250'

print(f'Отправление {mailing.track} из {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment} в {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment}. Стоимость {mailing.cost} рублей.')