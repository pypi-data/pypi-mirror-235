

def get_all_users(caller, org):
    path = f"asset/user/settings?path=%2F{org}"
    data, response = caller.r("GET", path)
    users = data['users']
    return users

def get_user(caller, email, org=None):
    if org != None:
        users = get_all_users(caller, org)
        for user in users:
            if user['username'] == email:
                return user
        raise Exception(f"User {email} not found in org {org}")
    path = f"asset/user/{email}"
    data, response = caller.r("GET", path)
    return data

def create_user(caller, org, email):
    path = f"asset/user/{email}/org/{org}"
    data, response = caller.r("PUT", path)

def delete_user(caller, org, email):
    path = f"asset/user/{email}/org/{org}"
    data, response = caller.r("DELETE", path)