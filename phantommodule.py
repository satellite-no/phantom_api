from phantom_api import phantom_api

key = ''

ph = phantom_api.PhanServer('SERVER URL', key)

#print(ph.build_url(endpoint='version', id=1, param1='page=1'))

#print(version = ph.get_version())

#print(ph.get_all_users())

#print(ph.get_user(24))

#print(ph.get_role(1))

#print(ph.get_container(11400))

print(ph.get_containers())

#print(ph.test_connection())
