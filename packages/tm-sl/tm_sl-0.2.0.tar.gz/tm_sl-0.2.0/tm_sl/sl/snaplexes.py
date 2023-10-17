
def get_all_splex_data(caller, org):
    path = f"plex/org/{org}"
    data, response = caller.r("GET", path)
    return data

def list_all_splex_in_project(caller, project_path):
    '''
    path: org/space/project
    '''
    path = f"asset/list/{project_path}?asset_type=Plex&limit=100&offset=0&sort=c_time%3A-1&search="
    data, response = caller.r("GET", path)
    return data['entries']

def get_splex_binary(caller, sl_path, save_path=None): ## maybe refactor to just get binary data
    assert save_path != None or save_path.endswith(".slpropz"), "save_path must not be None or end with .slpropz"
    '''
    path: "tidemark-dev/shared/dev1" references a snaplex directly
    '''
    path = f"plex/links/{sl_path}"
    data, response = caller.r("GET", path)
    snap_config_url = data['config']
    caller.download_binary(snap_config_url, save_path)
