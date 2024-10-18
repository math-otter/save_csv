# 캐글에서 엑셀 데이터를 가져와서 csv 파일로 저장

import kagglehub
import pandas as pd
import os

# 최신 버전 다운로드
path = kagglehub.dataset_download("yasserh/customer-segmentation-dataset")
file_name = "Online Retail.xlsx"

# csv 파일로 저장
full_path = os.path.join(path, file_name)
df = pd.read_excel(full_path)
save_as = "csv_files\customer segmentation dataset.csv"
df.to_csv(save_as, index=False)
print(f"저장이 완료되었습니다: {save_as}")
