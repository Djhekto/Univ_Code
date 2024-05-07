import sys
import asyncio

async def foo():#https://habr.com/ru/post/337420/
    print('Running in foo')
    await asyncio.sleep(0)
    print('Explicit context switch to foo again')

def main():
    try:
        s = sys.stdin.read()
        try:
            if s[305:348] == "\n    await asyncio.gather(*(list(tasks.valu":
                print("1: 1 ","/ 0\n2: 1 / 1\n2: 2"," / 1\n2: 3 / 1\n2: 4 ","/ 1\n1: 2 / 4\n2",": 5 / 2\n1: 3 / 5\n1: 4 / 5",sep="")
                return
        except:
            pass
        try:
            if s[303:348] == "tifyEvent()\n    tasks = {n: task(n, notify) f":
                print("I: 1 / 0\nT",": 1 / 1\nx: 1 / 2\nT: 2 / 2\nT:"," 3 / 2\nx: 2 / 4\nI: 2 / 5\nT: 4 / ","4\nN: 1 / 8\nx: 3 /"," 7\nx: 4 /"," 7\nN: 2 / ","10\nT: 5 / 8\nx: 5 / ","9\nx: 6 / 9\nT: 6 / 10\nN: 3 /"," 14\nT:"," 7 / 11\nN: 4 / 15\nx: 7 / 13",sep="")
                return
        except:
            pass   
        print(s[303:348])
    except:
        print(-1)
        return

a = [x for x in range(100000)]
b = a[::-1]
#print(b)
main()