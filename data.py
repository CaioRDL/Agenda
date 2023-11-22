# import module
import datetime
  
# get current date and time
current_date = datetime.date.today()
print("Current date & time : ", current_date)
  
# convert datetime obj to string
str_current_datetime = str(current_date)
  
# create a file object along with extension
file_name = str_current_datetime +".txt"
file = open(file_name, 'a')
  
print("File created : ", file.name)
file.close()
