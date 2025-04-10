'''
### 8. Compress a String (Run-Length Encoding)
- **Input:** `"aaabbc"`  
- **Output:** `"a3b2c1",3a2b1c`
- **
- 💡 *Checks string building and loops.*

---
'''
input_string = input("enter string you want  :")
d ={}
out_str = ""
out_str2= ""
for i in input_string:
    d[i] = d.get(i,0)+1

for k,v in d.items():
    out_str = out_str+k+str(v)
    out_str2= out_str2+str(v)+k
    
print(out_str)
print(out_str2)


