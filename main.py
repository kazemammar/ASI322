from linkedin_api import Linkedin
import json
from itertools import islice

linkedin = Linkedin('kazem.ammar@ensta-paris.fr', 'KazemASI322')
# # profile = linkedin.get_profile('kazem-julien-ammar')
#
# connections = linkedin.search_people(keywords='HEC Paris', network_depth='O')
#
# json_string = json.dumps(connections)
# print(json_string)

# Opening JSON file
with open('ENSTA.json') as json_file:
    data = json.load(json_file)

publicIds = []

for elt in data:
    publicIds.append(elt["public_id"])

publicIdsDict = dict.fromkeys(publicIds)
i=0

print(publicIdsDict)

i = 0
for key in islice(publicIdsDict, 3):
    profile = linkedin.get_profile(key)
    publicIdsDict[key]=profile["experience"][0]['companyName']
    i+=1
    print(i)

print(publicIdsDict)