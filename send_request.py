import requests

HOST = 'http://127.0.0.1:5000/'
API_KEY = '12345'
API_KEY_FIELD = 'X-API-KEY'
REMOTE_ENDPOINT = "https://stageglass-central-x3c53cgmra-uw.a.run.app"
PORT = "443"

GATEWAY_ENDPOINT = "https://central-4n8pnixh.wl.gateway.dev"

def with_api_key(headers):
  headers[API_KEY_FIELD] = API_KEY
  print('with_api_key')
  print(headers)
  return headers

def print_response(data):
  print(data.status_code)
  print(data.text)

def send_request(url):
  return requests.get(
    url
  )

def post_request(url, json_data):
  print(url, json_data)
  return requests.post(
    url,
    json = json_data
  )

#response = post_request(REMOTE_ENDPOINT + '/Central/GetLinkCodeRecord:' + PORT, {'link_code':'iifiG7WNFE'})
#response = send_request(REMOTE_ENDPOINT + '/Central/GetLinkCodeRecord:' + PORT, {'link_code':'iifiG7WNFE'})

#response = send_request(GATEWAY_ENDPOINT + '/Central/GetLinkCodeRecord?link_code=iifiG7WNFE')
response = send_request(GATEWAY_ENDPOINT + '/v1/linkcode/iifiG7WNFE/')
print_response(response)
