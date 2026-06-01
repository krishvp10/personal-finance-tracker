 CREATE TABLE transactions (
    ID SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    type VARCHAR(10) NOT NULL CHECK (type IN ('income', 'expense')),
    category VARCHAR(20) NOT NULL,
    description VARCHAR(50) NOT NULL
 );

