import json

# Explorando a estrutura dos dados
file_name = '/home/LucasSoares/Área de trabalho/Python projects/Downloading Data/earthquake/earthquakes.json'

with open(file_name) as f:
    all_eq_data = json.load(f)

readable_file = '/home/LucasSoares/Área de trabalho/Python projects/Downloading ' \
                'Data/earthquake/readable_data_earthquakes.json '

# Criando um arquivo que pode ser lido mais facilmente
# with open(readable_file, 'w') as f:
#    json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']

mags = []
lons = []
lats = []
hover_texts = []

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']

    mags.append(int(mag))
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

print(mags)
print(lats)
print(lons)
print(hover_texts)

