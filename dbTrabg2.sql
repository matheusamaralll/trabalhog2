create database trabg2;
create user trabg2 identified by '12345';
grant all on trabg2.* to trabg2;
use trabg2;

CREATE TABLE resume (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(120) UNIQUE NOT NULL,
    endereco_web VARCHAR(120),
    experiencia_profissional TEXT NOT NULL
);
describe resume;
select * from resume;