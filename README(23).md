# Real Estate Analysis and Price Prediction in Kazakhstan

## Project Overview

This project is focused on analyzing real estate listings in Kazakhstan. The main goal is to collect housing data, clean it, explore important patterns, build machine learning models for price prediction, and present the results in an interactive Streamlit dashboard.

The project shows the full data workflow: from raw scraped data to cleaned data, exploratory data analysis, machine learning prediction, and dashboard visualization.

## Main Features

- Web scraping of apartment listings from Krisha.kz
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering for real estate data
- Machine learning models for apartment price prediction
- Interactive Streamlit dashboard
- Visual analysis of prices, districts, area, floors, and other housing features

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Scikit-learn
- Streamlit
- Requests / BeautifulSoup
- Jupyter Notebook

## Project Structure

```text
Project_krisha.kz/
│
├── app.py                  # Streamlit dashboard
├── krisha.ipynb            # Main notebook with scraping, cleaning, EDA and ML
├── cleaned_data.csv        # Cleaned dataset
├── cleaned_data.json       # Cleaned dataset in JSON format
├── krisha_raw_data.csv     # Raw scraped data
├── krisha_raw_data.json    # Raw scraped data in JSON format
├── README.md               # Project documentation
└── requirements.txt        # Project dependencies
```

## Machine Learning Part

In this project, machine learning models were used to predict apartment prices based on available real estate features.

The prediction pipeline includes:

1. Preparing the cleaned dataset
2. Selecting useful features
3. Encoding categorical columns
4. Splitting data into training and testing sets
5. Training machine learning models
6. Evaluating model performance
7. Using the trained model for price prediction

Possible features used for prediction:

- Apartment area
- Number of rooms
- District or location
- Floor
- Total floors
- Price per square meter
- Other cleaned and engineered features

The ML part helps estimate apartment prices and understand which factors have the strongest influence on housing prices.

## Streamlit Dashboard

The project includes an interactive Streamlit dashboard in `app.py`.

The dashboard allows users to:

- Explore the cleaned dataset
- View charts and statistics
- Analyze apartment prices by different features
- Filter data interactively
- Use the ML prediction part to estimate apartment price

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

For Windows PowerShell:

```bash
.venv\Scripts\activate
```

For macOS / Linux:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not created yet, it can be generated with:

```bash
pip freeze > requirements.txt
```

### 5. Run the Jupyter Notebook

```bash
jupyter notebook krisha.ipynb
```

### 6. Run the Streamlit dashboard

```bash
streamlit run app.py
```

After running this command, Streamlit will open the dashboard in the browser.

## Dataset

The project uses real estate listing data collected from Krisha.kz. The raw data was saved and then cleaned for further analysis and machine learning.

Main dataset files:

- `krisha_raw_data.csv` — original scraped dataset
- `cleaned_data.csv` — cleaned dataset used for analysis and dashboard

## Key Insights

During the analysis, several important real estate patterns can be explored:

- Apartment price depends strongly on location
- Area has a major effect on total price
- Price per square meter can vary significantly between districts
- Outliers can affect model quality and visualizations
- Machine learning models can help estimate housing prices from apartment features

## Future Improvements

Possible improvements for this project:

- Add more cities and regions
- Improve the ML model quality
- Add more advanced feature engineering
- Deploy the Streamlit dashboard online
- Add model saving and loading with `.pkl`
- Add more interactive filters to the dashboard

## Author

This project was created as a data analysis and machine learning project for real estate price analysis in Kazakhstan.
