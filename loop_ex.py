

str = "hello my name is inigo montoya you killed my father prepare to die"
ls = str.split()
x=0
for i in ls:
    if i == 'my':
        x += 1
print(f'number of my: {x}')