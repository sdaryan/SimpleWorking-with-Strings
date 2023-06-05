## Working with Strings

Saman, a newcomer, has learned to work with strings. To start working with strings, he is faced with a relatively simple question, but he needs your help to be able to do it. Saman has to write a program that reads a string from the input and applies the following changes to it:

1- Remove all vowels.

2- Print a dot before each consonant letter.

3- Write all remaining consonant letters in lowercase.

(The vowel letters are aeiou.)


## Input:
```python
aBAcAba
```

## Output:
```python
.b.c.b
```

------------------------------------------------------------------------------
## مجموع کمترین مسافت بین دو نقطه از مجموع سه نوع عدد ورودی 

به مناسبت عید نوروز سه دوست قدیمی می خواهند همدیگر را ملاقات کنند. آذرمهر، آذرگون و مهرآئین قصد دارند در یک نقطه همدیگر را ملاقات کنند. منزل این سه نفر روی خط راست قرار دارد (محور xها) خانه ی آذرمهر در نقطه ی x1 قرار دارد، خانه ی آذرگون در نقطه ی x2 قرار دارد و خانه ی مهرآئین در نقطه ی x3 قرار دارد. آنها در مجموع می خواهند کمترین مسافت را طی کنند. با در دست داشتن x1 x2 x3 کمترین مسافتی که این سه در مجموع باید طی کنند تا در یک نقطه همدیگر را ملاقات کنند را محاسبه کنید. لطفا در صورتی که جواب عدد صحیح شد آن را بدون نقطه ی عدد اعشاری چاپ کنید مثلا در نمونه ی زیر اگر چاپ کنید 6.0 غلط است.

## ورودی نمونه
```python
6 9 10
```
## خروجی نمونه
```python
4
```
کد برنامه 
```python
input_str = input()

vowels = 'aeiouAEIOU'  # حروف صدادار
output_str = ''

for i in input_str:
    if i not in vowels:
        output_str += '.' + i.lower()

print(output_str)
```
