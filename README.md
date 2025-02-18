# Linear Regression Price Prediction

Author: Ayan Sengupta

Email: <ayan.sengupta@gmail.com>

Data Source: <https://insideairbnb.com/get-the-data/>
Only looking at Asheville NC

A linear regression model to predict the price of Airbnb listings in Asheville, NC.

Structure:

1) Data directory contains all data sets being used (initial and processed)
2) src directory contains all steps from cleaning to training and testibng the model. Each step is a python script with the name of the step being performed
3) main.py is the intended entry point to the project but each individual step (script) can also be executed individually for debugging purposes

Instructions on running the model locally :

1) make sure you have python3 installed
2) `cd /path/to/linearregression_priceprediction`
3) install dependencies --run  `pip install -r requirements.txt` from the project root directory
4) run main.py - `python main.py` or if using python3 `python3 main.py`

Instruction on running inside docker container (buildig image from scratch):

1) make sure to have docker desktop installed
2) navigate to project directory 
3) run `docker build -t linearregression_priceprediction .` to build image
4) run the container - `docker run -d -p 2222:22 --name linearregression_container linearregression_priceprediction`
