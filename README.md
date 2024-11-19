# Data Cleaning Project: Airbnb Listings Dataset

This project focuses on cleaning and preparing the **Airbnb Listings Dataset**. The dataset contains information about Airbnb listings, such as prices, locations, property types, and more. The goal is to clean the data by handling missing values, removing duplicates, detecting outliers, and preparing it for analysis or modeling.

---

## **Dataset**
The dataset is publicly available on the [Inside Airbnb: Get the Data](https://insideairbnb.com/get-the-data/) page. For this project, we used the **Lisbon Airbnb Listings Dataset**, which includes detailed information about listings in Lisbon.

---

## **Project Features**
1. **Data Loading**:
   - The dataset is loaded into a Pandas DataFrame for exploration and cleaning.

2. **Data Cleaning**:
   - Handling missing values:
     - Numerical values are filled with the median.
     - Categorical values are filled with the mode.
   - Removing duplicates to ensure data quality.
   - Identifying and removing outliers using the IQR method.

3. **Feature Selection**:
   - Irrelevant or low-variability columns are removed.

4. **Exporting Clean Data**:
   - The cleaned dataset is saved as `listings_cleaned.csv`.

---

## **Visualizations**
- **Bar Plot**: Displays missing values by column.
- **Box Plot**: Identifies outliers for numerical variables.

---

## **Setup and Usage**
### **Requirements**
- Python 3.8 or later
- Libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`

### **Installation**
1. Clone this repository:
   ```bash
   git clone https://github.com/tjfmleite/airbnb-data-cleaning.git
   cd airbnb-data-cleaning
