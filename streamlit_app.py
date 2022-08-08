import streamlit

# streamlit.title('Learning some new stuff!')

# streamlit.header('GITHUB')
# streamlit.text('Created account for the first time ever')
# streamlit.text('Needed it for Snowflake\'s DABW Badge')
# streamlit.text('It\'s really confusing!')
# streamlit.text('Will have to alot some time to learn this later since I need it down the line anyway')

# streamlit.header('Streamlit.io')
# streamlit.text('Created this for for the badge as well!')
# streamlit.text('Don\'t even know what this was until I read through some high level info')
# streamlit.text('Was never in to App development. But I guess I\'ll take it up soon')

streamlit.title('My Mom\'s New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#New Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
