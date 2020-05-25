import sys;U,W,Y,i,z,M,t,s,J,k,n,w,f,q,D,e,K=open,list,range,len,True,print,chr,input,ord,sys.argv,0,[0],[],{},{},0,[]
with U(k[1],"r")as f:f=W(f.read())
K=[j for j in Y(i(f))if f[j]=="["]
def y(r):
 global q;d=0;T=r+1
 while z:
  if f[T]=="]":
   if d>0:d-=1
   else:q[r]=T;break
  elif f[T]=="[":d+=1
  T+=1
for o in K:y(o)
for x,y in q.items():D[y]=x
def P(G):
 global n,w,f,q,D,e
 if G==">":w.append(0);n+=1
 if G=="<":n-=1
 if G=="+":
  w.append(0);w[n]+=1
  if w[n]>255:w[n]=0
 if G=="-":
  w.append(0);w[n]-=1
  if w[n]<0:w[n]=255
 if G==".":M(t(w[n]),end="")
 if G==",":u=s("?");w[n]=J(u)
 if G=="["and w[n]==0:e=q[e]
 if G=="]"and w[n]!=0:e=D[e]
while z:
 if e>i(f)-1:break
 P(f[e]);e+=1
