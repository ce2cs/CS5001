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

This code only works if the month that is entered in the keyboard is entered
in using their 3-letter abbreviation. Modify the code to be able to handle full
month names as well as their numeric equivalent.

For example, Feb, February, and 2 would set days = 28.
Do this using logical operators.
"""


def main():
    month = input("Enter month: ")
    # determine the number of days
    if month == "Jan" or month == "January" or month == "1":
        days = 31
    elif month == "Feb" or month == "February" or month == "2":
        days = 28
    elif month == "Mar" or month == "March" or month == "3":
        days = 31
    elif month == "Apr" or month == "April" or month == "4":
        days = 30
    elif month == "May" or month == "5":
        days = 31
    elif month == "Jun" or month == "June" or month == "6":
        days = 30
    elif month == "Jul" or month == "July" or month == "7":
        days = 31
    elif month == "Aug" or month == "August" or month == "8":
        days = 31
    elif month == "Sep" or month == "September" or month == "9":
        days = 30
    elif month == "Oct" or month == "October" or month == "10":
        days = 31
    elif month == "Nov" or month == "November" or month == "11":
        days = 30
    elif month == "Dec" or month == "December" or month == "12":
        days = 31
    else:
        days = "Unknown"
    print(month, "has", days, "days")


if __name__ == '__main__':
    main()
