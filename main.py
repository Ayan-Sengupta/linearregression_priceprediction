import os
import sys
import logging
from datetime import datetime

# Add src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('execution.log'),
        logging.StreamHandler()
    ]
)

def main():
    try:
        # Record start time
        start_time = datetime.now()
        logging.info("Starting Airbnb Price Prediction Pipeline")

        # Import and run scripts in order
        logging.info("1. Running data cleaning...")
        import data_clean
        
        logging.info("2. Running descriptive statistics...")
        import descriptive_stats
        
        logging.info("3. Running data exploration...")
        import data_explore
        
        logging.info("4. Running model training...")
        import model_train

        # Record end time and calculate duration
        end_time = datetime.now()
        duration = end_time - start_time
        logging.info(f"Pipeline completed successfully in {duration}")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    main()