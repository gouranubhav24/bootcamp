seconds = int(input("enter the number of seconds"))
days = seconds/(60*60*24)
hours =  (seconds%(60*60*24))/(60*60)
minutes = (seconds%(60*60))/60
sec = (seconds%60)




print('seconds = ',sec)
print('minutes = ',int(minutes))
print('hours = ',int(hours))
print('days = ',int(days))