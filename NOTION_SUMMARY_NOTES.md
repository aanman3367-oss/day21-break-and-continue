# #DAY 21 — BREAK AND CONTINUE IN PYTHON

---

## 1. Introduction

Sometimes while working with loops, we may want to:

- **stop the loop immediately**, or
- **skip a particular iteration**

Python provides two keywords for this:

- `break`
- `continue`

They help control the flow of loops.

---

# 2. `break` Statement

The `break` statement is used to **terminate the loop immediately**.

When `break` executes, the loop stops even if the condition is still True.

### Example

```python
for i in range(10):
	if i==5:
		break
	print(i)
```

### Output

```
0
1
2
3
4
```

The loop stops when `i` becomes **5**.

---

### Example — Password System

```python
while True:
	password=input("Enter password: ")

	if password=="python123":
		print("Access Granted")
		break
```

The loop continues until the correct password is entered.

---

# 3. `continue` Statement

The `continue` statement is used to **skip the current iteration** and move to the next one.

### Example

```python
for i in range(5):
	if i==2:
		continue
	print(i)
```

### Output

```
0
1
3
4
```

When `i` becomes **2**, that iteration is skipped.

---

# 4. Difference Between `break` and `continue`

| Feature | break | continue |
| --- | --- | --- |
| Stops loop | ✔ Yes | ❌ No |
| Skips iteration | ❌ No | ✔ Yes |
| Loop continues | ❌ No | ✔ Yes |

---

# 5. Real Example — Skip Even Numbers

```python
for i in range(10):
	if i%2==0:
		continue
	print(i)
```

Output:

```
1
3
5
7
9
```

---

# 6. Emulating a **Do-While Loop** in Python

Python does **not have a built-in `do-while` loop**, but we can emulate it using `while True` with `break`.

A **do-while loop runs the code at least once**, then checks the condition.

### Example

```python
while True:
	num=int(input("Enter a number (0 to stop): "))

	print("You entered:",num)

	if num==0:
		break
```

### Why this works

- The loop **runs first**
- Then the condition is checked
- If condition becomes true → `break` stops the loop

This behaves like a **do-while loop**.

---

# 📝 Summary

- `break` → stops the loop immediately
- `continue` → skips current iteration
- `while True + break` → can emulate a do-while loop

---

## One-Line Concept

> `break` stops a loop, `continue` skips an iteration, and a do-while loop can be simulated using `while True` with `break`.
>
