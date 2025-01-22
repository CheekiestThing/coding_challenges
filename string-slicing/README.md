Python Challenge

Your challenge is write a program to ask the user to enter their school username in the following format:

    Year Group Using two digits (e.g. “07” for year 7, “11” for year 11, “00” for staff members)
    1 character for their initial (first letter of their firstname)
    The user’s lastname
    A 2-digit code: “_S” for students, “_T” for teachers, “_A” for admin staff.

For instance the following usernames are valid usernames:

    07jFox_S
    09kJohnson_S
    11rTaylor_S
    00pJones_T
    00jOliver_A

Your program should read the username and decide:
* If the username is less than 6 characters long the program should ask the user to enter a valid username.
* If the username does not contain the character “_” it should also ask the user to enter a valid username.
* If the username is valid, the program should decide if the user is a member of staff or a student.
* If they are a student the programme should find out their year group.
* The program should also display the initial of the student as well as their lastname.
* Finally the program should display whether the user is a Student, a Teacher or an Admin member of staff. 