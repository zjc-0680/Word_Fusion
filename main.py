# Word_Fusion
import time
from wonderwords import RandomWord
from colorama import init, Fore, Style

init(autoreset = True)

def main():
    r = RandomWord()
    print(Fore.CYAN + "欢迎来到Word_Fusion 拼字游戏 ❤")
    time.sleep(0.5)
    while True:
        print("生成单词中...")
        time.sleep(1.5)
        a = r.word(include_parts_of_speech = ["nouns"])
        b = r.word(include_parts_of_speech = ["nouns"])
        print("\n" + "-" * 30)
        print("请将下面的啷个单词用下划线 _ 连接起来")
        
        print(Fore.YELLOW + f"{a} {b}")
        usr_input = input("输入: ").strip()

        time.sleep(0.5)
        ans = f"{a}_{b}"
        if usr_input == ans:
            print(Fore.GREEN + "Correct! 拼写正确")
        else:
            print(Fore.RED + f"Nope! 正确答案是 {ans}")

        print("继续挑战吗？ y/n")
        usr_input = input().strip().lower()
        if usr_input == 'n':
            print("Cya~")
            time.sleep(1)
            break

if __name__ == "__main__":
    main()

# 添加一定的间隔时间
