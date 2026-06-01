## Personal Finance Tracker
A personal finance tracking system using Python and PostgreSQL.

## Tech Stack
Python, PostgreSQL, psycopg2

## Status
functional - yet to be improved 

## overview
this is a cli finance tracker that takes the user input according to the categories of where it is spent. 
data is stored in postgresql based database.
psycopg2 is used for connection of database and python.
data can be retrieved according to the type 'income' or 'expense' or also can be retrieved on the basis of category on which money is spent(eg. food , travel).
a montly summary of user defined month can also be retrieved along with the net saving of that month

## How to Run
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Set up PostgreSQL and create database: `CREATE DATABASE personal_finance;`
4. Run schema: `psql -U postgres -d personal_finance -f schema.sql`
5. Run: `python main.py`

## What I'd Improve Next
1 Error handling for invalid inputs
2 Input validation (amount > 0, date format)
3 Transaction model class
4 Filter by date range
5 Running total using window functions
6 Integrate categories table for predefined category management