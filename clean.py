import os
import re

def remove_special_characters(text):
    # 알파벳, 숫자, 한글, 공백만 남기고 나머지 특수 문자는 제거
    cleaned_text = re.sub(r'[^A-Za-z0-9가-힣\s]', '', text)
    return cleaned_text

def clean_text_file(input_file, output_file):
    # 파일 존재 여부 확인
    if not os.path.exists(input_file):
        print(f"파일 '{input_file}'이(가) 현재 디렉토리에 존재하지 않습니다.")
        print("현재 디렉토리:", os.getcwd())
        return

    # 원본 파일 읽기
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # 특수 문자 제거
    cleaned_text = remove_special_characters(text)
    
    # 정제된 텍스트를 새 파일에 저장
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(cleaned_text)

    print(f"특수 문자가 제거된 파일이 '{output_file}'에 저장되었습니다.")

# 스크립트 위치를 기준으로 작업 디렉토리 설정
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# 현재 디렉토리 출력
print("현재 작업 디렉토리:", os.getcwd())

# 상대 경로로 입력 파일과 출력 파일 설정
input_file = 'The Wonderful Wizard of Oz.txt'  # 원본 파일 이름
output_file = 'The Wonderful Wizard of Oz_Cleaned.txt'  # 특수 문자가 제거된 파일 이름

# 특수 문자 제거 후 새 파일에 저장
clean_text_file(input_file, output_file)
