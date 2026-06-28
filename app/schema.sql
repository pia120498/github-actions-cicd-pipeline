CREATE DATABASE IF NOT EXISTS taskdb;

USE taskdb;

CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    completed BOOLEAN DEFAULT FALSE
);

INSERT INTO tasks (name, completed) VALUES
('Deploy Docker Container', FALSE),
('Configure GitHub Actions', TRUE),
('Deploy to Kubernetes', FALSE);