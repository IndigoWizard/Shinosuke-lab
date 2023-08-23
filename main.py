import os
import sys

# get the path of your current script (main.py in here)
script_path = os.path.dirname(os.path.abspath(__file__))

# add 'streamlit_app' folder to sys.path
app_folder = os.path.join(script_path, 'streamlit_app')
sys.path.append(app_folder)

# import and run the Streamlit app from app.py that lives in streamlit_app folder
import app

if __name__ == '__main__':
    app.run()  # run the Streamlit app

# you can call it run or main or whatever in the app.py script, just make sure to call the right funciton from there to here
