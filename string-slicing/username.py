import time

username_valid = False

print('''*Create new User*
      
Username requirements:
    1. Begin with your Year group (e.g. “07” for year 7, “11” for year 11, “00” for staff members)
    2. The first letter of your first name
    3. Your full last name
    4. A 2-digit code: “_S” for students, “_T” for teachers, “_A” for admin staff.
''')

while not username_valid:
    _input = input("New Username: \n>>>")

    if (len(_input) < 6):
        print("Invalid Username: The Username must be at least 6 characters long.")
        time.sleep(1)
        continue

    if not "_" in _input:
        print("Invalid Usernames: The Username must contain an underscore. (_)")
        time.sleep(1)
        continue

    username_valid = True

if username_valid:
    _code_location = _input.find("_")
    _year = "Staff"
    if int(_input[0:2]) > 0:
        _year = str(int(_input[0:2])) + "th Year"
    
    _name = _input[2].upper() + ". " + _input[3:_code_location]
    _user_type = _input[_code_location:_code_location+2].replace("_S", "Student").replace("_T", "Teacher").replace("_A", "Admin")

    print(f'''\nAbout "{_input}":
    Name: {_name}
    {_user_type}, {_year}\n''')