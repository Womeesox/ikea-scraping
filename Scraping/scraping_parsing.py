import ikea_api, json, asyncio

constants = ikea_api.Constants(country="pl", language="pl")

ingka_items = ikea_api.IngkaItems(constants)
endpoint = ingka_items.get_items(["30457903"])

ikea_api.run_async(endpoint)
# item_json = json.dumps(item, indent=4)

# print(item)