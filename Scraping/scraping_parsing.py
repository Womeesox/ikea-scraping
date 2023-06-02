#szklanki id: 18869
#talerzyki id: 
import ikea_api, json

constants = ikea_api.Constants(country="us", language="en")

endpoint = ikea_api.get_items(constants, ["30457903"])

item = ikea_api.run(endpoint)
item_json = json.dumps(item, indent=4)

print(item_json)

#EndpointInfo(func=functools.partial(<function PipItem.get_item at 0x000002D167842D40>, <ikea_api.endpoints.pip_item.PipItem object at 0x000002D16726C610>, '30288241'), handlers=())
#EndpointInfo(func=functools.partial(<function IowsItems.get_items at 0x000001C23807E480>, <ikea_api.endpoints.iows_items.IowsItems object at 0x000001C238918990>, '30288241'), handlers=())
