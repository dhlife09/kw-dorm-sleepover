# kw-dorm-sleepover

광운대학교 기숙사(한국사학진흥재단 행복기숙사 시스템) 외박신청 프로그램 입니다.

코드를 일부 수정할 경우, 한국사학진흥재단 행복기숙사 시스템을 사용하는 타 기숙사에서도 사용 가능할 것으로 추정됩니다.

## 사용방법
```py
sleepover(yyyy_mm_dd, hakbun, birth, de_code, locgbn, reason)
```

|파라미터|이름|설명|입력 형식(예)|
|-------|----|----|--------|
|`yyyy_mm_dd`|생년월일|yyyy_mm_dd 형식의 생년월일|2024_03_24|
|`hakbun`|학번|광운대학교 학번|2024201234|
|`birth`|생년월일|yymmdd 형식의 생년월일|240324|
|`de_code`|고유코드|(방 구분 관련 코드로 추정) 기숙사 홈페이지에서 직접 로그인 후 확인이 필요합니다.|2024012345|
|`locgbn`|기숙사 구분|광운대학교 기숙사의 경우 `KW`이 기본으로 지정되어 있습니다.|KW|
|`reason`|외박신청 사유|외박신청하는 사유를 입력합니다.|본가 방문|

## 응용


|![sample1](https://github.com/dhlife09/kw-dorm-sleepover/assets/22024308/6cbb0901-422b-4f90-8762-043f55b44684)|![sample2](https://github.com/dhlife09/kw-dorm-sleepover/assets/22024308/0c46d0eb-af81-4641-91fa-c9bb47a96742)|
|-|-|
|매일 오후 11시 20분마다 자동으로 단축어(스크립트) 실행|현재 위치를 확인해 우편번호가 `01890`(기숙사)이 아닌 경우 `외박신청을 하시겠습니까?` 알림 띄우기|


## 유의사항

- 본 코드는 개인 사용 목적으로 제작되었으며, **사용에 대한 책임은 사용자 본인에게 있습니다.**
- 본 repository는 MIT 라이선스를 따릅니다.