# Tested Inventory Service

An inventory management service with a full automated test suite, built to practice writing testable, reliable code.

## Problem
Wanted to move beyond "it works when I try it manually" and practice actually proving code correctness with automated tests — a standard professional practice.

## Features
- Add stock, remove stock (with validation against overselling)
- Check quantity for a specific item
- Flag items at or below a low-stock threshold
- Full test suite covering normal cases and error cases

## Tech Stack
Python, pytest

## How to Run Tests
```
pip install -r requirements.txt
pytest
```

## Test Coverage
9 tests covering: adding new/existing items, quantity validation, stock removal (including insufficient-stock and unknown-item errors), low-stock detection, and total inventory count.

## Future Improvements
- Add a CLI or API layer on top of this service
- Add persistence (currently in-memory only, resets each run)
- Add test coverage reporting

## What I learned
Separating core logic from any interface so it's independently testable, writing tests that check both correct behavior *and* proper error handling, and using pytest's `assert` and `pytest.raises` patterns.
