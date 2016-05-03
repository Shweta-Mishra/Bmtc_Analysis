import json
import ast
file=open("RouteMap2.csv","r")
#a=file.readline()
di={}
#print a
c=0
for a in file:
 m=a.find('[')
 st=a[:m-1]
 di[st]=[]
 print c,"counter"
 a=a.replace("\'","")
 if c>907:
  break
 while a.find('{')!=-1:
  i=a.find('{')
  j=a.find('}')
  s=a[i:j+1]
  s=s.replace("\"\"","\'")
  #print is
  a=a[j+2:]
 # print a
  d=ast.literal_eval(s)
  di[st].append(d["latlons"])
 c+=1
 #print type(d)
 #print di
 #print d["latlons"]
print di
