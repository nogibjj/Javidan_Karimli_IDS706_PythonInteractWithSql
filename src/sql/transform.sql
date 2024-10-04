CREATE TABLE {table_name} AS
SELECT 
    CAST(ID as int) as ID,
    url,
    Federation,
    Form_Fed,
    -- Convert 'MM/DD/YY' to 'YYYY-MM-DD' using SQLite's date function
    date('20' || substr(Transfer_Date, 7, 2) || '-' || 
            substr(Transfer_Date, 1, 2) || '-' || 
            substr(Transfer_Date, 4, 2)) AS Transfer_Date
FROM ChessTransfer;
