import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt
import seaborn as sns

try:

    st.sidebar.title("Whatsapp Chat Analyzer")
    time_format = st.sidebar.radio(
        "Select your mobile time format",
        ('12hr format', '24hr format'))

    uploaded_file = st.sidebar.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        # convert bytes stream into string
        data = bytes_data.decode("utf-8")
        # st.text(data)

        df = preprocessor.preprocess(data, time_format)
        # st.dataframe(df)
        # fetch unique users
        user_list = df['user'].unique().tolist()
        user_list.remove('group_notification')
        user_list.sort()
        user_list.insert(0, "Overall")

        selected_user = st.selectbox("show analysis wrt", user_list)


        if st.button("Show analysis"):
            num_messages, words, num_of_media, no_of_links = helper.fetch_stats(selected_user, df)
            st.title("Top Statistics")
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.header("Total Messages")
                st.title(num_messages)
            with col2:
                st.header("Total words")
                st.title(words)
            with col3:
                st.header("Total media")
                st.title(num_of_media)
            with col4:
                st.header("Total links")
                st.title(no_of_links)

            # timeline

            # monthly timeline
            st.title("Monthly Timelime")
            timeline = helper.monthly_timeline(selected_user, df)
            fig, ax = plt.subplots()
            ax.plot(timeline['time'], timeline['messages'], color='green')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

            # daily timeline
            st.title("Daily Timelime")
            daily_timeline = helper.daily_timeline(selected_user, df)
            fig, ax = plt.subplots()
            ax.plot(daily_timeline['only_date'], daily_timeline['messages'], color='black')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

            # activity map
            st.title("Activity map")
            col1, col2 = st.columns(2)
            with col1:
                st.header("Most Busy Day")
                busy_day = helper.week_activity_map(selected_user, df)
                fig, ax = plt.subplots()
                ax.bar(busy_day.index, busy_day.values)
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            with col2:
                st.header("Most Busy Month")
                busy_month = helper.month_activity_map(selected_user, df)
                fig, ax = plt.subplots()
                ax.bar(busy_month.index, busy_month.values, color='orange')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)

            # activity_heatmap
            st.title("weekly activity map")
            user_heatmap = helper.activity_heatmap(selected_user, df)
            fig, ax = plt.subplots()
            ax = sns.heatmap(user_heatmap)
            st.pyplot(fig)

            # finding the busiest users in the group(Group level)
            if selected_user == 'Overall':
                st.title("Busy users")
                x, new_df = helper.most_busy_users(df)
                fig, ax = plt.subplots()

                col1, col2 = st.columns(2)

                with col1:
                    ax.bar(x.index, x.values, color='red')
                    plt.xticks(rotation='vertical')
                    st.pyplot(fig)
                with col2:
                    st.dataframe(new_df)

            # wordcloud
            st.title("WordCloud")
            df_wc = helper.create_wordcloud(selected_user, df)
            fig, ax = plt.subplots()
            ax.imshow(df_wc)
            st.pyplot(fig)

            # most commmon words
            most_common_df, words = helper.most_common_words(selected_user, df)
            fig, ax = plt.subplots()
            ax.barh(most_common_df[0], most_common_df[1])
            plt.xticks(rotation='vertical')
            st.title("most common words")
            st.pyplot(fig)
            st.dataframe(most_common_df)

            # emoji analysis
            emoji_df = helper.emoji_helper(selected_user, df)
            st.title("Emoji Analysis")
            st.dataframe(emoji_df)

except ValueError:
    st.header('Dear User,')
    st.header('Select the right time format !!!')
