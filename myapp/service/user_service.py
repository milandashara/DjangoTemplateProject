from myapp.buisness import user as user_bll
    
def get_users(page):
    return user_bll.get_users(page);

def create_user(request_user_model, username,email,password,groupname):
    return user_bll.create_user(request_user_model,username, email, password, groupname);

def edit_user(request_user_model,username,email,password,role):
    return user_bll.edit_user(request_user_model, username, email, password, role)

def find_by_username(username):
    return user_bll.find_by_username(username)

def delete_user(request_user_model,username):
    return user_bll.delete_user(request_user_model, username)