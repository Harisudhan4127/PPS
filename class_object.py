class student:
    roll_No = 123
    name = 'abc'
    branch = 'CSE'
    
    def read(self):
        roll_No = 7847
        print('\nself.roll_No :',self.roll_No)
        print('read roll_N0',roll_No)
        print('Reading')

abc = student()

print('roll number :', abc.roll_No)
print('name :', abc.name)
print('branch :', abc.branch)

abc.read()