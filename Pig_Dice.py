# 주사위를 굴려 결과를 반환하는 함수
def roll_dice():
  return 0

# 플레이어가 차례를 수행하는 함수
def take_turn(player_name, current_score):
  dice = roll_dice()
  choice = input("주사위를 굴리려면 'r', 턴을 넘기려면 'x'를 입력하세요: ")

  if choice == 'r':
    dice = roll_dice()
    print(f"{player_name}이/가 주사위를 굴렸습니다. 나온 숫자: {dice}")
    
    if dice == 1:
      print("턴이 종료되었습니다. 턴 동안 얻은 점수는 0점입니다.")
      return 0
    else:
      print(f"{player_name}가 턴 동안 {current_score} 점수를 얻었습니다.")
      return current_score + dice
  elif choice == 'x':
    return -1

# 플레이어가 승리 조건을 충족했는지 확인하는 함수
def is_winner(player_score, winning_score):
  return 0

# 게임을 진행하는 함수
def game():
  return 0

def main():
  game():

if __name__ == "__main__":
  main()
