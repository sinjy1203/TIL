## 배운점
- telegram의 구버전과 신버전이 바껴서 에러발생
=> pip install --upgrade python-telegram-bot==13.14
- apscheduler 최신으로 업그레이드 필요
=> pip install --upgrade apscheduler
- ec2 ubuntu에 백그라운드로 selenium을 돌리기 위해선
  > chrome은 안됨, firefox 사용할것
  > headless option 넣기
  > 예외 처리할것 => try문에 전체 크롤링 코드 넣어야함
  > 마지막에 driver.quit 처리하기
- frame 변환에서 변환 후에 click하면 변환상태 유지됨 (다시 원상태로 돌리는게 나음)
- 처음에 get 쓸때 날짜 주의할것 (예전 날짜 계속쓰면 element를 못찾음)


## xpath를 이용한 노드 찾기
### '/html/body/div/div[3]/ul/li[descendant::*[@class="imax"]]'
- li[조건] = 해당 조건을 만족하는 li 노드들
- *[@class="imax"] = 어떤 노드건 class속성이 imax인 노드들 (@가 속성을 뜻함)
- descendant::검색노드[조건] = 자식노드들 중에 조건을 만족하는 검색노드들
