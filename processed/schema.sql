
CREATE TABLE Park (
  ID int,
  `Name` varchar(255),
  City varchar(25),
  State varchar(25),

  PRIMARY KEY (ID)
);

CREATE TABLE Player (
  ID int,
  FirstName varchar(25),
  LastName varchar(25),
  GivenName varchar(25),
  BirthCity varchar(25),
  BirthState varchar(25),
  BirthCountry varchar(25),
  BirthDate DATE,
  Bats ENUM('R', 'L', 'B'),
  Throws ENUM('R', 'L', 'B'),
  Weight int,
  Height int,
  DebutDate DATE,

  PRIMARY KEY (ID)
);

CREATE TABLE Team (
  ID int,

  PRIMARY KEY (ID)
);

CREATE TABLE TeamName (
  Year YEAR,
  TeamID int,
  `Name` varchar(255),

  PRIMARY KEY (Year, TeamID),
  FOREIGN KEY (TeamID) REFERENCES Team (ID)
);

CREATE TABLE TeamMember (
  Year YEAR,
  TeamID int,
  PlayerID int,

  PRIMARY KEY (Year, TeamID, PlayerID),
  FOREIGN KEY (TeamID) REFERENCES Team(ID),
  FOREIGN KEY (PlayerID) REFERENCES Player(ID)
);

CREATE TABLE Game (
  ID int,
  Park int NOT NULL,
  HomeTeam int NOT NULL,
  AwayTeam int NOT NULL,
  HomeScore int,
  AwayScore int,

  PRIMARY KEY (ID),
  FOREIGN KEY (Park) REFERENCES Park (ID),
  FOREIGN KEY (HomeTeam) REFERENCES Team (ID),
  FOREIGN KEY (AwayTeam) REFERENCES Team (ID)
);

CREATE TABLE Event (
  GameID int,
  EventID int UNSIGNED,
  HomeScore int,
  AwayScore int,
  Batter int,
  Pitcher int,

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
  GameID int,
  EventID int UNSIGNED,
  Comment TEXT,

  PRIMARY KEY (GameID, EventID),
  FOREIGN KEY (GameID) REFERENCES Game (ID),
  FOREIGN KEY (GameID, EventID) REFERENCES Event (GameID, EventID)
);
