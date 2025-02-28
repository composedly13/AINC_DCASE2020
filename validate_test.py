import pickle

# Pickle 파일 경로
pickle_path = 'D:/DCASE2020/DCASE-2020-Task1A-Code/pytorch/main/train/logmel_86frames_40melbins/TAU-urban-acoustic-scenes-2020-mobile-development/holdout_fold=1/Gamm_Cnn/validate_statistics.pickle'

# Pickle 파일 읽기
with open(pickle_path, 'rb') as f:
    validate_stats = pickle.load(f)

# 통계 출력
print(validate_stats)
