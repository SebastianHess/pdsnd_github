import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def error_1():
    e1 = '### Invalid city name! Please input Chicago, New York City or Washington! ###'
    return e1

def error_2():
    e2 = '### Invalid input! Please input "month", "day", "both" or "none" ###'
    return e2

def error_3():
    e3 = '### Invalid input! Please input "All", "January", "February", "March", "April", "May", "June" ###'
    return e3

def error_4():
    e4 =  '### Invalid input! Please input "0 = All", "1 = Sunday", "2 = Monday", "3 = Tuesday", "4 = Wednesday", "5 = Thursday", "6 = Friday", "7 = Saturday" ###'
    return e4

def line():
    line = print('-'*40)
    return line
    
def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        try:
            city = str(input('Would you like to see data for Chicago, New York City or Washington? [Enter city name]: ')).lower()
            if city in CITY_DATA.keys():
                print('Looks like you want to hear about ' + city.title() + '! If this is not true, restart the program now!') 
                restart = input('Would you like to restart? [Enter "yes" or "no"].\n').lower()
                if restart.lower() != 'yes':
                    break
            else:
                line()
                print(error_1())
                line()
        except NameError:
            line()
            print(error_1())
            line()    

    filters = ['month', 'day', 'both', 'none']
    while True:
        try:
            filter = str(input('Would you like to filter the data by month, day, both or not at all? [Type "none" for no time filter]: ')).lower()
            if filter in filters:
                break
            else:
                line()
                print(error_2())
                line()
        except NameError:
            line()
            print(error_2())
            line()
    
    ifvalue = 'all'
    if filter == 'month':      
        months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
        while True:
            try:
                month = str(input('Which month? [Enter: "All", "January", "February", "March", "April", "May", "June"]: ')).lower()
                if month in months:
                    month = month.title()
                    day = str(ifvalue)
                    break
                else:
                    line()
                    print(error_3())
                    line()
            except NameError:
                line()
                print(error_3())  
                line()
    elif filter == 'day':
        days = {'all' : 0,
                'sunday' : 1,
                'monday' : 2,
                'tuesday' : 3,
                'wednesday' : 4,
                'thursday' : 5,
                'friday' : 6,
                'saturday' :7}
        while True:
            try:
                day_input = int(input('Which day? [Enter an integer "0 for All", "1 for Sunday", "2 for Monday", "3 for Tuesday", "4 for Wednesday", "5 for Thursday", "6 for Friday", "7 for Saturday"]: '))
                if day_input == 0:
                    day = str(ifvalue).title()
                    month = str(ifvalue)
                    break
                elif day_input == 1:
                    day = str('sunday').title()
                    month = str(ifvalue)
                    break
                elif day_input == 2:
                    day = str('monday').title()
                    month = str(ifvalue)
                    break
                elif day_input == 3:
                    day = str('tuesday').title()
                    month = str(ifvalue)
                    break
                elif day_input == 4:
                    day = str('wednesday').title()
                    month = str(ifvalue)
                    break
                elif day_input == 5:
                    day = str('thursday').title()
                    month = str(ifvalue)
                    break
                elif day_input == 6:
                    day = str('friday').title()
                    month = str(ifvalue)
                    break
                elif day_input == 7:
                    day = str('saturday').title()
                    month = str(ifvalue)
                    break
                else:
                    line()
                    print(error_4())
                    line()
            except ValueError:
                line()
                print(error_4())
                line()    
    elif filter == 'both':      
        months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
        while True:
            try:
                month = str(input('Which month? [Enter: "All", "January", "February", "March", "April", "May", "June"]: ')).lower()
                if month in months:
                    month = month.title()
                    break
                else:
                    line()
                    print(error_3())
                    line()
            except NameError:
                line()
                print(error_3())
                line()
   
        days = {'all' : 0,
                'sunday' : 1,
                'monday' : 2,
                'tuesday' : 3,
                'wednesday' : 4,
                'thursday' : 5,
                'friday' : 6,
                'saturday' :7}
        while True:
            try:
                day_input = int(input('Which day? [Enter an integer "0 for All", "1 for Sunday", "2 for Monday", "3 for Tuesday", "4 for Wednesday", "5 for Thursday", "6 for Friday", "7 for Saturday"]: '))
                if day_input == 0:
                    day = str(ifvalue).title()
                    month = str(ifvalue)
                    break
                elif day_input == 1:
                    day = str('sunday').title()
                    month = str(ifvalue)
                    break
                elif day_input == 2:
                    day = str('monday').title()
                    month = str(ifvalue)
                    break
                elif day_input == 3:
                    day = str('tuesday').title()
                    month = str(ifvalue)
                    break
                elif day_input == 4:
                    day = str('wednesday').title()
                    month = str(ifvalue)
                    break
                elif day_input == 5:
                    day = str('thursday').title()
                    month = str(ifvalue)
                    break
                elif day_input == 6:
                    day = str('friday').title()
                    month = str(ifvalue)
                    break
                elif day_input == 7:
                    day = str('saturday').title()
                    month = str(ifvalue)
                    break
                else:
                    line()
                    print(error_4())
                    line()
            except ValueError:
                line()
                print(error_4())
                line()
    elif filter == 'none':
        month = str(ifvalue)
        day = str(ifvalue)

    line()
    print('\nYour inputs were:\n\nCity:\t{}\nFilter:\t{}\nMonth:\t{}\nDay:\t{}\n'.format(city.title(), filter.title(), month.title(), day.title()))            
    line()
    
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day
    
    ifvalue = 'all' 
    if month != ifvalue:
        months = ['All', 'January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) +1
        df = df.loc[df['month'] == month,:]

    if day != ifvalue:
        days = ['All', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        day = days.index(day) +1
        df = df.loc[df['day'] == day,:]

    return df


def time_stats(df, month, day):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    ifvalue = 'all'
    if month != ifvalue:
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['month'] = df['Start Time'].dt.month
        popular_month = df['month'].mode().values[0]
        if popular_month == 0:
            popular_month = 'All'
        elif popular_month == 1:
            popular_month = 'January'
        elif popular_month == 2:
            popular_month = 'February'
        elif popular_month == 3:
            popular_month = 'March'
        elif popular_month == 4:
            popular_month = 'April'
        elif popular_month == 5:
            popular_month = 'May'
        elif popular_month == 6:
            popular_month = 'June'
        print('Most Common Month:\t\t{}'.format(popular_month))
    else:     
        print('Most Common Month:\t\tFilter "All" selected!')
    
    if day != ifvalue:
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['day'] = df['Start Time'].dt.day

        popular_day = df['day'].mode().values[0]
        if popular_day == 0:
            popular_day = 'All'
        if popular_day == 1:
            popular_day = 'Sunday'
        elif popular_day == 2:
            popular_day = 'Monday'
        elif popular_day == 3:
            popular_day = 'Tuesday'
        elif popular_day == 4:
            popular_day = 'Wednesday'
        elif popular_day == 5:
            popular_day = 'Thursday'
        elif popular_day == 6:
            popular_day = 'Friday'
        elif popular_day == 7:
            popular_day = 'Saturday'
        print('Most Common Day:\t\t{}'.format(popular_day))
    else:        
        print('Most Common Day:\t\tFilter "All" selected!')

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode().values[0] 
    
    print('Most Frequent Start Hour:\t{}'.format(popular_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    line()


def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Frequent Start Station:\t{}'.format(popular_start_station))
    popular_end_station = df['End Station'].mode()[0]
    print('Most Frequent End Station:\t{}'.format(popular_end_station))
    popular_start_end_station = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('\nMost Frequent Combination Of Start Station And End Station Trip:\n\n{}'.format(popular_start_end_station))
    print("\nThis took %s seconds." % (time.time() - start_time))
    line()


def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    total_travel_time = int(df['Trip Duration'].sum())
    print('The Total Travel Time Was:\t{}'.format(total_travel_time))
    total_travel_time = int(df['Trip Duration'].mean())
    print('The Mean Travel Time Was:\t{}'.format(total_travel_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    line()


def user_stats(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    user_types = df['User Type'].value_counts()
    print('The Counts Of User Types Are:\n\n{}'.format(user_types)) 
    
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print('\nThe Counts Of Gender Are:\n\n{}'.format(gender))
    else:
        print('Gender Column Does Not Exist!')
    
    if 'Birth Year' in df.columns:
        earliest_birth_year = min(df['Birth Year'])
        print('\nThe Earliest Birth Year Is:\t{}'.format(int(earliest_birth_year)))
   
        recent_birth_year = max(df['Birth Year'])
        print('The Recent Birth Year Is:\t{}'.format(int(recent_birth_year)))
    
        common_birth_year = df['Birth Year'].mode()
        print('The Common Birth Year Is:\t{}'.format(int(common_birth_year)))
    else:
        print('Birth Year Column Does Not Exist!')    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    line()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        i = 0
        raw_5 = input('\nWould you like to display 5 lines of raw data? [Enter "yes" or "no"].\n').lower()
        pd.set_option('display.max_columns', 200)
        while True:
            if raw_5 == 'no':
                break
            print(df[i:i+5])
            raw_5 = input('\nWould you like to display the next 5 lines of raw data? [Enter "yes" or "no"].\n').lower()
            i += 5
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
