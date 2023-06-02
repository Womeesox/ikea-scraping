import ikea_api, json, asyncio

constants = ikea_api.Constants(country="us", language="en")

async def get_this_shit():
    item = await ikea_api.get_items(constants, ["30457903"])
    print(item)

item = asyncio.run(get_this_shit())

item_json = json.dumps(item, indent=4)

print(item)