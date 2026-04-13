# ByteBites Final Applied AI System

## Original Project

This project started from my week 3 ByteBites backend. The original version focused on turning a vague feature request into a clean object-oriented design using four core classes: `Customer`, `MenuItem`, `Menu`, and `Order`. The backend could store customers, manage menu items, filter categories, and calculate order totals.

## What I Added for Week 8

For the week 8 final version, I extended ByteBites with a lightweight recommendation feature. The system can now suggest menu items based on a customer's favorite category and item popularity. The goal was to take the original structured backend and add a simple but real “AI-style” feature that changes how the system behaves.

## Why This Matters

The main idea behind this update is that recommendation systems are one of the most common real-world AI features. Even though this project does not use machine learning, it still shows the important logic behind recommendation: taking user preferences, comparing them against available data, scoring the options, and ranking the results.

## System Architecture Overview

The system has four main classes:

- `Customer` stores the customer's name, favorite category, and purchase history
- `MenuItem` stores item data like name, price, category, and popularity
- `Menu` stores all menu items and now also handles recommendations
- `Order` stores selected items and calculates the total

The data flows like this:

1. A customer is created, optionally with a favorite category
2. Menu items are loaded into the menu
3. The menu recommendation logic checks each item
4. Matching category items get a stronger score
5. Popularity also contributes to the final score
6. The top ranked items are returned as recommendations

## New Feature: Recommendation Logic

The main added feature is the recommendation system inside the `Menu` class.

### Scoring idea
- +5 points if the menu item matches the preferred category
- +popularity rating points based on item popularity
- sort highest score first
- break ties using lower price, then name

This gives the system a simple ranking method that feels more personalized than just listing all items.

## Reliability / Testing

I tested both the original backend behavior and the new recommendation feature.

The tests now check:

- order totals with multiple items
- empty order totals
- category filtering
- customer purchase history
- category-based recommendations
- popularity-based ranking inside a category
- customer-based recommendations using favorite category
- empty recommendations when no preference is saved

This matters because I wanted to show that the new feature is not just described in the README but actually works in code.

## Files

- `models.py` → backend logic and recommendation feature
- `test_bytebites.py` → tests for old and new behavior
- `bytebites_design.md` → updated design and data flow
- `bytebites_spec.md` → original feature request

## How to Run

### Run tests
```bash
pytest