import requests
key=input("请输入你要查询的网页字串")
url=f'https://www.sogou.com/web?query={key}&_asf=www.sogou.com&_ast=&w=01015002&p=400'
mycookie1="ABTEST=5|1706004485|v17; SNUID=73EDE6EBB3B5BC2EACE7AEB4B47511F0; SUID=C05E555F5452A00A0000000065AF9005; cuid=AAEVhGjsSQAAAAqgMxjZvgAANgg=; IPLOC=CN4102; SUV=00C3E8BFDF5ABCB465AF901AB8B2D437; browerV=3; osV=1"
#转成json格式，使用正则
cookie_dict = {item.split("=")[0]: item.split("=")[1] for item in mycookie1.split(";") if "=" in item}
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
         }
res=requests.get(url,headers=headers,cookies=cookie_dict)
print(type(res.text))
with open(f'{key}.html',mode='wb') as f:
    f.write(res.content)