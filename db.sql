CREATE TABLE Station(
  stationID SERIAL PRIMARY KEY,
  type VAR (F,M,P),
  place VARCHAR (50),
  lat DOUBLE DEFAULT 0,
  lng DOUBLE DEFAULT 0
);


CREATE TABLE User (
  userID SERIAL PRIMARY KEY,
  name VARCHAR (30),
  password VARCHAR (30),
  value DECIMAL(4, 2)
);


CREATE TABLE report(
  id SERIAL PRIMARY KEY,
  fk_userID int FOREIGN KEY REFERENCES User(userID),
  fk_stationID int FOREIGN KEY REFERENCES Station(stationID),
  description VARCHAR (100)
)