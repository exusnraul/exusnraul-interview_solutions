'''
•	Find Nth day from given day of the week. Take 2 input which are number of days to be count and second is from which day. Say count 23 days from “Thursday” which will be “Saturday”
days=[ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

'''

def counts(curr_day,days_to_count):
    days=[ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if curr_day in days:
        a=len(days)-1
        idx_cur=days.index(curr_day)
        count=days_to_count//a
        dig=days_to_count%7
        if dig+idx_cur>a:
            return days[idx_cur-dig]
        else:
            return days[idx_cur+dig]
    else:
        return ValueError('Input Expected Inputs')
    
counts('Thursday',4)