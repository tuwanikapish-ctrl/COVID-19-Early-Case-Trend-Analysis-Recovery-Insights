# Analytics Project Infectious

This project analyzes COVID-19 patient data from Korea, focusing on infection reasons, recovery times, and regional distributions. The analysis is performed using Python, with results visualized through various plots and a regression model.

## Project Structure

```
Analytics Project Infectious/
│
├── code.py           # Main analysis script
├── patient.csv       # COVID-19 patient dataset
├── R2_Result.txt     # Output: R² score for recovery time regression
├── structure.txt     # Example project structure (possibly for reference)
└── __pycache__/      # Python cache files
```

## Data

- **patient.csv**: Contains anonymized patient-level data, including demographics, infection details, and outcome dates.

## Analysis Overview

The main analysis is performed in [`code.py`](Analytics%20Project%20Infectious/code.py):

1. **Data Preprocessing**  
   - Loads and cleans the dataset.
   - Converts date columns to datetime.
   - Calculates patient age and recovery days.

2. **Exploratory Data Analysis**  
   - Visualizes distributions of sex, age, infection reasons, and recovery days.
   - Shows the top 10 regions by case count.

3. **Regression Analysis**  
   - Builds a linear regression model to predict recovery days based on age, contact number, and infection order.
   - Outputs the R² score to `R2_Result.txt`.

4. **Visualizations**  
   - Saves plots as PNG files for infection reasons, recovery days, and region distributions.

## Results

- The regression model's R² score is saved in [`R2_Result.txt`](Analytics%20Project%20Infectious/R2_Result.txt).
- Plots are saved as PNG files in the project directory.

## Requirements

- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

Install dependencies with:

```sh
pip install pandas numpy matplotlib seaborn scikit-learn
```

## Usage

1. Place `patient.csv` in the `Analytics Project Infectious` directory.
2. Run the analysis:

```sh
python code.py
```

3. View the generated plots and the R² score in the output files.

---

*This project is for educational and analytical purposes, using publicly available COVID-19 data.*