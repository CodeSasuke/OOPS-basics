# Encapsulation in Python

## Why do we need encapsulation?

An object should protect its important state and control how that state changes. If every caller can change a bank balance directly, invalid values become easy to create.

```python
account.balance = -100000
```

The problem is not only privacy. The deeper problem is that no rule controls the state.

## Think first

Before running [encapsulation.py](encapsulation.py), predict:

1. Can a deposit of `50` increase the balance?
2. What should happen when withdrawing more than the balance?
3. Why should callers use `deposit()` and `withdraw()` instead of changing `_balance` directly?

Run:

```bash
python3 encapsulation.py
```

Expected output:

```text
Asha's balance: 125
Rejected invalid operation: Insufficient balance
```

## The central idea

Encapsulation groups data with the methods that protect and operate on it.

```text
outside caller
      |
      v
 deposit() / withdraw()
      |
      +-- validate amount
      +-- enforce balance rule
      +-- change _balance
```

The caller asks the object to perform a valid operation. The object owns the rules.

## What happens without encapsulation?

Business rules are scattered across callers:

```python
account._balance += 50
account._balance -= 200  # invalid state is possible
```

Every caller must remember every rule. One caller will eventually forget one.

## Python's convention

Python does not enforce private fields in the same way as some languages. A leading underscore means:

```text
_balance = internal implementation detail; do not change directly
```

This is a communication convention, supported by design and discipline. Name mangling with `__balance` adds stronger accidental-access protection, but it is not absolute security.

## Controlled access with `property`

The live example uses `@property` for read access:

```python
@property
def balance(self):
    return self._balance
```

This allows:

```python
print(account.balance)
```

while keeping writes controlled by `deposit()` and `withdraw()`.

`property` is an OOP + Python feature; the example introduces it here because it demonstrates encapsulated read access. Study [properties.py](properties.py) and its future notes for a dedicated lesson.

## Common mistakes

- Thinking a leading underscore creates a secure private variable.
- Exposing setters that allow every invalid value.
- Putting validation in callers instead of the object that owns the rule.
- Hiding every attribute without providing useful operations.

## Quick revision

```text
Encapsulation = state + rules for changing that state

Use methods to protect invariants.
Use a leading underscore to communicate internal state.
Expose safe operations instead of unrestricted mutation.
```
