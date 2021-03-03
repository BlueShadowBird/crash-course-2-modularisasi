import requests

print('-' * 25)
try:
    response = requests.get('https://kaskus.co.id')
    if response.status_code == 200:
        print(response.text)
    else:
        print(f'get requests not succesed with status code: {response.status_code}')
except Exception as e:
    print(f'Error occured: {e}')

print('-' * 25)
print('END')