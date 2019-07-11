from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic import CreateView
from .forms import xssurl
import urllib.parse
from string import whitespace
import socket
import sys
import http.client
import cgi
import re

def get(request):
    form=xssurl(request.GET)
    texts=None
    template_name="index.html"
    template_name="about.html"
    filt1=None
    conn=None
    av=None
    res=None
    avs=None
    count = None
    vul=None
    payl=None
    fpar=[]
    payloads=[]
    if form.is_valid():
        texts=form.cleaned_data['url']
        form=xssurl()
        if 'https://' in texts:
            pass
        elif 'http://' in texts:
            pass
        else:
            texts="http://"+texts
            furl = urllib.parse.urlparse(texts)
            urldata = urllib.parse.parse_qsl(furl.query)
            dcheck = '{uri.scheme}://{uri.netloc}/'.format(uri=furl)
            domain = dcheck.replace("https://","").replace("http://","").replace("www.","").replace("/","")
            con = http.client.HTTPConnection(domain)
            try:
                if not con.connect() :
                    av="Available"
                else:
                    av="Not avail"
            except:
                av="Not a Valid WebSite"
            fname="C:/djimple/xss/xss/assets/xss.txt"
            count=0
            pays=[]
            with open(fname,'r') as f:
                for line in f:
                    count+=1
                    final = str(line.replace("\n",""))
                    pays.append(final)
            paraname=[]
            paravalue=[]
            o=urllib.parse.urlparse(texts)
            parameters=urllib.parse.parse_qs(o.query,keep_blank_values=True)
            path=urllib.parse.urlparse(texts).scheme+"://"+urllib.parse.urlparse(texts).netloc+urllib.parse.urlparse(texts).path
            for para in parameters:
                for i in parameters[para]:
                    paraname.append(para)
                    paravalue.append(i)
            total =0
            c=0
            
            fresult=[]
            progress=0
            for pn,pv in zip(paraname,paravalue):
                foundparameter=pn
                fpar.append(str(pn))
                for x in pays:
                    validate=x.replace("",whitespace)
                    if validate== "":
                        progress=progress+1
                    else:
                        sys.stdout.flush()
                        progress=progress+1
                        enc = urllib.parse.quote_plus(x)
                        data=path+"?"+pn+"="+pv+enc
                        datas=data
                        page=urllib.request.urlopen(data)
                        sourcecode = page.read()
                        if x in str(sourcecode):
                            vul="The Parameter "+pn+" is vulnerable to Cross Site Scripting Attack"
                            payl=x
                            c=1
                            total=total+1
                            progress=progress+1
                            if c==1:
                                #filt2=None
                                filt=cgi.escape(datas)
                                worddic={'img':'','script':'','alert':'','prompt':'','confirm':'','svg':'','href':'','location':'','document':''}
                                rc=re.compile('|'.join(map(re.escape,worddic)))
                                def translate(match):
                                    return worddic[match.group(0)]
                                filt2=rc.sub(translate,filt)
                                filt1="XSS has Been Prevented and request looks like "+filt2
                            break
                        else:
                            c=0
                if c == 0:
                    
                    vul=pn+" is not Vulnerable."
                    payl="Tried Every Payload but Unsuccessfull :-("
                    res="No XSS in this Request URL"
                    filt1="URL is Safe from XSS attack"
                    progress=progress+1
                progress=0
                    
    args = {'form':form,'texts': texts,'av':av,'count':count,'fpar':fpar,'vul':vul,'payl':payl,'filt1':filt1,'res':res}
    return render(request,'index.html',args)

    
    
    
def post(self,request):
        form = xssurl(request.POST)
        if form.is_valid():
            text = form.cleaned_data['url']
            form= xssurl()
            #return redirect('/')
            #extracturl(form)
            
        #args ={'form':form, 'text': text}
        return render(request, self.template_name,{'form':form})
    


def about(request):
    return render(request,'about.html')

