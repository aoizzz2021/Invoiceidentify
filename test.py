
import requests

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=QmbktcExEG16jBxHxCUi1ktL&client_secret=YBtmnuRyM1dlCP5srIHnUD2b7QUfVLF7'
response = requests.get(host)
if response:
    print(response.json()['access_token'])