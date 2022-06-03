#Decorator
def deco(result_func):
    def distinct(marks):
        for m in marks:
            if m>=75:
                print('Distinction')
        result_func(marks)
    return distinct
@deco
def result(marks):
    for i in marks:
        if i<=33:
            print("Fail")
            break
    else:print("Pass")
    
result([40,50,60,70,80,33,90])