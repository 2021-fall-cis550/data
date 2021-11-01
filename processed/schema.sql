
CREATE TABLE Park (
  ID varchar(25),
  `Name` varchar(255),
  City varchar(25),
  State varchar(25),

  PRIMARY KEY (ID)
);

CREATE TABLE Team (
  ID varchar(25), -- TODO: Drop teamID and clean up the retroID column.

  PRIMARY KEY (ID)
);

CREATE TABLE TeamName (
  TeamID varchar(25),
  `Name` varchar(255),
  FirstYear YEAR,

  PRIMARY KEY (TeamID, Name),
  FOREIGN KEY (TeamID) REFERENCES Team (ID)
);

CREATE TABLE Game (
  ID varchar(25),
  Park varchar(25) NOT NULL,
  HomeTeam varchar(25) NOT NULL,
  AwayTeam varchar(25) NOT NULL,
  HomeScore varchar(25),
  AwayScore varchar(25),

  PRIMARY KEY (ID),
  FOREIGN KEY (Park) REFERENCES Park (ID),
  FOREIGN KEY (HomeTeam) REFERENCES Team (ID),
  FOREIGN KEY (AwayTeam) REFERENCES Team (ID)
);

CREATE TABLE Player (
  ID varchar(25), -- TODO: Drop PlayerID and migrate PlayerID to RetroID.
  FirstName varchar(25),
  LastName varchar(25),
  BirthCity varchar(25),
  BirthState varchar(25),
  BirthCountry varchar(25),
  BirthDate DATE,
  Bats ENUM('R', 'L', 'B'),
  Throws ENUM('R', 'L', 'B'),

  PRIMARY KEY (ID)
);

CREATE TABLE Event (
  GameID varchar(25),
  EventID int UNSIGNED,
  HomeScore varchar(25),
  AwayScore varchar(25),
  Batter varchar(25),
  Pitcher varchar(25),

  Strikes TINYINT,
  Ball TINYINT,

  Inning TINYINT,
  LineUp TINYINT,

  EventType ENUM(
    'Unknown event', 'No event', 'Generic out', 'Strikeout', 'Stolen base', 'Defensive indifference', 'Caught stealing',
    'Pickoff error', 'Pickoff', 'Wild pitch', 'Passed ball', 'Balk', 'Other advance', 'Foul error', 'Walk',
    'Intentional walk', 'Hit by pitch', 'Interference', 'Error', 'Fielders choice', 'Single', 'Double', 'Triple',
    'Home run', 'Missing play'
  ),

  PRIMARY KEY (GameID, EventID),
  FOREIGN KEY (GameID) REFERENCES Game (ID),
  FOREIGN KEY (Batter) REFERENCES Player (ID),
  FOREIGN KEY (Pitcher) REFERENCES Player (ID)
);

CREATE TABLE EventComment (
  GameID varchar(25),
  EventID int UNSIGNED,
  Comment TEXT,

  PRIMARY KEY (GameID, EventID),
  FOREIGN KEY (GameID) REFERENCES Game (ID),
  FOREIGN KEY (GameID, EventID) REFERENCES Event (GameID, EventID)
);
