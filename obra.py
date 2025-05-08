#Deros.All rights reserved
#=========================

class Person:
    def __init__(self, name, surname, age, email):
        try:
            self.test(name)    
            self.name = name
        except:
             print('Неверно указанно имя')
        try:
            self.test(surname)    
            self.surname = surname
        except:
             print('Неверно указанно фамилия')
        try:
            if int(age) > 0 and int(age) < 125:
                    self.age = int(age)
            else:
                 raise ValueError
        except:
             print('Введи нормальный возвраст, чурка')
        try:
            if '@' in email and '.' in email:
                if email[email.find('@') + 1] in range(97, 123) or email[email.find('@') + 1] in range(48, 58):
                     if email[email[(email.find('@')):].find('.')] in range(97, 123):
                        self.email = email
                else:
                    raise ValueError
            else:
                 raise ValueError
        except:
             print('Это, блэт, не email')
    def test(self, name):
         asc = [ord(char) for char in name]
         for i in asc:
              if i not in range(97, 123) and i != 45:
                   raise ValueError
    
    def __del__(self):
         print('Has been deleted')

cv = Person('asdfa-asd', 'qwe', 12, 'weqwe@1.fg')