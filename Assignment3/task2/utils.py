import networkx as nx
import requests

def get_list_of_friends(user :str):
    """Get list of friends of given user from livejournal website"""
    r = requests.get('https://www.livejournal.com/misc/fdata.bml', params = {'user':user})
    data = r.text.splitlines()
    data = data[1:]
    data = ' '.join(data)
    data = data.split()
    data = set(filter(lambda a: a != '>' and a != '<', data))

    return list(data)