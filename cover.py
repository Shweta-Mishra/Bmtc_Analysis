import json
import ast
file=open("route3.csv","r")
o=open("output3.txt","a")
#a=file.readline()
#print a
c=0
for a in file:
 m=a.find('[')
 st=a[:m-2]
 di={}
 di["k"]={"geometry":{"type":"LineString","coordinates":[]},"type":"Feature","properties":{"route_no":st}}
 #print c,"counter"
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
  d["latlons"][0],d["latlons"][1]=float(d["latlons"][1]),float(d["latlons"][0])
  di["k"]["geometry"]["coordinates"].append(d["latlons"])
 c+=1
 json.dump(di["k"],o)
 o.write("\n")

 #print type(d)
 #print di
 #print d["latlons"]
#print di