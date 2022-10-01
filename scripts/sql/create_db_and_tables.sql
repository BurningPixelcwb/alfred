CREATE TABLE IF NOT EXISTS categoria(
	id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nome_categoria VARCHAR(100),
    situacao VARCHAR(2),
    date_up TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    date_down TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS subcategoria(
	id_subcategoria INT AUTO_INCREMENT PRIMARY KEY,
    nome_subcategoria VARCHAR(100),
    fk_id_categoria INT,
    FOREIGN KEY (fk_id_categoria) REFERENCES categoria(id_categoria),
	date_up TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    date_down TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS conta(
	id_conta INT AUTO_INCREMENT PRIMARY KEY,
    nome_conta VARCHAR(255),
    situacao VARCHAR(2),
	date_up TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    date_down TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS tipo_transacao(
	id_tp_transacao INT AUTO_INCREMENT PRIMARY KEY,
    nome_tp_transacao VARCHAR(255),
    situacao VARCHAR(2),
	date_up TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    date_down TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS transacao(
	  id_transacao INT AUTO_INCREMENT PRIMARY KEY
    , url_nfe LONGTEXT
    , estabelecimento VARCHAR(255)
    , endereco_compra longtext
    , dt_ticket datetime(6)
    , dt_lancamento datetime(6)
    , situacao VARCHAR(2)
    , fk_id_conta int(11)
    , fk_id_sub_categoria int(11)
    , fk_id_tp_transacao int(11)
    /*, FOREIGN KEY (fk_id_conta) REFERENCES conta(id_conta)
    , FOREIGN KEY (fk_id_sub_categoria) REFERENCES subcategoria(id_subcategoria)
    , FOREIGN KEY (fk_id_tp_transacao) REFERENCES tipo_transacao(id_tp_transacao)*/
	, date_up TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    , date_down TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ticket(
	  id_ticket INT AUTO_INCREMENT PRIMARY KEY
	, cod_prod int(11)
    , item_comprado varchar(155)
    , quantidade decimal(5,2)
    , medida varchar(15)
    , preco decimal(15,2)
    , valor_total decimal(15,2)
    , fk_id_transacao int(11)
    , FOREIGN KEY (fk_id_transacao) REFERENCES transacao(id_transacao)
	, date_up TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    , date_down TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- drop database alfred_db