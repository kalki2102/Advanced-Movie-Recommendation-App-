Advanced Movie Recommendation App Backend Description

This advanced movie recommendation app leverages the power of Streamlit, HTML, and JavaScript to deliver a seamless and interactive user experience. Here's a comprehensive breakdown of its backend features:

Firstly, I created a Jupyter Notebook file where I performed the backend operations. I executed data science operations such as data cleaning, data preprocessing, vectorization, and cosine similarity calculations to develop a robust recommendation system.

Next, I created a recommendation function that enables users to input a movie name and retrieves its corresponding ID. This ID is then used to fetch the top 5 similar movies from the sorted similarity dataset, which was generated using cosine similarity.

To ensure efficient data storage and retrieval, I created pickle files for the data (data.pkl) and similarity indices (simi.pkl).

In the frontend, I utilized Streamlit to design a user-friendly search box where users can select a movie. The recommended movies are then displayed, and I made the movie icons clickable and on clicking icon a new tab will open which has information of movie its cast,overview i did using library urlencode on the new tab in url we will send the movie name and using that url java script will fetch the name convert it into string and then using the TMDB api we will easily fetch the details of the movie 

While the app is functional, I plan to make some enhancements, such as styling the app and integrating movie reviews to further improve the user experience
then 
