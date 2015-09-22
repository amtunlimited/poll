CREATE TABLE questions (
    qid INT AUTO_INCREMENT,
    question TEXT,
    madeOn DATETIME,
    primary key (qid)
);

CREATE TABLE options (
    oid INT AUTO_INCREMENT,
    option TEXT,
    primary key (oid)
);

CREATE TABLE vote (
    vid INT AUTO_INCREMENT,
    oid INT,
    voteDate DATETIME,
    primary key (vid)
);