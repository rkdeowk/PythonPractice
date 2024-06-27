# Sensor Project

## 프로젝트 설명
이 프로젝트는 다양한 센서로부터 데이터를 수집하고 처리하는 소프트웨어를 구현합니다. TDD, Clean Code, Refactoring 기법을 적용하여 코드를 작성했습니다.

## 설치 방법
```bash
pip install -r requirements.txt
```

## 사용 방법
```bash
python src/controller/sensor_controller.py
```

## 테스트 방법
```bash
python -m unittest discover tests
```

## 폴더 구조
```bash
sensor-project/
├── README.md
├── requirements.txt
├── src/
│   ├── sensors/
│   │   ├── sensor.py
│   │   ├── sensor1.py
│   │   ├── sensor2.py
│   │   ├── sensor3.py
│   ├── data_processor/
│   │   ├── data_processor.py
│   ├── controller/
│   │   ├── sensor_controller.py
├── tests/
│   ├── test_sensor.py
│   ├── test_data_processor.py
│   ├── test_sensor_controller.py
├── docs/
└── .gitignore
```


## 각 폴더와 파일 설명
- **README.md**: 프로젝트에 대한 설명과 사용 방법, 설치 방법 등을 기술합니다.
- **requirements.txt**: 프로젝트에서 필요한 Python 패키지 목록을 기술합니다.
- **src/**: 실제 코드가 위치하는 디렉토리입니다.
  - **sensors/**: 센서 관련 코드가 위치하는 디렉토리입니다.
    - **sensor.py**: 기본 `Sensor` 클래스 정의.
    - **sensor1.py**, **sensor2.py**, **sensor3.py**: 각각의 센서 클래스 정의.
  - **data_processor/**: 데이터 처리 관련 코드가 위치하는 디렉토리입니다.
    - **data_processor.py**: `DataProcessor` 클래스 정의.
  - **controller/**: 센서 제어 관련 코드가 위치하는 디렉토리입니다.
    - **sensor_controller.py**: `SensorController` 클래스 정의.
- **tests/**: 테스트 코드가 위치하는 디렉토리입니다.
  - **test_sensor.py**: 센서 클래스 테스트 코드.
  - **test_data_processor.py**: 데이터 처리 클래스 테스트 코드.
  - **test_sensor_controller.py**: 센서 컨트롤러 클래스 테스트 코드.
- **docs/**: CRA 보고서 등의 문서가 위치하는 디렉토리입니다.
  - **1st_report.md**: 1차 보고서.
  - **2nd_report.md**: 2차 보고서.
- **.gitignore**: Git에서 추적하지 않을 파일 및 디렉토리를 기술합니다.
