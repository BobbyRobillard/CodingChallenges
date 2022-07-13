-- Create universe database
CREATE DATABASE universe;

-- Connect to created db
\c universe

-- Creates db tables
CREATE TABLE galaxy(
  galaxy_id SERIAL PRIMARY KEY,
  name VARCHAR(30) UNIQUE NOT NULL,
  galaxy_type TEXT,
  age_in_millions_of_years INT NOT NULL,
  description TEXT,
);

CREATE TABLE star(
  star_id SERIAL PRIMARY KEY,
  name VARCHAR(30) UNIQUE NOT NULL,
  description TEXT,
  age_in_millions_of_years INT NOT NULL,
  galaxy_id INT REFERENCES galaxy(galaxy_id)
);

CREATE TABLE planet(
  planet_id SERIAL PRIMARY KEY,
  name VARCHAR(30) UNIQUE NOT NULL,
  age_in_millions_of_years INT NOT NULL
  distance_from_earth NUMERIC(10, 1) NOT NULL,
  has_life BOOLEAN NOT NULL,
  is_spherical BOOLEAN NOT NULL,
  star_id INT REFERENCES star(star_id)
);

CREATE TABLE moon(
  moon_id SERIAL PRIMARY KEY,
  name VARCHAR(30) UNIQUE NOT NULL,
  description TEXT,
  age_in_millions_of_years INT NOT NULL,
  planet_id INT REFERENCES planet(planet_id)
);

CREATE TABLE extra_galaxy_info(
  latin_name VARCHAR(50) UNIQUE,
  galaxy_id INT REFERENCES galaxy(galaxy_id)
);

-- Add Foreign key relations
