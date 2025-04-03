DROP TABLE IF EXISTS tmp_demonstracoes_contabeis;

CREATE TEMP TABLE tmp_demonstracoes_contabeis (
    data TEXT,
    registro_ans TEXT,
    cd_conta_contabil TEXT,
    descricao TEXT,
    vl_saldo_inicial TEXT,
    vl_saldo_final TEXT
);

COPY tmp_demonstracoes_contabeis
FROM'C:\\temp\\1T2024.csv'
WITH (FORMAT CSV, DELIMITER ';', HEADER, QUOTE '"');

INSERT INTO operadoras (registro_ans, cnpj, razao_social, nome_fantasia, modalidade)
SELECT DISTINCT registro_ans::INTEGER, '00000000000000', 'Operadora Desconhecida', 'Desconhecida', 'Desconhecida'
FROM tmp_demonstracoes_contabeis 
WHERE registro_ans::INTEGER NOT IN (SELECT registro_ans FROM operadoras);

INSERT INTO demonstracoes_contabeis (
    data, registro_ans, cd_conta_contabil, descricao, 
    vl_saldo_inicial, vl_saldo_final
)
SELECT 
    data::DATE, 
    registro_ans::INT,
    cd_conta_contabil, 
    descricao, 
    REPLACE(vl_saldo_inicial, ',', '.')::NUMERIC, 
    REPLACE(vl_saldo_final, ',', '.')::NUMERIC  
FROM tmp_demonstracoes_contabeis;
