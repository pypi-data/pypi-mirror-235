# A "fast-forward and rewind" custom iterator for flexible traversal through iterables 

## Tested against Windows / Python 3.11 / Anaconda

## pip install loophopper

```python
from loophopper import FFIter
# Create an FFIter object for a range iterable
l = FFIter(range(40), ignore_exceptions=True, exception_replacement=None)
for no in l:
	if no % 10 == 0:
		print(f"number: {no}, 2 forward: {l.forward(2)}")
	if no % 7 == 0:
		print(f"number: {no}, 1 back: {l.back(1)}")

# Create an FFIter object for a dictionary iterable
l = FFIter(
	{k: k * 2 for k in range(40)}, ignore_exceptions=True, exception_replacement=None
)
for no in l:
	if no[0] % 10 == 0:
		print(f"number: {no}, 2 forward: {l.forward(2)}")
	if no[1] % 7 == 0:
		print(f"number: {no}, 1 back: {l.back(1)}")

l = FFIter(
	{k: k * 2 for k in range(40)}, ignore_exceptions=True, exception_replacement=None
)
for no in l:
	if l.active_index%5==0:
		print(f'{l.active_index}: {no}')

# number: 0, 2 forward: 2
# number: 0, 1 back: None
# number: 7, 1 back: 6
# number: 10, 2 forward: 12
# number: 14, 1 back: 13
# number: 20, 2 forward: 22
# number: 21, 1 back: 20
# number: 28, 1 back: 27
# number: 30, 2 forward: 32
# number: 35, 1 back: 34
# number: (0, 0), 2 forward: (2, 4)
# number: (0, 0), 1 back: None
# number: (7, 14), 1 back: (6, 12)
# number: (10, 20), 2 forward: (12, 24)
# number: (14, 28), 1 back: (13, 26)
# number: (20, 40), 2 forward: (22, 44)
# number: (21, 42), 1 back: (20, 40)
# number: (28, 56), 1 back: (27, 54)
# number: (30, 60), 2 forward: (32, 64)
# number: (35, 70), 1 back: (34, 68)
# 0: (0, 0)
# 5: (5, 10)
# 10: (10, 20)
# 15: (15, 30)
# 20: (20, 40)
# 25: (25, 50)
# 30: (30, 60)
# 35: (35, 70)

```

