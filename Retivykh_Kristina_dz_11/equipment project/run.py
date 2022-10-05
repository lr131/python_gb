import uuid
from pprint import pprint

from branch import Branch
from copier import Copier
from scanner import Scanner
from printer import Printer
from store import Store
from exceptions import *

if __name__ == '__main__':
    
    irk = Branch("Иркутск", "Иркутская область, г. Иркутск, ул. Советсткая, 109")
    msk = Branch("Москва", "г. Москва, ул. Кожова, 19А")
    
    store = Store(temp=15, humidity=23, capacity=50)
    
    pr_samsung = Printer(serial=uuid.uuid4(), year=2020, model='tr', subtype='printer',
                         printing_type='цветной', method='лазерный', company='Kyocera',
                         os_compatibility='Windows,Ubuntu', is_duplex=True)
    pr_hp = Printer(serial=uuid.uuid4(), year=2021, model='yu', subtype='printer',
                         printing_type='монохромный', method='Матричный', company='HP',
                         os_compatibility='WindowsXP')
    pr_brozers = Printer(serial=uuid.uuid4(), year=2019, model='rtt', subtype='printer',
                         printing_type='цветной', method='Струйный', company='Brothers',
                         os_compatibility='Ubuntu,Mac,Windows10', is_duplex=True)
    
    sc_samsung = Scanner(serial=uuid.uuid4(), year=2022, model='scr', subtype='ручной',
                         output_file_formats='png,jpg', speed=50, company='Kyocera',
                         os_compatibility='Windows,Ubuntu')
    sc_hp = Scanner(serial=uuid.uuid4(), year=2020, model='htr', subtype='барабанный',
                         output_file_formats='png,bmp', speed=50, company='HP',
                         os_compatibility='Windows')
    sc_bears = Scanner(serial=uuid.uuid4(), year=2003, model='br', subtype='планшетный',
                         output_file_formats='png,bmp,jpg', speed=50, company='HP',
                         os_compatibility='Windows')
    
    cp_samsung = Copier(serial=uuid.uuid4(), year=2020, model='tr', subtype='printer',
                        company='Kyocera', copy_cost='A4', method='струйный', speed=20)
    cp_xerox = Copier(serial=uuid.uuid4(), year=2020, model='tr', subtype='printer',
                        company='Xerox', copy_cost='A4,A3', method='термопечать', speed=40)
   
    cp_brozers = Copier(serial=uuid.uuid4(), year=2020, model='tr', subtype='printer',
                        company='Brothers', copy_cost='A3', method='термопечать', speed=60)
    
    store.add(cp_brozers)
    store.add(sc_bears)
    
    print(store)
    
    # print(cp_brozers.to_dict())
    
    pprint(store.get_filling())
    
    print("Работа идёт штатно")