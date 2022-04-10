import re
import pandas as pd


def preprocess(data, time_format):
    if time_format == '12hr format':
        pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s(?:am|pm)\s-\s'
    else:
        pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'

    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)
    df = pd.DataFrame({'user_message': messages, 'date': dates})
    # convert message_data type

    if time_format == '12hr format':
        try:
            df['date'] = pd.to_datetime(df['date'], format='%d/%m/%y, %I:%M %p - ')
        except:
            df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y, %I:%M %p - ')


    else:
        df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y, %H:%M - ')

    users = []
    messages = []
    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification')
            messages.append(entry[0])
    df['user'] = users
    df['messages'] = messages
    df.drop(columns=['user_message'], inplace=True)

    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['only_date'] = df['date'].dt.date
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    if time_format == '12hr format':
        range = []
        for hour in df[['day_name', 'hour']]['hour']:
            if hour == 0:
                range.append(str("12am") + "-" + str("1am"))
            elif hour == 12:
                range.append(str("12pm") + "-" + str("1pm"))
            elif hour < 12:
                range.append(str(hour) + "am -" + str(hour + 1) + "am")
            else:
                range.append(str(hour - 12) + "pm -" + str(hour + 1 - 12) + "pm")

    else:
        range = []
        for hour in df[['day_name', 'hour']]['hour']:
            if hour == 23:
                range.append(str(hour) + "-" + str('00'))
            elif hour == 0:
                range.append(str('00') + "-" + str(hour + 1))
            else:
                range.append(str(hour) + "-" + str(hour + 1))

    df['range'] = range
    return df
