#한 줄에 하나씩 숫자 입력받기
a=int(input('a 입력:'))
b=int(input('b 입력:'))
c=int(input('c 입력:'))
print(a,b,c,a+b+c)


#한 줄에 여러 개의 숫자 입력받기
a,b,c=map(int,input('a b c값 입력').split())
print(a,b,c,a+b+c)

text=input('날짜 입력 yyyy.mm.dd')
y,m,d=text.split('.')
print(text,y,m,d)

a,b,c=map(int['1','2','3'])
print(a,b,c,a+b+c)

#하나씩 적용
a,b,c=map(int,input('a b c값 입력').split())
text=input('a b c값 입력')
text=text.split()
a,b,c=map(int,text)
print(a,b,c,a+b+c)

#숫자 출력하기
x=3
y=5
print(x,y,x+y)
print('3과 5의 합은 8이다.')
#숫자와 문자 함께 출력하기 (1) 콤마 & 형변환
print(x,'과',y,'의 합은',x+y,'이다.') #-> 글자와 숫자 사이에 부자연스러운 공백 발생
print(str(x)+'과'+str(y)+'의 합은'=str(x+y)+이다.')
#숫자와 문자 함께 출력하기 (2) end=''
print(x,end='')
print('과',end='')
print(y,end='')
print('의 합은',end='')
print(x+y,end='')
print('이다.')
#숫자와 문자 함께 출력하기 (3) format()
print('{}과 {}의 합은 {}이다.'format(x,y,x+y))

#반올림: round(a), round(a,b)
print(round(3.33))
print(round(3.66))
print(round(3.66,1))

#절대값: abs(a)
print(abs(3))
print(abs(-3))

#제곱: pow(a,b)
print(pow(3,2))
print(3**2)

#나눗셈: divmod(a,b)
x,y=divmod(7,2)
print(x)
print(y)

#최대값: max(a,b,c,d,...)
print(max([7,5,1,3]))

#최소값: min(a,b,c,d,...)
print(min([7,5,1,3]))

#합: sum(집합 형태: Iterable)
print(sum([7,5,1,3]))
