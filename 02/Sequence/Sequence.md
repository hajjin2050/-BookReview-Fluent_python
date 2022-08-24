-  Python 은 시퀀스를 단일하게 처리하는 ABC 언어의 특징을 물려받았다.
    - 문자열, 리스트, 바이트 시퀀스, 배열, XML 요소, 데이터베이스 결과에는 모두 반복, 슬라이싱, 정렬, 연결 등 공통된 연산을 적용 할 수 있다.
    - 파이썬에서 제공하는 다양한 시퀀스를 이해하면 코드를 새로 구현할 필요 x

## 2.1 ##. 내장 시퀀스 개요


파이썬 표준 라이브러리르는 C로 구현된 다음과 같은 시퀀스형을 제공
#### 컨테이너 시퀀스
- 서로 다른 자료형의 항목들을 담을 수 있는 list, tuple, collections,deque 형

#### 균일 시퀀스
- 단 하나의 자료형만을 담을 수 있는 str, bytes, bytearray, memoryview, array, array 형

###  가변 시퀀스
- list, bytearray, array, array, collections, deque, memoryview 형

### 불변 시퀀스
- tuple, str, bytes 형



## 2.2 지능형 리스트와 제너레이터 표현식

### 1 지능형 리스트와 가독성 
----
- 지능형 리스트는 더 이상 메모리를 누수하지 않는다.