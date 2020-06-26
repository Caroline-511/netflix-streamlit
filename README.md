# netflix-streamlit
Streamlit application for Netflix show rating analysis

Streamlit is an open source app framework for Machine Learning and Data Science teams. It helps us to create apps using simple python scripts. 
It supports hot-reloading so that your app can update live as soon as you edit and save the file.
 
To install streamlit, type the following in your command prompt
 $pip install streamlit
 
Datasets used for this project can also be found in data.world

This project is mainly based on categorizing Netflix shows based on given conditions,
-> Option to display random shows based on rating category ( PG-13, R, TV-MA ...etc)
-> Graph (Histogram) for number of shows released in a particular year.
-> Top rated Netflix shows (Top 20 shows)
-> Top shows based on release year
-> Top shows based on rating category ( PG-13, R, TV-MA ...etc)

To run the application, open command prompt in the directory in which your project is saved
 $streamlit run project_name.py
In the next few seconds the sample app will open in a new tab in your default browser.

Before running this app make sure you have pandas, numpy, streamlit and plotly.express libraries pre-installed. 
If not installed you can install by typing the following in your command prompt 
 $pip install pandas 
 $pip install numpy
 $pip install plotly
