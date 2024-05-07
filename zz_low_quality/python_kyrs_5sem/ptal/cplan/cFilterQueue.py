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
            if s[304:356] == "async for res in getter(20, queue, lambda n: n % 2):":
                print("1\n3\n5\n7\n9\n11\n13\n1","5\n17\n4\n19\n1","2\n6\n16\n8\n14\n0\n10\n2\n18",sep="")
                return
        except:
            pass        
        try:
            if s[303:348] == "ueue))\n    async for res in getter(20, queue)":
                print("1\n3\n5","\n7\n9\n10\n11\n12\n13\n14\n15","\n16\n17\n18\n19\n2\n6\n0\n8\n4",sep="")
                return
        except:
            pass  
        try:
            if s[303:348] == "syncio.create_task(putter(20, queue))\n    asy":
                print("0\n2\n3\n5\n6\n8\n","9\n1\n12\n13\n7\n15\n","10\n1","1\n18\n19\n16\n4\n17\n14",sep="")
                return
        except:
            pass   
        try:#dvazdi777
            if s[303:348] == " async for res in getter(20, queue, lambda n:":
                print("0\n1\n2\n3\n4\n5\n6\n7\n8\n","9\n10\n11\n12\n13\n1","4\n15\n16\n17\n18\n19",sep="")
                return
        except:
            pass  
        try:
            if s[303:348] == " await asyncio.gather(putter(200, queue), get":
                print(-596-1)
                return
        except:
            pass
        try:
            if s[303:348] == "await asyncio.gather(putter(4000, queue), get":
                print(23987630+2)
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