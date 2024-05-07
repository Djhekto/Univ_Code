import asyncio

class NotifyEvent(asyncio.Event):
    imena={}

    def set(self, Name=None):
        self.Name=Name
        super().set()

    @property
    async def wait(self):
        await super().wait()
        NotifyEvent.clear(self)
        return self.Name

    def uvel2(self, name):
        if name in self.imena:
            self.imena[name][1]+=1
        else:
            self.imena[name]=[0,1]  
            
    def uvel1(self, name):
        if name in self.imena:
            self.imena[name][0]+=1
        else:
            self.imena[name]=[1,0]      

async def task(name, object):
    while 1:
        try:
            J = await object.wait
        except:
            break
        if J==None:
            break
        if J==name:
            NotifyEvent.uvel1(object, name)
            print(J,": ",object.imena[name][0]," / ",object.imena[name][1],sep="")
        else:
            NotifyEvent.uvel2(object, name)
     

##   
