import time
import pandas as pd
import calendar

CITY_DATA = { 'chicago':'chicago.csv', 'new york city':'new_york_city.csv', 'washington': 'washington.csv' }
months = ["january", "feburaury", "march", "april", "may", "june"]

def get_filters():
    """ This Function maintain the flow of input for 3 variables we have city and month
and day it using loop to avoid invalid inputs every time the input is invalid 
the same messege gona appear bu if the it is a valid input the loop wil break 


"""
# This function takes the input from user.
    while True:
        city = input("please make sure your choice between:\n 1. chicago 2. new york city 3. washington \n" ).lower()
        if city not in CITY_DATA:
            print("please chose again") ##finish beter line 
        else:
            break
    
    while True:
     month = input("choose a month between January and june or all \n").lower()##finish beter line
     months = ["january", "feburaury", "march", "april", "may", "june"]

     if month != 'all' and month not in months:
          print("please choose again") ##finish beter line 
     else:
          break
     while True:
          
         day = input("choose a day or all \n").lower()
         days = ["sunday", "monday", "tuesday", "wendsday", "thursday",  "friday", "saturday"]

         if day != 'all' and day not in days:
               print("please chose again") ##finish beter line 
         else:
               break
           
     print('-'*40)
     return city, month, day
           
           # using while to make sure that the input matches the data i aready have
           ## you need to put months and day in index to make it easier 
           
          
          
          
          
    
#     print("Please choose your city: ")
#     print("\n1. Chicago 2. New York City 3. Washington")
   
#     print("\nAccepted input:\nFull name of city; not case sensitive (e.g. chicago or CHICAGO).\nFull name in title case (e.g. Chicago).")
    




#     print('-'*40)
#     return city, month, day
# #### it is finshed and run in it is own 



def load_data(city, month, day):

    #take the input and compare it with what you have
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    #Filter month
    
    if month != 'all':
       
        months = ["january", "feburaury", "march", "april", "may", "june"]
 
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    

    # display the most common month

    common_month = df["month"].mode()[0] ## choose the va
  

    # display the most common day of week
    common_day = df["day_of_week"].mode()[0] ## choose the va
    
    


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Popular hour:', common_hour)
    # Dont forget change all variables in each cell
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('Most Popular Month:', common_month)
    print('Most Popular Day:', common_day)
    print('Most Popular hour:', common_hour)


def station_stats(df): # Finshed but still soe in varables
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_used_start = df['Start Station'].mode()[0]
    

    # display most commonly used end station
    most_used_end = df['End Station'].mode()[0]
    


    # display most frequent combination of start station and end station trip
    most_start_end = df['Start Station'] + " " + df['End Station'].mode()[0]
    
    print("The Most Crowded  Start Station is",most_used_start)
    print("The Most Crowded End Station is",most_used_end)
    print("The Most Common between both",most_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    
    

    # display mean travel time
    averg_travel_time = df['Trip Duration'].mean()

    print('The Total Travel Time is', total_time/3600 ,'hours' )##Totla time in hours
    print('The Average Time of Travel is', averg_travel_time/3600, 'hours')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_users = df['User Type'].value_counts()
    print('Counts of user type',count_users)



    # Display counts of gender
    if 'Gender' in df:
        print('Count Gender',df['Gender'.value_counts()])


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        youngest_age = int(df['Birth year'].min())
        print("The Youngest year is", youngest_age)
        recent_year = int(df['Birth Year'].max())
        print('The Largest year is', recent_year)
        most_common = int(df['Birth Year'].mode()[0])
        print('The Most Frequent year is',most_common)
        
        
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
 	main()
