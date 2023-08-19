import csv
import random

output_file = 'random_scores.csv'

# 만들고자 하는 평가 점수 개수
num_scores = 1000

# 최소 점수와 최대 점수 범위
min_score = 60
max_score = 100

# 랜덤한 평가 점수 과정
random_scores = [[random.randint(min_score, max_score)] for _ in range(num_scores)]

# CSV 파일에 저장
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Score'])
    for score in random_scores:
        writer.writerow(score)

from sklearn.preprocessing import StandardScaler