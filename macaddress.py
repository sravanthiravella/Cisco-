from maclookup import ApiClient
import logging

client = ApiClient('https://api.macaddress.io/v1?apiKey=at_H86mdXhKntbqN9IbW7trDkoxbi9gS&output=json&search=44:38:39:ff:ef:57')

logging.basicConfig(filename='myapp.log', level=logging.WARNING)

print(client.get_raw_data('44:38:39:ff:ef:57', 'json'))
print(client.get_vendor('44:38:39:ff:ef:57'))
print(client.get('44:38:39:ff:ef:57'))

response = client.get('44:38:39:ff:ef:57')
print(response.vendor_details.is_private)
print(response.block_details.date_created)
