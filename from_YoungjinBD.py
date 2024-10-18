# https://raw.githubusercontent.com/YoungjinBD/dataset/main에 저장된 모든 csv 파일을 불러오기
# 빅데이터분석기사 실기시험 연습용도

import pandas as pd

# 저장하려는 파일 입력
files = ["airquality",
        "Bank_Personal_Loan_Modeling",
        "HR-Employee-Attrition",
        "Parkinsons",
        "data_6_1_1",
        "data_6_1_2",
        "data_6_1_3",
        "data_6_3_2",
        "trash_bag",
        "BMI",
        "students",
        "used_car_X_train",
        "used_car_X_test",
        "used_car_y_train",
        "facebook",
        "netflix",
        "CS_Seg_X_train",
        "CS_Seg_X_test",
        "CS_Seg_y_train"]  

# 예외 처리 테스트: 의미없는 파일 추가
test_files = ["ㅇㅅㅇ", "dtd"]
for test_file in test_files:
    files.append(test_file)

# 성공 및 실패한 파일 수와 목록 저장을 위한 변수 초기화
success_count = 0
failure_count = 0
failed_files = []

for file in files:
    link = f"https://raw.githubusercontent.com/YoungjinBD/dataset/main/{file}.csv"
    
    try:
        # 파일 로드: UTF-8 시도 후 실패 시 cp949로 재시도
        try:
            df = pd.read_csv(link)
        except UnicodeDecodeError:
            print(f"{file}.csv 파일에서 UTF-8 인코딩 오류 발생, cp949 인코딩으로 재시도합니다.")
            df = pd.read_csv(link, encoding="cp949")

        # 파일 저장
        df.to_csv(f"csv_files\{file}.csv", index=False)
        print(f"{file}.csv 파일 저장이 완료되었습니다.")
        success_count += 1

    except Exception as e:
        # 모든 오류 처리
        print(f"{file}.csv 파일을 처리하는 데 실패했습니다. 오류: {e}")
        failure_count += 1
        failed_files.append(file)

# 결과 출력
print(f"\n저장에 성공한 파일 수: {success_count}")
print(f"저장에 실패한 파일 수: {failure_count}")

if failed_files:
    print(f"저장에 실패한 파일 목록: {', '.join(failed_files)}") # '을 "로 바꾸지 말것
else:
    print("모든 파일이 성공적으로 저장되었습니다.")
