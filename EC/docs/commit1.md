# Commit 및 PR 가이드

## Commit 메시지 가이드

1. **기본 프로젝트 설정**
   - **커밋 메시지**: `Initialize project structure`

2. **센서 클래스 구현**
   - **커밋 메시지**: `Implement base Sensor class and Sensor1, Sensor2, Sensor3 subclasses`

3. **데이터 처리 클래스 구현**
   - **커밋 메시지**: `Implement DataProcessor class`

4. **센서 컨트롤러 클래스 구현**
   - **커밋 메시지**: `Implement SensorController class`

5. **테스트 코드 작성**
   - **커밋 메시지**: `Add unit tests for Sensor, DataProcessor, and SensorController`

## PR 가이드

1. **PR 1: 프로젝트 초기 설정**
   - **PR 제목**: `Initialize project structure`
   - **PR 설명**:
     ```markdown
     ### 변경 사항
     - 프로젝트 기본 구조를 설정하고 초기 설정 파일을 추가합니다.
     
     ### 상세 내용
     - README.md 파일 추가
     - requirements.txt 파일 추가
     - .gitignore 파일 추가
     - src, tests, docs 폴더 및 초기화 파일 생성
     
     ### 체크리스트
     - [x] 프로젝트 구조 설정
     - [x] 초기 설정 파일 추가
     ```

2. **PR 2: 센서 클래스 구현**
   - **PR 제목**: `Implement Sensor classes`
   - **PR 설명**:
     ```markdown
     ### 변경 사항
     - 기본 Sensor 클래스를 구현하고, Sensor1, Sensor2, Sensor3 하위 클래스를 추가합니다.
     
     ### 상세 내용
     - Sensor 클래스 구현
     - Sensor1, Sensor2, Sensor3 클래스 구현
     
     ### 체크리스트
     - [x] Sensor 클래스 구현
     - [x] Sensor1, Sensor2, Sensor3 클래스 구현
     - [x] 코드 리뷰
     ```

3. **PR 3: 데이터 처리 클래스 구현**
   - **PR 제목**: `Implement DataProcessor class`
   - **PR 설명**:
     ```markdown
     ### 변경 사항
     - 데이터를 처리하는 DataProcessor 클래스를 추가합니다.
     
     ### 상세 내용
     - DataProcessor 클래스 구현
     
     ### 체크리스트
     - [x] DataProcessor 클래스 구현
     - [x] 코드 리뷰
     ```

4. **PR 4: 센서 컨트롤러 클래스 구현**
   - **PR 제목**: `Implement SensorController class`
   - **PR 설명**:
     ```markdown
     ### 변경 사항
     - 센서를 제어하고 데이터를 처리하는 SensorController 클래스를 추가합니다.
     
     ### 상세 내용
     - SensorController 클래스 구현
     
     ### 체크리스트
     - [x] SensorController 클래스 구현
     - [x] 코드 리뷰
     ```

5. **PR 5: 테스트 코드 작성**
   - **PR 제목**: `Add unit tests`
   - **PR 설명**:
     ```markdown
     ### 변경 사항
     - Sensor, DataProcessor, SensorController 클래스에 대한 유닛 테스트를 추가합니다.
     
     ### 상세 내용
     - Sensor 클래스 테스트 코드 추가
     - DataProcessor 클래스 테스트 코드 추가
     - SensorController 클래스 테스트 코드 추가
     
     ### 체크리스트
     - [x] Sensor 클래스 테스트 코드 작성
     - [x] DataProcessor 클래스 테스트 코드 작성
     - [x] SensorController 클래스 테스트 코드 작성
     - [x] 모든 테스트 통과 확인
     ```

## 커밋 및 PR 예시

```bash
# Step 1: 프로젝트 초기 설정 커밋 및 PR
git add .
git commit -m "Initialize project structure"
git push origin feature/initialize-project

# Create PR on GitHub with title "Initialize project structure"

# Step 2: 센서 클래스 구현 커밋 및 PR
git add .
git commit -m "Implement base Sensor class and Sensor1, Sensor2, Sensor3 subclasses"
git push origin feature/implement-sensors

# Create PR on GitHub with title "Implement Sensor classes"

# Step 3: 데이터 처리 클래스 구현 커밋 및 PR
git add .
git commit -m "Implement DataProcessor class"
git push origin feature/implement-data-processor

# Create PR on GitHub with title "Implement DataProcessor class"

# Step 4: 센서 컨트롤러 클래스 구현 커밋 및 PR
git add .
git commit -m "Implement SensorController class"
git push origin feature/implement-sensor-controller

# Create PR on GitHub with title "Implement SensorController class"

# Step 5: 테스트 코드 작성 커밋 및 PR
git add .
git commit -m "Add unit tests for Sensor, DataProcessor, and SensorController"
git push origin feature/add-unit-tests

# Create PR on GitHub with title "Add unit tests"
```

