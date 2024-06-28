import requests


def fetch_data(option, count):
  url = f"https://swapi.dev/api/{option}/"
  result = []
  while len(result) < count:
    try:
      response = requests.get(url)
      response.raise_for_status()
      data = response.json()
      result.extend(data["results"])
      #print(len(result))
      url = data["next"]

    except requests.HTTPError as e:
      print(f"Error fethcing data: {e}")
      return None
  
    if url is None:
      break
  return result[:count]

count = int(input("Enter the number of entities to download: "))

result = fetch_data("people", count)

if len(result) > 0:
  for entity in result:
    print(entity["name"])
else:
  print("Unable to download data")