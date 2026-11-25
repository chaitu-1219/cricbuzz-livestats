CREATE DATABASE IF NOT EXISTS cricbuzz_livestats;

USE cricbuzz_livestats;

-- --------------------------------
-- Countries
-- --------------------------------

CREATE TABLE countries (

    country_id INT AUTO_INCREMENT PRIMARY KEY,

    country_name VARCHAR(100) UNIQUE NOT NULL

);

-- --------------------------------
-- Teams
-- --------------------------------

CREATE TABLE teams (

    team_id INT AUTO_INCREMENT PRIMARY KEY,

    team_name VARCHAR(100) NOT NULL,

    country_id INT,

    FOREIGN KEY(country_id)

    REFERENCES countries(country_id)

);

-- --------------------------------
-- Venues
-- --------------------------------

CREATE TABLE venues (

    venue_id INT AUTO_INCREMENT PRIMARY KEY,

    venue_name VARCHAR(200),

    city VARCHAR(100),

    country VARCHAR(100),

    capacity INT

);

-- --------------------------------
-- Series
-- --------------------------------

CREATE TABLE series (

    series_id INT AUTO_INCREMENT PRIMARY KEY,

    series_name VARCHAR(200),

    match_type VARCHAR(30),

    host_country VARCHAR(100),

    start_date DATE,

    end_date DATE

);

-- --------------------------------
-- Players
-- --------------------------------

CREATE TABLE players (

    player_id INT AUTO_INCREMENT PRIMARY KEY,

    full_name VARCHAR(200),

    team_id INT,

    role VARCHAR(50),

    batting_style VARCHAR(100),

    bowling_style VARCHAR(100),

    FOREIGN KEY(team_id)

    REFERENCES teams(team_id)

);

-- --------------------------------
-- Matches
-- --------------------------------

CREATE TABLE matches (

    match_id BIGINT PRIMARY KEY,

    series_id INT,

    venue_id INT,

    team1_id INT,

    team2_id INT,

    match_date DATE,

    status VARCHAR(100),

    FOREIGN KEY(series_id)

    REFERENCES series(series_id),

    FOREIGN KEY(venue_id)

    REFERENCES venues(venue_id),

    FOREIGN KEY(team1_id)

    REFERENCES teams(team_id),

    FOREIGN KEY(team2_id)

    REFERENCES teams(team_id)

);

-- --------------------------------
-- Match Results
-- --------------------------------

CREATE TABLE match_results (

    result_id INT AUTO_INCREMENT PRIMARY KEY,

    match_id BIGINT,

    winner_team INT,

    victory_margin VARCHAR(50),

    victory_type VARCHAR(20),

    toss_winner INT,

    toss_decision VARCHAR(20),

    FOREIGN KEY(match_id)

    REFERENCES matches(match_id),

    FOREIGN KEY(winner_team)

    REFERENCES teams(team_id)

);

-- --------------------------------
-- Player Statistics
-- --------------------------------

CREATE TABLE player_statistics (

    stat_id INT AUTO_INCREMENT PRIMARY KEY,

    player_id INT,

    format VARCHAR(20),

    matches INT,

    runs INT,

    wickets INT,

    batting_average DECIMAL(6,2),

    bowling_average DECIMAL(6,2),

    strike_rate DECIMAL(6,2),

    economy DECIMAL(6,2),

    hundreds INT,

    fifties INT,

    catches INT,

    stumpings INT,

    FOREIGN KEY(player_id)

    REFERENCES players(player_id)

);

-- --------------------------------
-- Batting Scorecards
-- --------------------------------

CREATE TABLE batting_scorecards (

    scorecard_id BIGINT AUTO_INCREMENT PRIMARY KEY,

    match_id BIGINT,

    player_id INT,

    innings INT,

    batting_position INT,

    runs INT,

    balls INT,

    fours INT,

    sixes INT,

    strike_rate DECIMAL(6,2),

    FOREIGN KEY(match_id)

    REFERENCES matches(match_id),

    FOREIGN KEY(player_id)

    REFERENCES players(player_id)

);

-- --------------------------------
-- Bowling Scorecards
-- --------------------------------

CREATE TABLE bowling_scorecards (

    bowling_id BIGINT AUTO_INCREMENT PRIMARY KEY,

    match_id BIGINT,

    player_id INT,

    innings INT,

    overs DECIMAL(4,1),

    maidens INT,

    runs_given INT,

    wickets INT,

    economy DECIMAL(6,2),

    FOREIGN KEY(match_id)

    REFERENCES matches(match_id),

    FOREIGN KEY(player_id)

    REFERENCES players(player_id)

);

-- --------------------------------
-- Indexes
-- --------------------------------

CREATE INDEX idx_player_name
ON players(full_name);

CREATE INDEX idx_match_date
ON matches(match_date);

CREATE INDEX idx_team_name
ON teams(team_name);

CREATE INDEX idx_player_runs
ON player_statistics(runs);

CREATE INDEX idx_player_wickets
ON player_statistics(wickets);

CREATE INDEX idx_match_status
ON matches(status);