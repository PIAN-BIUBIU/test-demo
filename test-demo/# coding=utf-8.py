# coding=utf-8
print('hello world')
print('hello nihao')
a='ABC'
print(a)
num1=10
num2=3
result=num1/num2
print(result)
round_result=round(result,2)
print(round_result)
print(True and True)

a='python'
print('hello,',a or 'world')

b=''
print('hello,',b or 'world')

t='special string:\',",\\,\\\\,\\n,\\t)'
print(t)

x=r'''"To be, or not to be": that is the question.
Whether it's nobler in the mind to suffer.'''

print(x)

x='hello {2},hello {0},hello {1}'
b=x.format('World','beijing','aoyun')
print(b)

w="life is short, {q} {e} {w}."
qi='you'
ei='need'
wi='python'
r=w.format(q=qi,e=ei,w=wi)
print(r)

print('这是一句中英文混合的Python')
print('Hello World!')

sss='AABCDEFGHHIJ'
print(sss[1:9])