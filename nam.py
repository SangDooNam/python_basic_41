"""Task 1"""


settings = {'title': 'My original title'}



def change_site_title(string):
    
    settings['title'] = string
    
    return settings
    

# print(settings)
# change_site_title("A new fancy title")
# print(settings)

"""Task 2"""

default_settings = {'title' : 'My original title'}

def get_title(dict = default_settings):
    
    return dict['title']


print(get_title(settings))
print(get_title())
change_site_title("A new fancy title")
print(get_title(settings))
print(get_title())