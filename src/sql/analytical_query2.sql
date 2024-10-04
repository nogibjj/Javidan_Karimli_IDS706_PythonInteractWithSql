SELECT 
    Federation,
    COUNT(*) as cnt

FROM ChessTransfersFormatted
GROUP BY 
    Federation
ORDER BY cnt DESC 
LIMIT 1