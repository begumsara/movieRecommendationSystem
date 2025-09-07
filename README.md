# 🎬 Movie Recommendation System  

## 📌 Project Overview  
This project recommends movies to users based on their selection.  
It uses **TF-IDF Vectorization** and **Cosine Similarity** to calculate similarity between movies, and also provides an **interactive web app** built with **Streamlit**.  

- 📂 **movieRecommendApp.py** → Streamlit web app  
- 📂 **movieRecommend.ipynb** → Jupyter Notebook (model explanation + experiments)  
- 📂 **movies.csv** → Dataset (scraped from IMDB)  
- 📂 **poster.jpeg** → Poster image displayed in the web app  

---

## 🛠️ Tech Stack  
- Python 🐍  
- Streamlit  
- Pandas, NumPy  
- scikit-learn  
- difflib  

---

## 📊 Data Collection  
The dataset was collected via **web scraping from IMDB**.  
👉 Detailed scraping code can be found here: [IMDB Movies Scraper Repository](https://github.com/begumsara/imdbMovies)  

The dataset contains thousands of movies with metadata including:  
- 🎭 Genres  
- 📝 Keywords  
- 🎬 Cast & Director  
- 🎯 Tagline & Overview  

---

## 🚀 How to Run  

### 1️⃣ Run the Notebook (Exploration & Backend)  
```bash
jupyter notebook movieRecommend.ipynb
```

### 2️⃣ Run the Streamlit App  
```bash
streamlit run movieRecommendApp.py
```

Then, open the link shown in the terminal (usually `http://localhost:8501`) in your browser.  

---

## 🌟 Features  
✔️ Recommends similar movies based on user input  
✔️ Handles misspellings (thanks to `difflib`)  
✔️ Lets the user choose **how many movies** to recommend  
✔️ Interactive UI with Streamlit  

---

## 🖼️ Screenshots  

### Web App Poster  
![Poster](poster.jpeg)  

### Example Recommendation (Jupyter Notebook)  
```
Input: "Iron Man"  
Output:  
1. Iron Man 2  
2. Iron Man 3  
3. The Avengers  
4. Captain America: Civil War  
5. Avengers: Age of Ultron  
```

 

---

## 📜 License  
This project is licensed under the MIT License.  
Data was scraped from IMDB and is used **only for educational and research purposes**.  
