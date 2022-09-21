
# Whatsapp Chat Analyzer

Discover more about your WhatsApp conversations.

This application can be used in two ways:                  
  - on overall group members 
  - on individual member

## Documentation



Step 1: Get the chat
-
The data is taken ,  
  - Whatsapp -> select chat -> ⋮ (on top left) -> more -> Export chat -> without media.

Step 2: Preprocess the data
-
- The textfile is converted inot Pandas dataframe by splitting into two lists with 'date' and 'user_message' using regular expression.
- User is required to select the date_format, since regular expression differs for 12hr or 24hr.
- 'user_message' column is further splitted into two columns, one with 'user_name' and the other with 'message'.
- Year, Month, Day, Hour, Minute are further extracted from 'date' and added to the Pandas dataframe.

Step 3: Analysis
-
 First I displayed 'Top Statistics', containing:
   -
  
  1 . Total Messages- 
  - This is achieved by using df.shape() function. It returns number of rows and columns.
  - Applying df.shape(0), returns rows, therby number of messages.
  
  2 . Total Words
  - Splitted all the messages on the basis of spaces and extended to a list, and returned the length of list.
  
  3 . Media Shared
  - When I exported chat from Whatsapp, I selected "without media". In dataframe, we find '<Media Omitted>\n' instead of media.
  - So, counting total number of 'Media Omitted>\n' would give total number of media.
  
  4 . Links Shared
  - Added all the URLs in a list using 'find_urls()' function of 'URLExtract' class of "urlextract" library. Returned the length of list.
 
  
  
  Now I found Busiest_User [group level, not on userlevel]
    -

  Made two columns: 
  
  - In column 1, apllied 'value_counts()' function on 'user' column in dataframe to return user names and count of their of messages. Applied 'head()' function on top of dataframe to get first 5 rows, therby 5 Busiest_Users containing user_message and number of messages.
  - Used 'matplotlb.pyplot' library to display bar_graph with x-axis user_name and y-axis number of messages.
  - In column 2, displayed a dataframe of 'user_name' and the 'percentage' of chats of 'user'.
  - This was done by dividing 'number of message of particular user' with 'total number of messages'.

 Displayed a WordCloud
   -
   
   - Generally, WordCloud is an image in which the size of each word indicates its frequency. But, there is a problem with words that have no use like '<Media omitted>\n', 'group_notifications' and stop_words like the, is, and etc. So, removed these words.
   - Used 'wordcloud' library and generated an image on 'message' column of dataframe using 'generate()' function and displayed using "subplots()" function.

 Finding most common 20 words
 -
  
- Similarly, like WordCloud first I filtered all the insignificant words from the messages and added into a list.

- Used Collections moudule, applied 'counter().most_common(20)' on the list to return top 20 words and  using "subplots()" function displayed an horizontal bargraph.

Emoji Analysis
 -

- Using 'emoji' library, I took emoji from every message with 'emoji.UNICODE_EMOJI['en']]' and extended to a list.
- Aplleid 'counter().most_common()' and converted into a dataframe.

TIME-BASED ANALYSIS
 -

 1 . Monthly_Timeline
- A new datafrmae 'timeline' is created by grouping 'month', 'year' columns and applying 'count()' on 'message' column.
- Using 'subplot()' function of 'matplotlib', dataframe is plot with x-axis 'time' and y-axis 'number of messages'.

 2 . Daily_Timeline
 - A new dataframe 'daily_timeline' is created by grouping 'date' and applying count on 'message'.
 - Using 'subplot()' function  of 'matplotlib', dataframe is plot with x-axis 'date' and y-axis 'number of messages'.
 
3 . Activity_Map
- Finding the day and the month that saw the most communication.
- Extracted day_name and month and applied 'value_count()'. Using 'subplots()' displayed a bargraph with x-axis day (month) and y-axis 'the number of messages of day (month)'.

4 . Heat_Map
- The time in the week, at which the user is most active.
- Created a new column 'range' form 'hour' column by adding a range of 1 hour to it. Ex: from 4 to 4-5, 10 to 10-11.
- Plotted a pivot_table with index = 'day_name', columns = 'range', values = 'messages'. Used 'heatmap()' function of 'Seaborn' library to display the pivot_table.



## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

