# OpenWeatherMap API Key
#api_key = "acebe012aa09a42fa41503aa5a8e7558"
file_path = 'api_key.txt'
with open(file_path) as api_file:
    api_key = api_file.read().strip('\n')
