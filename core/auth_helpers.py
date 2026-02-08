def is_free_user(user):
    return user.is_authenticated and user.groups.filter(name='freeUser').exists()

def is_premium_user(user):
    return user.is_authenticated and user.groups.filter(name='premiumUser').exists()

def is_admin_user(user):
    return user.is_authenticated and user.groups.filter(name='admin').exists()
