CREATE DATABASE IF NOT EXISTS valoracions_db;
USE valoracions_db;

CREATE TABLE IF NOT EXISTS valoracions_tipus (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(50) NOT NULL
);

INSERT INTO valoracions_tipus (nom) VALUES 
('Excel·lent'), ('Notable'), ('Bé'), ('Suficient'), ('Insuficient');

CREATE TABLE IF NOT EXISTS valoracions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dni VARCHAR(10) NOT NULL,
    poblacio VARCHAR(100) NOT NULL,
    valoracio INT NOT NULL,
    data_hora DATETIME NOT NULL,
    FOREIGN KEY (valoracio) REFERENCES valoracions_tipus(id)
);