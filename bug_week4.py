# bug_week4.py
# BUG OF THE WEEK - Week 4: if Statements   (Test-Case Edition)
# =============================================================================
# This file has FOUR bugs. Every one of them RUNS without crashing and prints
# something -- which is exactly the trap. "It ran" does not mean "it works."
#
# You find these bugs the way engineers really do: with TEST CASES.
# A test case is just a known INPUT plus the OUTPUT you EXPECT for it.
# Run the code, compare the ACTUAL output to what you expected, and every
# mismatch is a bug.
#
# The sneaky part: some bugs are only wrong for CERTAIN inputs. A section can
# look perfect on the first value you try and be broken on the next. That is
# why you test several cases -- especially BOUNDARIES (a number right on a
# cutoff) and EDGE CASES (odd capitalization, a value that isn't in a list).
#
# HOW TO WORK THROUGH IT
#   1. Run the file. Each section prints its result for every test input.
#   2. Go to that section's TEST CASE TABLE and fill in ACTUAL, then PASS/FAIL.
#   3. Each FAIL points at the bug. Fix the code, re-run, and confirm every
#      row now PASSES.
#   4. Add at least TWO of your own test cases to each list -- try to find an
#      input the table did not already cover.
#   5. For Bug 3, practice the VS Code debugger: put a breakpoint on the first
#      'if', Step Over (F10), and WATCH which branch runs.
# =============================================================================


# =============================================================================
# BUG 1 - Grade Checker
# Category: test-case-triggered.  Hint: test grades right ON the cutoffs.
# =============================================================================
print("--- Grade Checker ---")

grades_to_test = [95, 90, 85, 80, 72, 86, 92]          # <-- add your own grades
for grade in grades_to_test:
    if grade >= 90:
        result = "You got an A!"
    elif grade >= 80:
        result = "You got a B!"
    else:
        result = "Keep working at it."
    print(f"  grade {grade} -> {result}")

# TEST CASE TABLE  (fill in ACTUAL, then mark PASS or FAIL)
#   INPUT | EXPECTED             | ACTUAL | PASS?
#   95    | You got an A!        |    You got an A!          | PASS
#   90    | You got an A!        |    You got an A!          | PASS
#   85    | You got a B!         |    You got a B!           | PASS
#   80    | You got a B!         |    You got a B!           | PASS
#   72    | Keep working at it.  |    Keep working at it.    | PASS
#   92    | You got an A!        |    You got an A!          | PASS    <- add your own
#   86    | You got a B!         |    You got a B!           | PASS    <- add your own

# a) Test case number 80
# b) the test case for grade 80 was only a > and not a >=


# =============================================================================
# BUG 2 - User Check
# Category: test-case-triggered.  A warning should appear ONLY for users who
# are NOT on the list.  Hint: test a user who SHOULD be allowed AND one who
# should NOT -- one test case alone won't reveal this one.
# =============================================================================
print("\n--- User Check ---")
approved_users = ["admin", "natalie", "carlos", "priya"]

users_to_test = ["admin", "guest", "natalie", "hacker", "Keatts"]     # <-- add your own
for current_user in users_to_test:
    if current_user not in approved_users:
        print(f"  WARNING: '{current_user}' is not an approved user!")
    else:
        print(f"  Welcome, {current_user}!")

# TEST CASE TABLE  (fill in ACTUAL, then mark PASS or FAIL)
#   INPUT   | EXPECTED                                   | ACTUAL | PASS?
#   admin   | Welcome, admin!                            |   yes     | PASS
#   guest   | WARNING: 'guest' is not an approved user!  |   yes    | PASS
#   natalie | Welcome, natalie!                          |   yes     | PASS
#   hacker  | WARNING: 'hacker' is not an approved user! |   yes     | PASS
#   Keatts  | WARNING: 'Keatts' is not an approved user! |   yes     | PASS  <- add your own

# a) line 70 test cases admin and guest
# b) if current_user "not in" rather than "in"

# =============================================================================
# BUG 3 - Stage of Life
# Category: logic error -- easiest to SEE in the debugger.
# Put a breakpoint on the first 'if', Step Over (F10), and watch which branch
# runs for a teenager.  Also test one age from EVERY stage.
# =============================================================================
print("\n--- Stage of Life ---")

ages_to_test = [1, 5, 12, 11, 13, 15, 19, 20, 45, 99]      # <-- add your own
for age in ages_to_test:
    if age < 2:
        stage = "infant"
    elif age < 13:
        stage = "child"
    elif age <= 19:
        stage = "teenager"
    
    else:
        stage = "adult"
    print(f"  age {age} -> {stage}")

# TEST CASE TABLE  (fill in ACTUAL, then mark PASS or FAIL)
#   INPUT | EXPECTED | ACTUAL | PASS?
#   1     | infant   |infant    | PASS
#   5     | child    |child     | PASS
#   12    | child    |child     | PASS
#   13    | teenager |adult     | PASS
#   15    | teenager |adult     | PASS
#   19    | teenager |adult     | PASS
#   20    | adult    |adult     | PASS
#   45    | adult    |adult     | PASS
#   11    | child    |child     | PASS <- add your own

# a) age 13, 15 and 19
# b) made me realize that adult starts after "19", so the mistake was replicating "< 13" rather than adding "<= 19" 

# =============================================================================
# BUG 4 - Pizza Topping Checker
# Category: test-case-triggered.  Hint: test the SAME real topping typed with
# different capitalization, plus a topping that is not on the menu.
# =============================================================================
print("\n--- Pizza Topping Checker ---")
available_toppings = ["Pepperoni", "Mushrooms", "Green Peppers", "Olives"]

requests_to_test = ["Pepperoni", "Mushrooms", "Mushrooms", "Pineapple", "Cheese"]   # <-- add your own
for requested_topping in requests_to_test:
    if requested_topping == available_toppings[0]:
        print("  Adding pepperoni.")
    elif requested_topping == available_toppings[1]:
        print("  Adding mushrooms.")
    elif requested_topping == available_toppings[2]:
        print("  Adding green peppers.")
    elif requested_topping == available_toppings[3]:
        print("  Adding olives.")
    else:
        print(f"  Sorry, we don't have {requested_topping}.")

# TEST CASE TABLE  (fill in ACTUAL, then mark PASS or FAIL)
#   INPUT     | EXPECTED                        | ACTUAL | PASS?
#   Pepperoni | Adding pepperoni.               |    Adding pepperoni.                   | PASS
#   Mushrooms | Adding mushrooms.               |    Adding mushrooms.                   | PASS
#   mushrooms | Adding mushrooms.               |    Adding mushrooms.                   | PASS
#   Pineapple | Sorry, we don't have Pineapple. |    Sorry, we don't have Pineapple.     | PASS
#   cheese    | Sorry, we don't have cheese     |    Sorry, we don't have cheese.        | PASS  <- add your own

# a) line 135 and 130, "Mushrooms" and "mushrooms" test cases
# b) both the mushrooms needed to be the same capitlization in order for the == to refrence the ["number"]


# =============================================================================
# WHEN YOU ARE DONE
#   [X] Every table has ACTUAL filled in and PASS/FAIL marked
#   [X] You added at least two of your own test cases to each section
#   [X] You fixed each bug and re-ran until every row PASSES
#   [X] For each bug you can say (a) which test case exposed it and
#       (b) why the original code was wrong
# =============================================================================
