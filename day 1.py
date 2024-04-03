#!/usr/bin/env python
# coding: utf-8

# if statement 

# In[1]:


# if statement
i = 10
if i>5:
    print('i is greater than 5...')


# if-else statement

# In[3]:


i = 1
if i>5:
    print('i is greater than 5...')
else:
    print('i is less than 5')


# if-elif-else statement

# In[4]:


i = 10
if i==5:
    print('i is equal 5...')
elif i==10:
    print('i is equal 10..')
else:
    print('i is other..')


# Nested-if statements:

# In[7]:


marks = int(input("Enter the student's marks: "))
if marks >= 90:
    grade = 'A'
    if marks >= 95:
        distinction = True
elif marks >= 80:
    grade = 'B'
    distinction = False
elif marks >= 70:
    grade = 'C'
    distinction = False
elif marks >= 60:
    grade = 'D'
    distinction = False
else:
    grade = 'F'
    distinction = False

print("Grade:", grade)

if distinction:
    print("Distinction achieved!")


# Short hand if statement:

# In[8]:


# Short hand if statement
i = 10
if i<15: print('i less than 15..')


# In[9]:


#Short hand if-else statement
i = 10
print(True) if i==10 else print(False)


# In[11]:


flag = int(input('Enter num:'))

if flag == 5:
    print('Flag = 5')
elif flag == 10:
    print('Flag = 10')
elif flag == 15:
    print('Flag = 15')
elif flag == 20:
    print('Flag = 20')
else:
    print('Not matched')

        


# In[14]:


role = 'Admin'

if role == 'Emp' or role == 'User':
    print('Not allowed access..')
elif role == 'Admin':
    print('Allowed access to Admin..')
else:
    print('No role..')

