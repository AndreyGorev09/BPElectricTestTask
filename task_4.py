""" Дан json файл. Найдите в нём все поля "updated" и 
поменяйте значение на текущие дату и время в формате ISO 8601. """
import json
import datetime
    

with open('Desktop/test.json') as f:
    templ = json.load(f)
    templ['updated'] = f'{datetime.datetime.now()}'
    f.close()

with open('Desktop/test.json', 'w') as f:
    json.dump(templ, f)
    f.close()
    
    
   






    

