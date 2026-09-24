# Attendance Safety Calculator

A command-line Python tool that helps students track attendance across multiple subjects and stay above the required 75% minimum. It tells you how many classes you can safely miss, or how many you need to attend to reach the cutoff — for each subject and overall.

## Problem it solves

Most colleges require students to maintain at least 75% attendance to be eligible to sit for exams. Students juggling multiple subjects often lose track of exactly where they stand in each one, leading to last-minute stress or unnecessary "safe" absences being missed. This tool gives an instant, per-subject and overall answer, and remembers your data between runs.

## Features

- Tracks attendance across multiple subjects (not just one)
- Calculates current attendance percentage per subject
- Tells you the max classes you can miss and stay above 75%, or how many you need to attend if below
- Shows an overall attendance summary and flags "at risk" subjects
- Saves data to a file so it persists between runs
- Validates input (rejects invalid numbers, negative values, attended > total)
- Lets you check multiple times without restarting the program

## Technologies used

- Python 3 (standard library only — no external installs required)
- `json` module for data persistence

## Project structure