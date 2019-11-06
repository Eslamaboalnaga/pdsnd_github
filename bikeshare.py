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
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city =input('\nWould you like to see data for chicago, new york city, washington ?\n').lower()
        if city not in ('chicago','new york city','washington'):
            print('sorry, enter city of the previous cities.\n try again')
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('All right! now it\'s time to provide us a month name '\
                      'or just say \'all\' to apply no month filter. \
                      (e.g. all, january, february, march, april, may, june) \n> ')
        if month not in ('january', 'february', 'march', 'april', 'may', 'june','all'):
            print('Sorry, I do not understand your input. Please type in a '
                  'month between January and June or all')
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\n Which day ? please type one of the week day you want to analyze.'
                    ' You can type \'all\' again to apply no day filter.(e.g. all, monday, sunday)')
        if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','all' ):
            print('Sorry, I do not understand your input. Please type in a day or all')
        else:
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
    df= pd.read_csv(CITY_DATA[city])
    # convert the start time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from start time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month !='all':
        # use the index of the months list 
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month=months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print("The most common month is :", most_common_month)
   
    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of week is :", most_common_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print("The most common start hour is :", most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station :", start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station :", end_station)

    # TO DO: display most frequent combination of start station and end station trip
    start_end_station = df.groupby(['Start Station', 'End Station']).count()
    print("The most commonly used start station and end station : {}, {}".format(start_station, end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time :", total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts = df['User Type'].value_counts()
    print("Counts of user types:", user_counts)

    # TO DO: Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
        print("Counts of gender:", gender_counts)
    except KeyError:
        print('\n Gender_counts : no data available in washington.')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        print("The most earliest birth year:", earliest_year)
    except KeyError:
        print('\n earliest year : no data available in washington.')
    try:
        most_recent_year = df['Birth Year'].max()
        print("The most recent birth year:", most_recent_year)
    except KeyError:
        print('\n most recent year : no data available in washington.')
    
    try:
        most_common_year = df['Birth Year'].value_counts().idxmax()
        print("The most common birth year:", most_common_year)
    except KeyError:
        print('\n most common year : no data available in washington.')
                       
                     
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_row_data(df):
    """
    desplay the data used to compute the stats
    
    """
    # omit irrelevant columns from visualization
    row_index=0
    yes = input('\nWould you like to examine the particular user trip data? Type \'yes\' or \'no\'\n>    ').lower()
    while True:
        if yes == 'no':
            return
        if yes == 'yes':
            print(df[row_index:row_index + 5])
            row_index= row_index + 5
        yes = input('\nWould you like to examine the particular user trip data? Type \'yes\' or \'no\'\n>    ').lower()     
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_row_data(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
