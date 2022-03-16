# Importação de bibliotecas
import requests, json, webbrowser
# Variáveis
api_key = "3d57b8d8656846b828a661fde61cbe9b"
lang = "pt_BR"
# Campo que pergunta o nome da cidade
while True:
    cidade = str(input("Digite o nome de uma cidade: "))
    if (len(cidade.strip()) <= 0):
        print("O nome da cidade não pode ficar vazia.")
    else:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang={lang}"
        clima = requests.get(url).json()
        break  
# Se for diferente do ERRO 404    
if clima["cod"] != "404":
    # Parâmetro
    geografia = clima["id"]
    # Variável para armazenar o parâmetro
    id_city = geografia
    # Mensagem
    print("Aguardando resultado...")
    # Abre as informações climáticas via navegador
    webbrowser.open(f"https://openweathermap.org/city/{id_city}")
else:
    print(f"A cidade {cidade} não foi encontrada.")