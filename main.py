from linkedin_api import Linkedin
import json

# api = Linkedin('kazemjulien.ammar@gmail.com','KazemASI322')
# #ACoAABGenOABIM9Qn4d4TzyD0OdExJR4D2auU9M
#
# data = api.get_profile_connections('kazem-julien-ammar')
#
# json_string = json.dumps(data)
# print(json_string)


linkedin = Linkedin('kazemjulien.ammar@gmail.com', 'KazemASI322')
# profile = linkedin.get_profile('kazem-julien-ammar')

connections = linkedin.search_people(keywords='HEC Paris')


json_string = json.dumps(connections)
print(json_string)

# # Opening JSON file
# with open('ENSTA.json') as json_file:
#     data = json.load(json_file)
#
# print(data)
