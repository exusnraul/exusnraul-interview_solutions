'''
•	Get all the items from dictionary whose value is more than given threshold with dict comprehension. Take input for dict and threshold value
'''
dic={'test':123,'test1':432,'test2':44}
a={key:val for key,val in dic.items() if val>200}