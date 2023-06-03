#szklanki id: 18869
#talerzyki id: 
import ikea_api, json, asyncio

constants = ikea_api.Constants(country="ru", language="pl")

items = asyncio.run(ikea_api.get_items(constants, ["30288241"]))
#item_json = json.dumps(item, indent=4)

print(item)

#EndpointInfo(func=functools.partial(<function PipItem.get_item at 0x000002D167842D40>, <ikea_api.endpoints.pip_item.PipItem object at 0x000002D16726C610>, '30288241'), handlers=())
#EndpointInfo(func=functools.partial(<function IowsItems.get_items at 0x000001C23807E480>, <ikea_api.endpoints.iows_items.IowsItems object at 0x000001C238918990>, '30288241'), handlers=())
