import datetime
import Random_function
date_entry = input('Enter a date in MM-DD format: ')
month, day = map(int, date_entry.split('-'))
spacial_day = input('Is today your birthday: ')

wishes_for_birthday=["Hope all your birthday wishes come true!", "It is your special day — get out there and celebrate!"
    , "It is your special day — get out there and celebrate!", "Wishing you the biggest slice of happy today.", "I hope your celebration gives you many happy memories!"
    , "Our age is merely the number of years the world has been enjoying us!"]
wishes_for_good_day=["We got to live only once so make great things and enjoy life.", "Wishing you a great day."
    ,"May you be loved more and more everyday.", "Never give up, hurdles do come your way, learn to overcome them and reach your goal."]
wishes_for_christmas=["May the Christmas Season bring only happiness and joy to you and your family."
    ,"The gift of love.","Wishing you a season full of light and laughter for you and your family."
    ,"Best wishes for a joyous Christmas filled with love, happiness and prosperity!"]

if spacial_day in ("Yes", "yes"):
    wishes = Random_function.get_random_wishes(wishes_for_birthday)
    print(wishes)
elif month!=12 or day !=25:
    wishes = Random_function.get_random_wishes(wishes_for_good_day)
    print(wishes)
elif month==12 and day ==25:
    wishes = Random_function.get_random_wishes(wishes_for_christmas)
    print(wishes)