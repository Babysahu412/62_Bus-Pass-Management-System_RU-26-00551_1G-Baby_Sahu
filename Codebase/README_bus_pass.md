# Bus Pass Management System

**PS No. 62** | Rungta International Skills University
School of Computer Science and Engineering | B.Tech Computer Science and Engineering

A console-based Python 3 application to issue and manage bus passes. Passes are stored in a file, so the data is still there the next time the program runs.

---

## Problem Statement

Create a console application to issue and manage bus passes. The user can issue a new pass, renew an existing pass, search a pass by ID and view all passes. Fees depend on the pass type and passenger category, and passes are saved in a file.

### Pass Types and Fees

| Pass Type | Validity | General Fee | Student Fee (25% off) |
|-----------|----------|-------------|-----------------------|
| Monthly   | 30 days  | Rs. 500     | Rs. 375               |
| Quarterly | 90 days  | Rs. 1350    | Rs. 1012.5            |
| Yearly    | 365 days | Rs. 4800    | Rs. 3600              |

- Passes are saved in `buspass.txt`.
- The first pass ID is `BP101`; later IDs are `BP102`, `BP103`, and so on.

---

## Features

- Issue a new pass (name, route, pass type, category)
- Renew an existing pass (change pass type, fee and validity)
- Search a pass by ID
- View all registered passes
- Edit a pass (name, route, category); press Enter to keep the old value
- Delete a pass, with a Yes/No confirmation
- 25% discount for students
- Validation of empty name/route, pass type and category
- Automatic save to `buspass.txt` and load on start

## Concepts Used

- Lists
- Dictionaries
- Functions
- File handling (`open`, `read`, `write`) with the `json` module

---

## Requirements

- Python 3.x (only standard library modules `json` and `os` are used)

## How to Run

```bash
python bus_pass_management.py
```

(Use `python3` instead of `python` if required on your system.) Run it from the folder where you want `buspass.txt` to be created.

---

## Menu

```
================================
     BUS PASS MANAGEMENT SYSTEM
================================
1. Issue New Pass
2. Renew Existing Pass
3. Search Pass by ID
4. View All Passes
5. Exit
6. Edit Existing Pass
7. Delete Existing Pass
================================
```

## Functions

| Function | Description |
|----------|-------------|
| `load_passes()` | Reads `buspass.txt` and returns the list of passes |
| `save_passes(passes)` | Writes the list of passes to `buspass.txt` |
| `generate_id(passes)` | Returns the next pass ID (BP101, BP102, ...) |
| `calculate_fee(pass_type, category)` | Returns the fee after the student discount |
| `find_customer(passes, pass_id)` | Returns the pass with the given ID, or `None` |
| `show_details(customer)` | Prints the details of one pass |
| `issue_pass(passes)` | Issues a new pass |
| `renew_pass(passes)` | Renews an existing pass |
| `search_pass(passes)` | Searches a pass by ID |
| `view_passes(passes)` | Shows all passes |
| `edit_pass(passes)` | Edits a pass |
| `delete_pass(passes)` | Deletes a pass |
| `main()` | Shows the menu and runs the program loop |

## Data Format

Each pass is a dictionary stored in a list and saved as JSON:

```json
{
    "id": "BP101",
    "name": "Riya",
    "route": "Route 5",
    "type": "Monthly",
    "category": "General",
    "fee": 500,
    "validity": 30
}
```

---

## Test Cases

### Test Case 1: Normal Input
**Input:** Menu option 1 (Issue), Name: Riya, Route: Route 5, Type: Monthly, Category: General
**Result:** Pass issued with ID BP101, Riya, Route 5, Monthly, Fee: Rs. 500, Valid: 30 days

### Test Case 2: Boundary / Minimum Input
**Input:** `buspass.txt` is empty, menu option 4 (View all)
**Result:** `No passes issued yet.`

### Test Case 3: Invalid Input
**Input:** Menu option 1, Name: Aman, Route: Route 7, Type: Weekly, Category: General
**Result:** The program prints `Invalid pass type!` and the pass is not issued.

### Test Case 4: Different Valid Scenario
**Input:** `buspass.txt` has BP101 (Riya, Route 5, Monthly, Rs. 500)
(a) Option 1: Aman, Route 7, Yearly, Student
(b) Option 3 (Search): ID BP101
**Result:**
(a) Pass issued with ID BP102, Aman, Route 7, Yearly, Fee: Rs. 3600, Valid: 365 days
(b) BP101, Riya, Route 5, Monthly, Fee: Rs. 500

---

## Project Structure

```
.
├── bus_pass_management.py
├── buspass.txt        (created automatically when the first pass is issued)
└── README.md
```

## Author

- Name: Baby Sahu
- Enrollment No.: RU-26-00551
- Program: B.Tech Computer Science and Engineering
- University: Rungta International Skills University
