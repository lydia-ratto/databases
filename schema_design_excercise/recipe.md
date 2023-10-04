1. Extract nouns from the user stories or specification

As a person who loves movies,
So I can list all my favourite movies
I want to see a list of movies' titles.

As a person who loves movies,
So I can list all my favourite movies
I want to see a list of movies' genres.

As a person who loves movies,
So I can list all my favourite movies
I want to see a list of movies' release years.

Nouns:

movies, titles, genres, release year

2. Infer the Table Name and Columns
Put the different nouns in this table. Replace the example with your own nouns.


Table name: movies

Column names: title, genre, release_year



3. Decide the column types

Here's a full documentation of PostgreSQL data types.

Most of the time, you'll need either text, int, bigint, numeric, or boolean. If you're in doubt, do some research or ask your peers.

Remember to always have the primary key id as a first column. Its type will always be SERIAL.


id: SERIAL
title: text
genre: text
release_year: int



4. Write the SQL

-- file: movies_table.sql

CREATE TABLE movies (
  id SERIAL PRIMARY KEY,
  title text,
  genre text,
  release_year int
);
5. Create the table
psql -h 127.0.0.1 movies_directory < movies_table.sql