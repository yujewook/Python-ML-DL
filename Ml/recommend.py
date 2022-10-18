# 협업 필터링
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")
ratings_movie = pd.merge(ratings, movies, on="movieId")  # ratings를 기준으로 movies를 join
# print(ratings_movie.head())
ratings_matrix = ratings_movie.pivot_table("rating", "userId", "title")
# print(ratings_matrix.head())
ratings_matrix.fillna(0, inplace=True)
# print(ratings_matrix.shape)        # (610, 9719)
ratings_matrixT = ratings_matrix.T  # 사용자 아이디 <-> 영화 아이디

from sklearn.metrics.pairwise import cosine_similarity      # 코사인 유사도
cs = cosine_similarity(ratings_matrixT, ratings_matrixT)    # 아이템 기반의 유사도 측정 시 코사인 유사도가 주로 쓰인다.
# print(type(cs)) # numpy.array 타입
similarity = pd.DataFrame(cs, index=ratings_matrixT.index, columns=ratings_matrixT.index)
# print(similarity.head(1))

items = similarity[movies['title'][300]].sort_values(ascending=False)[:5]
# print(items)    # 평점이 유사한 영화들 추천

def predict_rating(ratings_array, item_similarity):
    sum = ratings_array @ item_similarity   # 행렬곱
    sum_abs = np.array([np.abs(item_similarity).sum(axis=1)])
    return sum / sum_abs

rating_pred = predict_rating(ratings_matrix.values, similarity.values)
rating_df = pd.DataFrame(data=rating_pred, index=ratings_matrix.index, columns=ratings_matrix.columns)
# print(rating_df.head())

# print(ratings_matrix.columns)

# 안 본 영화 리스트
def no_watch(ratings_matrix, user):
    user_rating = ratings_matrix.loc[user, :]   # user 행을 뽑고 열은 전부 가져와라
    no_watching = user_rating[user_rating==0].index.tolist()
    movie_list = ratings_matrix.columns.tolist()
    return [movie for movie in movie_list if movie in no_watching]

def recommend(rating_pred, userId, no_list, top=10):
    return rating_pred.loc[userId, no_list].sort_values(ascending=False)[:top]

userId = 15
no_watching = no_watch(ratings_matrix, userId)
recommend_movie = recommend(rating_df, userId, no_watching, 10)
recommend_df = pd.DataFrame(recommend_movie.values, index=recommend_movie.index, columns=["predict_score"])
print(recommend_df)
