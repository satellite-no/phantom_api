import requests
import json

class PhanServer:
    """Phantom Server Object"""
    def __init__(self, server, key):
        self.base_url = server
        self.params = {'Accept':'application/json','ph-auth-token':key}

    def build_url(self, **kwargs):
        """ Builds the URL for the Phantom Servers REST API.
        Arguments = endpoint, id, param1, param2, etc... """
        # Build base URL for API query
        url_path = '/rest/' + kwargs['endpoint']
        if 'id' in kwargs:
            url_path = url_path + '/' + str(kwargs['id'])

        if 'param1' in kwargs:
            for i in kwargs:
                if 'param' in i:
                    url_path = url_path + '?' + kwargs[i]

        url = self.base_url + url_path

        return url

    def test_connection(self):
        """ Tests connectivity to the Phantom Server."""
        # Build base URL for API query
        url = self.build_url(endpoint='version')

        r = requests.get(url=url, headers=self.params, verify=False)

        if r.status_code == 200:
            return "Success"
        else:
            message = json.loads(r.text)
            error = "ERROR: " + str(r.status_code) + " " + r.reason + ", " + message['message']
            return error
    
    def get_version(self):
        """ Returns the version of the Phantom Server."""

        # Build base URL for API query
        url = self.build_url(endpoint='version')

        r = requests.get(url=url, headers=self.params, verify=False)

        version = r.json()
        return version['version']

    # Call to get all Phantom users and return
    def get_all_users(self):
        """Method to get all users from Phantom."""
        # Build base URL for API query
        url = self.build_url(endpoint='ph_user')

        # Make the request 
        r = requests.get(url=url, headers=self.params, verify=False)
        data = r.json()

        return data

    # Gets a specific user
    def get_user(self, id=None):
        """Method to get specfic user from Phantom."""
        if id == None:
            return "Missing Paramater"

        # Build base URL for API query
        url = self.build_url(endpoint='ph_user',id=id)
       
        # Make the request 
        r = requests.get(url=url, headers=self.params, verify=False)
        data = PhanUser(r.json())

        return data

    def get_role(self, id=None):
        """Method to get all roles from Phantom."""
        if id == None:
            return "Missing Paramater"

        # Build base URL for API query
        url = self.build_url(endpoint='role',id=id)

        # Make the request 
        r = requests.get(url=url, headers=self.params, verify=False)
        data = r.json()

        return data

    def get_container(self, id=None):
        """Method to get a single container from Phantom."""
        if id == None:
            return "Missing Parameter"

        # Build base URL for API query
        url = self.build_url(endpoint='container',id=id)
       
        # Make the request 
        r = requests.get(url=url, headers=self.params, verify=False)
        if r.status_code != 200:
            print("Error: {0} Returned {1}".format(r.status_code, r.reason))
        else:
            data = PhanContainer(r.json())
            return data

        return

    def get_containers(self, page=1, page_size=10, filter_field=None, sort='id', order='desc'):
        """Method to get multiple containers back from Phantom.
        Defaults = page=1, page_size=10, filter_field=None, sort='id', order='desc'"""
        
        # Build base URL for API query
        ## Cleaner way of doing this? maybe pass in dict to *arg?
        url = self.build_url(endpoint='container',param1='page='+str(page),param2='page_size='+str(page_size),param3='sort='+sort,param4='order='+order)
        
        # Makes the REST request to Phantom.
        r = requests.get(url=url, headers=self.params, verify=False)

        #checks for errors in the returned value.
        if r.status_code != 200:
            print("Error: {0} Returned {1}".format(r.status_code, r.reason))
        else:
            count = r.json()['count']
            page_count = r.json()['num_pages']
            data = []
            for i in r.json()['data']:
                i['data'] = None
                data.append(PhanContainer(i))
            return [count, page, page_count, data]

        return

# Phantom User object
class PhanUser:
    """Phantom user class"""
    
    def __init__(self, user):
        self.json = user
        self.last_name = user['last_name']
        self.is_staff = user['is_staff']
        self.external_update_needed = user['external_update_needed']
        self.default_label = user['default_label']
        self.id = user['id']
        self.date_joined = user['date_joined']
        self.first_name = user['first_name']
        self.title = user['title']
        self.default_tenant = user['default_tenant']
        self.is_superuser = user['is_superuser']
        self.last_login = user['last_login']
        self.location = user['location']
        self.type = user['type']
        self.email = user['email']
        self.username = user['username']
        self.prevent_login = user['prevent_login']
        self.is_active = user['is_active']
        self.onboarding_state = user['onboarding_state']
        self.externally_managed = user['externally_managed']
        self.roles = user['roles']
        self.time_zone = user['time_zone']
        self.show_onboarding = user['show_onboarding']

# Phantom Container Class Object
class PhanContainer:
    """Phantom Container Class"""
    
    def __init__(self, container):
        self.artifact_count = container['artifact_count']
        self.id = container['id']
        self.close_time = container['close_time']
        self.custom_fields = container['custom_fields']
        self.data = container['data']
        self.description = container['description']
        self.due_time = container['due_time']
        self.end_time = container['end_time']
        self.ingest_app = container['ingest_app']
        self.kill_chain = container['kill_chain']
        self.label = container['label']
        self.name = container['name']
        self.owner_name = container['owner_name']
        self.role = container['role']
        self.sensitivity = container['sensitivity']
        self.severity = container['severity']
        self.source_data_identifier = container['source_data_identifier']
        self.start_time = container['start_time']
        self.open_time = container['open_time']
        self.status = container['status']
        self.tags = container['tags']
        self.container_type = container['container_type']
        self.current_phase = container['current_phase']
        self.status = container['status']
