
def get_products_list(list_products):
    product_info = {'products': []}
    for product in list_products:
        product_info['products'].append(product.get_product_info())

    return  product_info

def get_users_list(list_users):
    user_info = {'users': []}
    for user in list_users:
        user_info['users'].append(user.get_user_info())

    return  user_info