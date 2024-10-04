SELECT 
    Form_Fed, 
    Federation, 
    COUNT(*) AS num_switches
FROM 
    ChessTransfersFormatted
GROUP BY 
    Form_Fed, 
    Federation
ORDER BY 
    num_switches DESC