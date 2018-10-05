message = "[REDACTED]"
key = ""

r,o,u,x,h=range,ord,chr,"".join,hex
def e(m,k):
 l=len(k);s=[m[i::l]for i in r(l)]
 for i in r(l):
  a,e=0,""
  for c in s[i]:
   a=o(c)^o(k[i])^(a>>2)
   e+=u(a)
  s[i]=e
 return x(h((1<<8)+o(f))[3:]for f in x(x(y)for y in zip(*s)))

print(e(message,key))


# 473c23192d4737025b3b2d34175f66421631250711461a7905342a3e365d08190215152f1f1e3d5c550c12521f55217e500a3714787b6554
