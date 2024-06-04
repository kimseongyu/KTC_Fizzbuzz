# 주사위를 굴려 결과를 반환하는 함수
def roll_dice():
  return 0

# 플레이어가 차례를 수행하는 함수
def take_turn(player_name, player_score):
  return 0

# 플레이어가 승리 조건을 충족했는지 확인하는 함수
def is_winner(player_score, winning_score):
  return 0

# 게임을 진행하는 함수
def game():
  winning_score = 100
  player_scores = {"Player 1": 0, "Player 2": 0}
  current_player = "Player 1"
  
  while True:
    print(f"\n현재 점수 - Player 1: {player_scores['Player 1']}, Player 2: {player_scores['Player 2']}")
    turn_score = take_turn(current_player, player_scores[current_player])
    player_scores[current_player] += turn_score
    if is_winner(player_scores[current_player], winning_score):
      print(f"{current_player}이(가) 승리했습니다! 최종 점수: {player_scores[current_player]}")
      break
    current_player = "Player 2" if current_player == "Player 1" else "Player 1"

def main():
  game()

if __name__ == "__main__":
  main()
