DROP TABLE IF EXISTS phonebook;
DROP FUNCTION IF EXISTS search_pattern(TEXT);
DROP FUNCTION IF EXISTS get_paginated(INT, INT);
DROP PROCEDURE IF EXISTS insert_or_update(TEXT, TEXT);
DROP PROCEDURE IF EXISTS bulk_insert(TEXT[], TEXT[]);
DROP PROCEDURE IF EXISTS delete_user(TEXT);

-- Таблица
CREATE TABLE phonebook (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL
);

-- -------------------
-- Функция поиска по шаблону
CREATE OR REPLACE FUNCTION search_pattern(p_pattern TEXT)
RETURNS TABLE(id INT, username VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT t.id, t.username, t.phone
    FROM phonebook t
    WHERE t.username ILIKE '%' || p_pattern || '%'
       OR t.phone ILIKE '%' || p_pattern || '%';
END;
$$ LANGUAGE plpgsql;

-- -------------------
-- Функция пагинации
CREATE OR REPLACE FUNCTION get_paginated(limit_val INT, offset_val INT)
RETURNS TABLE(id INT, username VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT t.id, t.username, t.phone
    FROM phonebook t
    ORDER BY t.id
    LIMIT limit_val OFFSET offset_val;
END;
$$ LANGUAGE plpgsql;