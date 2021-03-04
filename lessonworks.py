
telebeler=[
    {
        "ad":"Anar",
        "yas":17
    },
    {
        "ad":"Rza",
        "yas":19
    },
    {
        "ad":"Saleh",
        "yas":30
    }
]


yaslar=[]
for telebe in telebeler:
    print(telebe)
    yaslar.append(telebe['yas'])


print(max(yaslar))

print(yaslar)
