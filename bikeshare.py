import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    
    cities = ('chicago', 'new york city', 'washington')
    
    while True:
        city = input('Which city do you want to explore? ').lower()
        if city in cities:
            break

    # get user input for month (all, january, february, ... , june)

    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
 
    while True:
        month = input('Which month do you want to explore? ').lower()
        if month in months:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)

    days = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    
    while True:
        day = input('Now please enter a day to get some days result. ').lower()
        if day in days:
            break
            
            
    print('-'*40)
    return city, month, day



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    
    # load datafile into a dataframe 
    df = pd.read_csv(CITY_DATA[city.lower()])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month, day of week, hour and trip to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    df['trip'] = df['Start Station'].astype(str) + ' / ' + df['End Station']

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':  
        # filter by day of week to create the new dataframe
        day = day.title()
        df = df[df['day_of_week'] == day]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
    # display the most common time
    popular_month = df['month'].mode()[0]
    popular_day = df['day_of_week'].mode()[0]
    popular_hour = df['hour'].mode()[0]
    
    print(' \n month: {}, \n day: {}, \n hour: {}'
          .format(popular_month, popular_day, popular_hour))

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    
    # display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('The Most Popular Start Station: ', popular_start)

    # display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('The Most Popular End Station: ', popular_end)

    # display most frequent combination of start station and end station trip
    popular_trip = df['trip'].mode()[0]
    print('The Most Popular Trip: ', popular_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    
    # display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total travel time: ', total_time)

    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('Mean travel time: ', mean_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    
    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types: ', user_types)

    # Display counts of gender
    # Washington data does not have Gender column.
    if 'Gender' in df:
        user_gender = df['Gender'].value_counts()
        print('Counts of user gender: ', user_gender)
    else:
        print ('No gender data available.')

    # Display earliest, most recent, and most common year of birth
    # Washington data does not have Birth Year column.
    if 'Birth Year' in df:
        user_birth_min = df['Birth Year'].min()
        user_birth_max = df['Birth Year'].max()
        user_birth = df['Birth Year'].value_counts()
        print('Earliest, most recent and most common year of birth: ', 
              user_birth_max, '\n', user_birth_min, '\n', user_birth)
    else:
        print ('No data on the year of birth.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def display_data(df):
    """Displays 5 rows of data."""
    
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0

    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_display = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
        if view_display != 'yes':
            break
            


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


            
if __name__ == "__main__":
	main()
