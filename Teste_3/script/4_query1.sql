SELECT d.registro_ans, o.razao_social, SUM(d.vl_saldo_final) AS total_despesas
FROM demonstracoes_contabeis d
JOIN operadoras o ON d.registro_ans = o.registro_ans
WHERE d.descricao ILIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADO%'
AND d.data BETWEEN DATE '2024-10-01' AND DATE '2024-12-31'
GROUP BY d.registro_ans, o.razao_social
ORDER BY total_despesas DESC
LIMIT 10;

