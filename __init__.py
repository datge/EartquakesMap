from elaborate import elaborate
def main():
    pressed=input("Press 1 for last hour eartquakes,2 for today eartquakes,3 for this week eartquakes and 4 for past 30 days eartquakes(press 'q' for exit):\n")
    if pressed =='q':
        print("good bayz")
    elif pressed == '1':
        csv = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.csv'

    elif pressed == '2':
        csv = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.csv'

    elif pressed == '3':
        csv = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.csv'

    elif  pressed == '4':
        csv = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv'
    else:
        print("no")
    return csv

if __name__ =='__main__':
    csv = main()
    elaborate(csv)


