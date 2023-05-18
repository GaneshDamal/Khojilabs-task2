CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  product VARCHAR(255) NOT NULL
);

INSERT INTO users (name, product) VALUES ('John Doe', 'Product A');
INSERT INTO users (name, product) VALUES ('Jane Smith', 'Product B');
INSERT INTO users (name, product) VALUES ('Alice Johnson', 'Product A');
INSERT INTO users (name, product) VALUES ('Bob Anderson', 'Product C');