from linkedin_api import Linkedin
import json

api = Linkedin('kazemjulien.ammar@gmail.com','KazemASI322')
#ACoAABGenOABIM9Qn4d4TzyD0OdExJR4D2auU9M
data = api.get_profile_connections("urn:li:person:")
print(data)

# # Opening JSON file
# with open('data.json') as json_file:
#     data = json.load(json_file)
#
# print(data)
