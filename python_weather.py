# Importação de bibliotecas
import requests, json
# Variáveis
api_key = "3d57b8d8656846b828a661fde61cbe9b"
lang = "pt_BR"
# Campo que pergunta o nome da cidade
while True:
    cidade = str(input("Digite o nome de uma cidade do planeta terra: "))
    if (len(cidade.strip()) <= 0):
        print("O nome da cidade não pode ficar vazia.")
    else:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang={lang}"
        clima = requests.get(url).json()
        break  
# Se for diferente do ERRO 404    
if clima["cod"] != "404":
    # Parâmetros
    clm = clima["main"]
    local = clima["sys"]
    coordenada = clima["coord"] 
    geografia1 = clima["id"]
    geografia2 = clima["name"]
    #
    ID = geografia1
    city = geografia2
    pais = local["country"]
    temperatura = clm["temp"]
    temp_minima = clm["temp_min"]
    temp_maxima = clm["temp_max"]
    umidade = clm["humidity"]
    longitude = coordenada["lon"]
    latitude = coordenada["lat"]
    # Cálculos
    calculo_temperatura = temperatura / 10
    calculo_temp_min = temp_minima / 10
    calculo_temp_max = temp_maxima / 10
    # Impressão
    print("-----------------------------------------------")
    print(f"ID: {ID} | Cidade: {city} | País: {pais}")
    print(f"Longitude: {longitude} | Latitude: {latitude}")
    print(f"Temperatura atual: {round(calculo_temperatura,2)}°C")
    print(f"Temparatura mínima: {round(calculo_temp_min,2)}°C")
    print(f"Temparatura máxima: {round(calculo_temp_max,2)}°C")
    print(f"Umidade atmosférica: {umidade}%")
else:
    print(f"A cidade {cidade} não foi encontrada.")