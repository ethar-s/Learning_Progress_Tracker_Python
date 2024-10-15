import re


student_instance = "n/a"



class Student:
    all_students = {}
    def __init__(self, firstname='', lastname='', email=''):
        self.flask_completed = []
        self.databases_completed = []
        self.dsa_completed = []
        self.python_completed = []
        self.flask_score_total = 0
        self.flask_score = 0
        self.completed={}
        self.student_notify={}
        self.database_score_total = 0
        self.database_score = 0
        self.dsa_score_total = 0
        self.dsa_score = 0
        self.python_score = 0
        self.python_score_total = 0
        self.students_point = {}
        self.popular = {}
        self.activity = {}
        self.most_popluer = 'n/a'
        self.least_popular = "n/a"

        self.highest_activity = 'n/a'
        self.lowest_activity = 'n/a'

        self.easiest_course = 'n/a'
        self.hardest_course = 'n/a'

        self.python_populatry = 0
        self.dsa_populatry = 0
        self.database_populatry = 0
        self.flask_populatry = 0
        self.python_activity = 0
        self.dsa_activity = 0
        self.database_activity = 0
        self.flask_activity = 0
        check_students = self.check_existing(email)
        # Updated name validation to allow spaces, apostrophes, and hyphens in both names
        if (re.fullmatch(r"^[a-zA-Z]+([-'][a-zA-Z]+)*$", firstname) and len(firstname) > 1  # First name validation
                and re.fullmatch(r"^[a-zA-Z ]+([-'][a-zA-Z ]+)*$", lastname) and len(
                    lastname) > 1  # Last name validation
                and re.fullmatch(r"^[\w\.-]+@[a-zA-Z\d-]+\.[a-zA-Z\d]+$", email)  # Email validation
                and not check_students):

            self.firstname = firstname
            self.lastname = lastname
            self.email = email
            self.id = len(self.all_students) + 1
            self.all_students[self.id] = {'first name': self.firstname, 'last name': self.lastname, 'email': self.email}
            print("The student has been added.")
            global students_added
            students_added += 1
        else:
            if not re.fullmatch(r"^[a-zA-Z]+([-'][a-zA-Z]+)*$", firstname) or len(firstname) < 2:
                print('Incorrect first name')
            elif not re.fullmatch(r"^[a-zA-Z ]+([-'][a-zA-Z ]+)*$", lastname) or len(lastname) < 2:
                print('Incorrect last name')
            elif not re.fullmatch(r"^[\w\.-]+@[a-zA-Z\d-]+\.[a-zA-Z\d]+$", email):
                print('Incorrect email')
            elif check_students:
                print('This email is already taken.')
            else:
                print("Incorrect credentials.")

    def check_existing(self, email):
        return any(email == student['email'] for student in self.all_students.values())

    def add_points(self, id_student, python, dsa, database, flask):

        if id_student not in self.students_point:
            self.popular[id_student] = {'python': 0, 'dsa': 0, 'database': 0, 'flask': 0}
            self.activity[id_student] = {'python': 0, 'dsa': 0, 'database': 0, 'flask': 0}  # Initialize activity


        if id_student not in self.students_point:
            self.students_point[id_student] = {'python': 0, 'dsa': 0, 'database': 0, 'flask': 0}
            self.completed[id_student] = {'python': 0, 'dsa': 0, 'database': 0, 'flask': 0}
            self.student_notify[id_student] = {0}


        self.students_point[id_student]['python'] += python

        if python > 0:
            self.popular[id_student]['python'] = 1
            self.activity[id_student]['python'] += 1

        self.students_point[id_student]['dsa'] += dsa
        if dsa > 0:
            self.popular[id_student]['dsa'] = 1
            self.activity[id_student]['dsa'] += 1


        self.students_point[id_student]['database'] += database
        if database > 0:
            self.popular[id_student]['database'] = 1
            self.activity[id_student]['database'] += 1

        self.students_point[id_student]['flask'] += flask
        if flask > 0:
            self.popular[id_student]['flask'] = 1
            self.activity[id_student]['flask'] += 1



        print(f'Points updated for student ID {id_student}.')

    def notify(self):
        for idd, courses in self.students_point.items():
            for course, value in courses.items():
                if course =='python' and value >= 600 and self.completed[idd]['python'] == 0 :
                    print('To: {}'.format(student_instance.all_students[idd]['email']))
                    print('Re: Your Learning Progress')
                    print('Hello, {} {}! You have accomplished our Python course!'
                          .format(student_instance.all_students[idd]['first name'],
                                  student_instance.all_students[idd]['last name']))
                    self.completed[idd]['python'] = 1
                    self.student_notify[idd] = 1

                if course =='dsa' and value >= 400 and self.completed[idd]['dsa'] == 0 :
                    print('To: {}'.format(student_instance.all_students[idd]['email']))
                    print('Re: Your Learning Progress')
                    print('Hello, {} {}! You have accomplished our DSA course!'
                          .format(student_instance.all_students[idd]['first name'],
                                  student_instance.all_students[idd]['last name']))
                    self.completed[idd]['dsa'] = 1
                    self.student_notify[idd] = 1

                if course =='database' and value >= 480 and self.completed[idd]['database'] == 0 :
                    print('To: {}'.format(student_instance.all_students[idd]['email']))
                    print('Re: Your Learning Progress')
                    print('Hello, {} {}! You have accomplished our Databases course!'
                          .format(student_instance.all_students[idd]['first name'],
                                  student_instance.all_students[idd]['last name']))
                    self.completed[idd]['database'] = 1
                    self.student_notify[idd] = 1

                if course =='flask' and value >= 550 and self.completed[idd]['flask'] == 0 :
                    print('To: {}'.format(student_instance.all_students[idd]['email']))
                    print('Re: Your Learning Progress')
                    print('Hello, {} {}! You have accomplished our flask course!'
                          .format(student_instance.all_students[idd]['first name'],
                                  student_instance.all_students[idd]['last name']))
                    self.completed[idd]['flask'] = 1
                    self.student_notify[idd] = 1

        for x, y in self.student_notify.items():
            if y == 1:
                self.student_notify[x] = 2
                global counter
                counter += 1

        print('Total {} students have been notified.'.format(counter))





    def find_student(self, id_student):
        """Return student details by ID if exists."""
        # Check if the ID can be converted to an integer
        try:
            int_id = int(id_student)  # Convert to integer here to check with keys
            if int_id in student_instance.all_students:
                points = self.students_point.get(int_id, {'python': 0, 'dsa': 0, 'database': 0, 'flask': 0})
                return f"{int_id} points: Python={points['python']}; DSA={points['dsa']}; Databases={points['database']}; Flask={points['flask']}"
            else:
                return None
        except ValueError:
            return None  # Return None if the ID is not a valid integer

    def statistics(self):
        for x, y in self.activity.items():
            for a, z in y.items():
                if a == 'python' and z > 0:
                    self.python_activity += z
                if a == 'dsa' and z > 0:
                    self.dsa_activity += z
                if a == 'database' and z > 0:
                    self.database_activity += z
                if a == 'flask' and z > 0:
                    self.flask_activity += z

        for x, y in self.popular.items():
            for a, z in y.items():
                if a == 'python' and z > 0:
                    self.python_populatry += 1
                if a == 'dsa' and z > 0:
                    self.dsa_populatry += 1
                if a == 'database' and z > 0:
                    self.database_populatry += 1
                if a == 'flask' and z > 0:
                    self.flask_populatry += 1

        for x, y in self.students_point.items():
            for a, z in y.items():
                if a == 'python' and z > 0:
                    self.python_score += 1
                    self.python_score_total += z
                if a == 'dsa' and z > 0:
                    self.dsa_score += 1
                    self.dsa_score_total += z
                if a == 'database' and z > 0:
                    self.database_score += 1
                    self.database_score_total += z
                if a == 'flask' and z > 0:
                    self.flask_score += 1
                    self.flask_score_total += z

        self.popularity_dict = {
            'Python': self.python_populatry,
            'DSA': self.dsa_populatry,
            'Databases': self.database_populatry,
            'Flask': self.flask_populatry
        }

        self.activity_dict = {
            'Python': self.python_activity,
            'DSA': self.dsa_activity,
            'Databases': self.database_activity,
            'Flask': self.flask_activity
        }

        self.course_dict = {
            'Python': self.python_score_total /  self.python_score,
            'DSA': self.dsa_score_total /  self.dsa_score,
            'Databases': self.database_score_total /  self.database_score,
            'Flask': self.flask_score_total /  self.flask_score,
        }



        self.most_popluer = max(self.popularity_dict.values())
        self.most_popluer = ', '.join([course for course, value in self.popularity_dict.items() if value == self.most_popluer ])
        self.least_popular = min(self.popularity_dict.values())
        self.least_popular = ', '.join([course for course, value in self.popularity_dict.items() if value == self.least_popular and course not in self.most_popluer ])
        if self.least_popular == '':
            self.least_popular = 'n/a'

        self.highest_activity = max(self.activity_dict.values())
        self.highest_activity = ', '.join([course for course,value in self.activity_dict.items() if value == self.highest_activity ])
        self.lowest_activity = min(self.activity_dict.values())
        self.lowest_activity = ', '.join([course for course,value in self.activity_dict.items() if value == self.lowest_activity and course not in self.highest_activity])
        if self.lowest_activity == '':
            self.lowest_activity = 'n/a'
        self.easiest_course = max(self.course_dict.values())
        self.easiest_course = ', '.join([course for course,value in self.course_dict.items() if value == self.easiest_course ])
        self.hardest_course = min(self.course_dict.values())
        self.hardest_course =', '.join([course for course,value in self.course_dict.items() if value == self.hardest_course and course not in self.easiest_course ])
        if self.hardest_course == '':
            self.hardest_course = 'n/a'
        if len(self.popular) > 0:
            pass

    def completed_courses(self,coursename):
        if len(self.all_students) > 0:
            self.python_completed = [(x,a,z, z / 600) for x, y in self.students_point.items() for a, z in y.items() if a == 'python']
            self.dsa_completed = [(x,a,z, z / 400) for x, y in self.students_point.items() for a, z in y.items() if a == 'dsa']
            self.databases_completed = [(x,a,z, z / 480) for x, y in self.students_point.items() for a, z in y.items() if a == 'database']
            self.flask_completed = [(x,a,z, z / 550) for x, y in self.students_point.items() for a, z in y.items() if a == 'flask']
            if coursename == 'Python':
                print('Python')
                print('id    points    completed')
                self.python_completed.sort(key=lambda x: x[2], reverse=True)
                if len(self.python_completed) > 0:
                    for x, y, z, i in self.python_completed:
                        if z > 0:
                            print('{}     {}         {}%'.format(x, z, round(i * 100, 1)))
            if coursename == 'DSA':
                print('DSA')
                print('id    points    completed')
                self.dsa_completed.sort(key=lambda x: x[2], reverse=True)
                if len(self.dsa_completed) > 0:
                    for x, y ,z,i in self.dsa_completed:
                        if z > 0:
                            print('{}     {}         {}%'.format(x,z,round(i * 100,1)))

            if coursename == 'Databases':
                print('Databases')
                print('id    points    completed')
                self.databases_completed.sort(key=lambda x: x[3], reverse=True)
                if len(self.databases_completed) > 0:
                    for x, y, z, i in self.databases_completed:
                        if z > 0:
                            print('{}     {}         {}%'.format(x, z, round(i * 100, 1)))
            if coursename == 'Flask':
                print('Flask')
                print('id    points    completed')
                self.flask_completed.sort(key=lambda x: x[2], reverse=True)
                if len(self.flask_completed) > 0:
                    for x, y, z, i in self.flask_completed:
                        if z > 0:
                            print('{}     {}         {}%'.format(x, z, round(i * 100, 1)))


# Main Program
print('Learning progress tracker')

answer = input().strip()
while answer != 'exit':
    students_added = 0
    if answer == '':
        print('No input.')
    elif answer == 'add points':
        print("Enter an id and points or 'back' to return:")
        answer3 = input().split()

        while answer3[0] != 'back':
            try:
                student_id = int(answer3[0])  # Convert student ID to integer for adding points
                if student_id in student_instance.all_students:
                    # Validate the points: ensure they are integers and non-negative
                    if len(answer3) == 5:
                        try:
                            points = list(map(int, answer3[1:]))  # Convert point inputs to integers
                            if all(p >= 0 for p in points):  # Ensure all points are non-negative
                                # Call add_points on the class with valid data
                                  student_instance.add_points(student_id, *points)
                            else:
                                print("Points must be non-negative integers.")
                        except ValueError:
                            print("Incorrect points format. Points should be valid integers.")
                    else:
                        print("Incorrect points format. Please enter the ID and exactly 4 points.")
                else:
                    print(f"No student found with ID={answer3[0]}.")
            except ValueError:
                print(f"No student found with ID={answer3[0]}.")

            answer3 = input().split()  # Ask for points again
    elif answer == 'list':
        try:
            if len(student_instance.all_students) > 0:
                print('Students:')
                for x in student_instance.all_students:
                    print(x)
            else:
                print('No students found.')
        except AttributeError:
            print('No students found.')
    elif answer == 'add students':
        print("Enter student credentials or 'back' to return")
        answer2 = input().strip()


        while answer2 != 'back':
            credentials = answer2.split()

            if len(credentials) < 3:
                print('Incorrect credentials.')
            else:
                firstname = credentials[0]
                email = credentials[-1]
                lastname = ' '.join(credentials[1:-1])
                student_instance = Student(firstname, lastname, email)  # Create a Student instance

            answer2 = input().strip()

        print(f'Total {students_added} students were added.')
    elif answer == 'find':
        print("Enter an id or 'back' to return.")
        answer4 = input().strip()
        while answer4 != 'back':
            try:
                student_id4 = int(answer4)
                if student_instance != None:
                    if student_instance.find_student(int(answer4)):
                        print(student_instance.find_student(int(answer4)))
                    else:
                        print(f"No student is found for id={answer4}.")
            except ValueError:
                print(f"No student is found for id={answer4}.")

            answer4 = input().strip()
    elif answer == 'back':
        print("Enter 'exit' to exit the program")
    elif answer == 'statistics':
        print("Type the name of a course to see details or 'back' to quit:")
        if student_instance != "n/a":
            student_instance.statistics()
            print("Most popular: {}".format(student_instance.most_popluer))
            print("Least popular: {}".format(student_instance.least_popular))
            print("Highest activity: {}".format(student_instance.highest_activity))
            print("Lowest activity: {}".format(student_instance.lowest_activity))
            print("Easiest course: {}".format(student_instance.easiest_course))
            print("Hardest course: {}".format(student_instance.hardest_course))
        elif student_instance == "n/a":
            print("Most popular: n/a")
            print("Least popular: n/a")
            print("Highest activity: n/a")
            print("Lowest activity: n/a")
            print("Easiest course: n/a")
            print("Hardest course: n/a")

        answer_stat = input().strip()
        while answer_stat != 'back':
            if student_instance != "n/a":
                if answer_stat == 'Python' or  answer_stat == 'python':
                    student_instance.completed_courses('Python')
                elif answer_stat == 'DSA' or  answer_stat == 'dsa':
                    student_instance.completed_courses('DSA')
                elif answer_stat == 'Flask' or  answer_stat == 'flask':
                    student_instance.completed_courses('Flask')
                elif answer_stat == 'Databases' or  answer_stat == 'databases':
                    student_instance.completed_courses('Databases')
                else:
                    print("Unknown course.")
            elif student_instance == "n/a":
                if answer_stat == 'Python' or  answer_stat == 'python':
                    print('Python')
                    print('id    points    completed')
                elif answer_stat == 'DSA' or  answer_stat == 'dsa':
                    print('DSA')
                    print('id    points    completed')
                elif answer_stat == 'Flask' or  answer_stat == 'flask':
                    print('Flask')
                    print('id    points    completed')
                elif answer_stat == 'Databases' or  answer_stat == 'databases':
                    print('Databases')
                    print('id    points    completed')
                else:
                    print("Unknown course.")

            answer_stat = input().strip()
    elif answer == 'notify':

        try:
            counter = 0
            student_instance.notify()
        except AttributeError:
            print('123')
    else:
        print("Unknown command!")
    answer = input()
print('Bye!')
