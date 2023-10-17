def get_all_tasks(caller, org, project_space, project_name):
    '''Get all tasks in a project.'''
    path = f"asset/list/{org}/{project_space}/{project_name}?asset_type=Job&limit=1000&offset=0&sort=c_time:-1&search="
    data, response = caller.r("GET", path)
    return data['entries']