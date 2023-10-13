import random

def get_user_choice():
    user_choice = input("じゃんけんをします。[1] グー, [2] チョキ, [3] パー: ")
    if user_choice in ['1', '2', '3']:
        return int(user_choice)
    else:
        print("無効な選択です。[1], [2], [3]の中から選んでください。")
        return get_user_choice()

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "引き分け"
    elif (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 3) or (user_choice == 3 and computer_choice == 1):
        return "ユーザーの勝利"
    else:
        return "コンピューターの勝利"

def main():
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"ユーザー: {user_choice}, コンピューター: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("もう一度プレイしますか？(y/n): ")
        if play_again.lower() != 'y':
            break

if __name__ == "__main__":
    main()