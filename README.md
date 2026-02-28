🎬 Movie Recommender System (TMDB Dataset)
A production-structured Content-Based Movie Recommendation Engine built using the TMDB dataset.
The system recommends semantically similar movies using NLP-based feature engineering and Cosine Similarity.
This project demonstrates applied machine learning, feature engineering, and scalable similarity computation.
🚀 Project Summary
Designed and implemented a content-based recommendation system that:
Processes and transforms structured + unstructured movie metadata
Builds high-dimensional vector representations
Computes similarity using cosine distance
Returns top-N relevant recommendations in real time
The project focuses on clean architecture, reproducibility, and scalable design principles.
🧠 Problem Statement
Users often struggle to discover movies aligned with their preferences.
This system solves the discovery problem by analyzing movie content rather than relying on user ratings.
Unlike collaborative filtering systems, this approach:
Works for new users (cold-start friendly)
Does not require historical interaction data
Is fully explainable (based on movie metadata)
🏗️ System Architecture
1️⃣ Data Processing Layer
Merged TMDB movies and credits datasets
Cleaned and normalized JSON-based metadata fields
Handled missing values and duplicates
2️⃣ Feature Engineering
Constructed a unified feature representation by combining:
Genres
Keywords
Top-billed cast
Director
Overview
Applied:
Tokenization
Lowercasing
Stemming (optional)
Stopword filtering
3️⃣ Vectorization Layer
Converted textual features into numerical vectors using CountVectorizer
Generated sparse matrix representation for scalability
4️⃣ Similarity Engine
Computed pairwise cosine similarity
Stored precomputed similarity matrix for fast inference
Achieved O(1) recommendation lookup after preprocessing
📊 Core Algorithm
Each movie is represented as a vector in high-dimensional feature space.
Cosine similarity:
similarity(A, B) = (A · B) / (||A|| ||B||)
Higher similarity → More semantically related movies.
🛠️ Tech Stack
Python
Pandas – Data processing
NumPy – Numerical computation
Scikit-learn – Vectorization & similarity modeling
NLTK – Text preprocessing
TMDB 5000 Dataset
📈 Performance & Design Decisions
Precomputed similarity matrix for fast runtime recommendations
Reduced dimensional noise by limiting feature vocabulary
Selected top-k cast members to reduce overfitting
Memory-efficient sparse matrix storage
📂 Project Structure
movie-recommender-system-tmdb-dataset/
│
├── data/
│   ├── tmdb_5000_movies.csv
│   ├── tmdb_5000_credits.csv
│
├── src/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── model.py
│   ├── recommender.py
│
├── artifacts/
│   ├── movies.pkl
│   ├── similarity.pkl
│
├── app.py (optional deployment)
└── README.md
💡 Example Usage
recommend("Inception")
Output:
1. The Dark Knight Rises
2. Interstellar
3. The Prestige
4. Shutter Island
5. Memento
🔮 Scalability Considerations
Can be extended to use TF-IDF for improved weighting
Can integrate FastAPI/Flask for API deployment
Can store similarity matrix in Redis for production systems
Can evolve into hybrid recommender (content + collaborative)
🎯 Skills Demonstrated
End-to-end ML pipeline design
NLP feature engineering
Vector space modeling
Similarity metrics & recommendation systems
Code modularization & project structuring
Performance optimization for inference systems
📌 Future Enhancements
Hybrid recommendation system
Real-time API deployment
TMDB poster integration via API
User-personalized ranking layer
📄 License
MIT License