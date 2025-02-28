import h5py

with h5py.File("D:\\DCASE2020\\workspace\\features\\logmel_86frames_40melbins\\TAU-urban-acoustic-scenes-2020-mobile-development.h5", 'r') as f:
    print(list(f.keys()))  # HDF5 파일의 최상위 키 출력
    print(f['audio_name'][:])  # 'audio_name' 데이터셋의 내용 출력
    print(f['feature'].shape)  # 'feature' 데이터셋의 형태 출력
