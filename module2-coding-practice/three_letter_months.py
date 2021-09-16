"""
Consider the following code:
def main():
   month = input("Enter month: ")
   # determine the number of days
   if month == "Jan":
       days = 31
   elif month == "Feb":
       days = 28
   elif month == "Mar":
       days = 31
   elif month == "Apr":
       days = 30
   elif month == "May":
       days = 31
   elif month == "Jun":
       days = 30
   elif month == "Jul":
       days = 31
   elif month == "Aug":
       days = 31
   elif month == "Sep":
       days = 30
   elif month == "Oct":
       days = 31
   elif month == "Nov":
       days = 30
   elif month == "Dec":
       days = 31
   else:
       days = "Unknown"
   print(month, "has", days, "days")

This code only works if the month that is entered in the keyboard is entered in using their 3-letter abbreviation.
Modify the code to be able to handle full month names as well as their numeric equivalent.
For example, Feb, February, and 2 would set days = 28. Do this using logical operators.
"""


def main():
    month = input("Enter month: ")
    # determine the number of days
    if month == "Jan" or "January" or "1":
        days = 31
    elif month == "Feb" or "February" or "2":
        days = 28
    elif month == "Mar" or "March" or "3":
        days = 31
    elif month == "Apr" or "April" or "4":
        days = 30
    elif month == "May" or "5":
        days = 31
    elif month == "Jun" or "June" or "6":
        days = 30
    elif month == "Jul" or "July" or "7":
        days = 31
    elif month == "Aug" or "August" or "8":
        days = 31
    elif month == "Sep" or "September" or "9":
        days = 30
    elif month == "Oct" or "October" or "10":
        days = 31
    elif month == "Nov" or "November" or "11":
        days = 30
    elif month == "Dec" or "December" or "12":
        days = 31
    else:
        days = "Unknown"
    print(month, "has", days, "days")


if __name__ == '__main__':
    main()
