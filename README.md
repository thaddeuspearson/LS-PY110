# PY110 - Programming Foundations with Python: Intermediate
Repository for working through Launch School's PY110 Course


## :green_book: Books
1. [Introduction to Programming with Python](https://launchschool.com/books/python)

## :memo: Articles
1. [The Two Layer Problem](https://medium.com/launch-school/the-two-layer-problem-915b7587654c)

## :clipboard: Notes
### f-string alignment cheatsheet:

```python
num = 35
f'{num:5d}'            # '   35' (Leading spaces)
f'{num:05d}'           # '00035' (Leading zeros)

num = 3.141592653589793
f'{num:.3f}'           # '3.142' (3-digit precision)
f'{num:.5f}'           # '3.14159' (5-digit precision)

string = 'Hello'
f'{string:<10s}'       # 'Hello     ' (Left aligned)
f'{string:>10s}'       # '     Hello' (Right aligned)
f'{string:^10s}'       # '  Hello   ' (Centered)
```