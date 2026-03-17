# Amazon Best Sellers Data Analysis 📚

This project analyzes a dataset of Amazon's Top 50 Bestselling Books from 2009 to 2019. Using Python and the **pandas** library, the script cleans the data, explores author popularity, and compares ratings across genres.

This project was built following the [Codédex](https://www.codedex.io/) "Analyze Best Selling Amazon Books with Pandas" tutorial. I have also added additional analysis of my own.

## ✨ Features
- **Data Cleaning:** Removes duplicates, renames columns for clarity, and ensures correct data types.
- **Author Analysis:** Identifies the authors with the most best-selling titles.
- **Genre Insights:** Calculates and compares the average user ratings for Fiction vs. Non-Fiction.
- **Data Export:** Saves the processed results into new CSV files for easy sharing.

## 🛠️ Technologies Used
- **Python 3.x**
- **Pandas Library**: For data manipulation and analysis.

## 🚀 How to Run
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
   cd YOUR_REPO_NAME

2. **Install dependencies:**
   ```bash
   pip install pandas

3. **Prepare the data:**
   Ensure the bestsellers.csv file is in the same directory as main.py.

4. **Run the script:**
   ```bash
   python main.py

## 📊 Results

After running the script, two files will be generated:

- **top_authors.csv:** A list of the top 10 most frequent authors.
- **avg_rating_by_genre.csv:** The average user ratings categorized by genre.
- **most_popular_book:** I performed an additional analysis to find the "crowd favorite" for every rating level (from 4.9 down to 3.3).
  
- *Note: Interestingly, the most reviewed book overall (87k+ reviews) has a 4.8 rating, proving that as a book's popularity explodes, maintaining a perfect 4.9 becomes much harder.*
  
