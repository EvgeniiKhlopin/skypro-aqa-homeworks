from smartphone import Smartphone

catalog = [Smartphone('Samsung', 'A60', '+79999999999'), 
           Smartphone('Apple', '14', '+71112223344'), 
           Smartphone('Honor', '50', '+78888888888'), 
           Smartphone('Samsung', 'S60', '+71113331122'), 
           Smartphone('Redme', '30', '+79995554477')]



for smartphone in catalog:
    print(f'{smartphone.brand} - {smartphone.model}. "{smartphone.number}"')