#Should I get up and go to work, or sleep in?

days_of_the_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
day = int(input("Day (0-6)? "))
if day == 0 or day == 6:
    print("Sleep in, it's the weekend.")
else:
    print("Go to work!");
