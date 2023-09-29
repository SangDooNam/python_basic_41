"""Task 1"""


# settings = {'title': 'My original title'}



# def change_site_title(string):
    
#     settings['title'] = string
    
#     return settings
    

# print(settings)
# change_site_title("A new fancy title")
# print(settings)

"""Task 2"""

# default_settings = {'title' : 'My original title'}

# def get_title(dict = default_settings):
    
#     return dict['title']


# print(get_title(settings))
# print(get_title())
# change_site_title("A new fancy title")
# print(get_title(settings))
# print(get_title())



"""Task 3"""

# settings = {'title': 'My original title', 'pages' : []}
# default_settings = {'title' : 'My original title', 'pages': []}

# def get_pages(settings = default_settings):
    
#     return settings['pages']
    


# def add_pages(page, settings = default_settings):
    
#     settings['pages'].append(page)

    


# home = {"title": "Home", "path": "/"}
# add_pages(home)
# print(get_pages())
# print(get_pages(settings))
# about = {"title": "About", "path": "/about/"}
# add_pages(about, settings)
# print(get_pages())
# print(get_pages(settings))


"""Task 4"""


# def print_user_profile(gender = 'female', 
#                        first = None, 
#                        last = 'Doe', 
#                        pictures = []):
#     if first is None:
#         if gender == 'male':
            
#             first = 'John'
#         elif gender == 'female':
            
#             first = 'Jane'
    
#     print(f'The user {first} {last} has the following pictures:\ncommon_header.png')
    
#     for i in pictures:
        
#         print(i)
    
    

# test_data1 = {
#     "gender": "male",
#     "last": "Brown",
#     "pictures": ["holidays1.png", "easter_grandma.png"]
# }
# test_data2 = {
#     "first": "Alicia",
#     "last": "Schmidt"
# }
# test_data3 = {
#     "last": "Korkov",
#     "pictures": ["sunset.png"]
# }
# print_user_profile(**test_data1)
# print_user_profile(**test_data2)
# print_user_profile(**test_data3)
# print_user_profile(**test_data2)




def print_user_profile(gender = 'female', 
                       first = None, 
                       last = 'Doe', 
                       pictures = []):
    if first is None:
        
        if gender == 'female':
            
            first = 'Jane'
            
        elif gender == 'male':
            
            first = 'John'
    
    print(f'The user {first} {last} has the following pictures:')
    
    
    if len(pictures) != 0:
        
        if pictures[0] != 'common_header.png':
            
            pictures.insert(0, 'common_header.png')
    else:
        pictures.insert(0, 'common_header.png') 

    
    for i in pictures:
        
        print(i)
    
    

test_data1 = {
    "gender": "male",
    "last": "Brown",
    "pictures": ["holidays1.png", "easter_grandma.png"]
}
test_data2 = {
    "first": "Alicia",
    "last": "Schmidt"
}
test_data3 = {
    "last": "Korkov",
    "pictures": ["sunset.png"]
}
print_user_profile(**test_data1)
print_user_profile(**test_data2)
print_user_profile(**test_data3)
print_user_profile(**test_data2)
