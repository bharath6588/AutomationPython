from sdbqatest.src.helpers.config_helpers import get_base_url


endpoint = '/my-account/'

base_url = get_base_url()
print("base_url", base_url)
#my_account_url = "http://demostore.supersqa.com" + endpoint

my_account_url = base_url + endpoint

print(my_account_url)