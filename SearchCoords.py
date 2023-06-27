import pandas as pd
import requests
import json

def get_coords(text):##Функция делает запрос в поиске по организациям
  request = requests.get("https://search-maps.yandex.ru/v1/?text="\
                         +text+"&lang=ru_RU&results=100&\
                        apikey=YOUR_API_KEY")
  place = json.loads(request.content)
  return place

##Функция передает координаты места по названию и адресу
##data - датасет с информацией о местах
##name - название столбца с названиями
##adress - название стоблца с адресом
##i - номер строки в датасете

def searchPlace(data, i, name, adress):
  place = get_coords(data[name][i] + " " + data[adress][i])
  features = place['features']
  for j in features:
    if "description" in j['properties']:
      if "Иркутская область" in j['properties']['description']:##Находится ли место в Иркутской области
        return j['geometry']['coordinates']
    
  place = get_coords(data[adress][i])
  features = place['features']
  return features[0]['geometry']['coordinates'] + ["*"]

data = pd.read_excel("Path_to_.xlsx")
coords = []
for i in range(len(data["Наименование"])):
  coords += [searchPlace(data, i,"Наименование","Местоположение")]
  
data["coords"] = coords
writer = pd.ExcelWriter('coords.xlsx')
data.to_excel(writer)
writer.save()


