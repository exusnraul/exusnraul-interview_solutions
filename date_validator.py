'''
•	Check if given date is valid or not in DD-MM-YYYY format.
'''
def datechecker(date_input):
    import datetime
    if isinstance(date_input,str):
        try:
            datetime.datetime.strptime(date_input,"%d-%m-%Y")
            return 'Correct Format Passed'
        except ValueError:
            return ValueError("Incorrect date format")
        
datechecker('02-12-202')