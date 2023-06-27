import pandas as pd

alldata = pd.DataFrame()
name = []
adress = []
longitude = []
latitude = []
category = []
desc = []
raion = []

data = pd.read_excel("/content/Museums.xlsx")
for i in range(len(data["Наименование"])):
  name += [data["Наименование"][i]]
  adress += [data["Адрес"][i]]
  longitude += [data["longitude"][i]]
  latitude += [data["latitude"][i]]
  desc += [data["Описание"][i]]
  raion += [data["Муниципальное образование"][i]]
  category += ["Музей"]
  
data = pd.read_excel("/content/Pamyatniki.xlsx")
for i in range(len(data["Наименование"])):
  name += [data["Наименование"][i]]
  adress += [data["Адрес"][i]]
  longitude += [data["longitude"][i]]
  latitude += [data["latitude"][i]]
  desc += [data["Описание"][i]]
  raion += [data["Муниципальный район"][i]]
  category += ["Памятник"]

data = pd.read_excel("/content/Prirodnye_obekty.xlsx")
for i in range(len(data["Наименование"])):
  name += [data["Наименование"][i]]
  adress += [data["Местоположение"][i]]
  longitude += [data["longitude"][i]]
  latitude += [data["latitude"][i]]
  desc += [data["Описание"][i]]
  raion += [data["Муниципальное образование"][i]]
  category += ["Природный обьект"]
  
alldata["Наименование"] = name
alldata["Категория"] = category
alldata["Муниципальное образование"] = raion
alldata["Описание"] = desc
alldata["Местоположение"] = adress
alldata["longitude"] = longitude
alldata["latitude"] = latitude

writer = pd.ExcelWriter('Достопремичательности.xlsx')
alldata.to_excel(writer)
writer.save()
