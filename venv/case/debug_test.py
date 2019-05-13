import requests

header={
    "Accept":"image/webp,image/apng,image/*,*/*;q=0.8"
}
res = requests.get(url="http://jgtest.qida.yunxuetang.com.cn/Services/DrawImage.ashx?t=vc&f=%E5%AE%8B%E4%BD%93&v=tbvvw0hcjzbg",
                   headers=header)

print(res.content)
with open(r"E:\1.png","wb") as fp:
    fp.write(res.content)