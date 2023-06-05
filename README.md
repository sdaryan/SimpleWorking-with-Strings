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
## کار با رشته ها

سامان تازه کار با رشته ها رو یاد گرفته. برای شروع کار با رشته ها یه سوال نسبتا ساده پیش روی اون قرار گرفته ولی به کمک شما نیاز داره تا بتونه انجامش بده. سامان باید برنامه این بنویسه که یه رشته ی حرفی رو از ورودی بخونه و تغییرات زیر رو در اون اعمال کنه.



۱ - تمامی حروف صدادار رو پاک کنه.

۲ - قبل از هر حرف بی صدا یک نقطه چاپ کنه.

۳ - تمام حروف بی صدا که باقی مانده اند را به صورت کوچک بنویسد.

(حروف صدادار aeiou می باشند)
## ورودی نمونه
```python
aBAcAba
```
## خروجی نمونه
```python
.b.c.b
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
