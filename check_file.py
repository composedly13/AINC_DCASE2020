import os
import pandas as pd

file_path = r'D:\DCASE2020\data\dev\evaluation_setup\fold1_train.csv'

try:
    df = pd.read_csv(file_path, sep=',')  # 쉼표로 구분된 경우
    print("CSV 파일 읽기 성공!")
    print(df.head())  # 첫 5줄 출력
except Exception as e:
    print(f"CSV 파일 읽기 실패: {e}")

file_path = r'D:\DCASE2020\data\dev\evaluation_setup\fold1_train.csv'
print("File exists:", os.path.exists(file_path))
