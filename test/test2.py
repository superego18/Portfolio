# 축구 팀 이름과 초기 전적을 저장할 딕셔너리
teams = {"A": [0, 0, 0], "B": [0, 0, 0], "C": [0, 0, 0], "D": [0, 0, 0]}

# 축구 경기 결과를 입력받음
while True:
  # 축구 경기 결과를 입력 받음
  result = input("Enter game result (A B): ")

  # 입력이 종료되면 반복문을 종료함
  if result == "":
    break

  # 입력된 축구 경기 결과를 공백으로 분리하여 각 팀의 이름을 추출
  team1, team2 = result.split()

  # 경기 결과를 입력 받음
  score1 = int(input("Enter score for team " + team1 + ": "))
  score2 = int(input("Enter score for team " + team2 + ": "))

  # 각 팀의 전적을 갱신
  if score1 > score2:
    # team1 승리
    teams[team1][0] += 1  # 승수 증가
    teams[team2][2] += 1  # 패수 증가
  elif score1 < score2:
    # team2 승리
    teams[team1][2] += 1  # 패수
