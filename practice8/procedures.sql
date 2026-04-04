-- Процедура insert или update
CREATE OR REPLACE PROCEDURE insert_or_update(p_name TEXT, phone_val TEXT)
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE username = p_name) THEN
        UPDATE phonebook
        SET phone = phone_val
        WHERE username = p_name;
    ELSE
        INSERT INTO phonebook(username, phone)
        VALUES (p_name, phone_val);
    END IF;
END;
$$ LANGUAGE plpgsql;

-- -------------------
-- Процедура bulk insert
CREATE OR REPLACE PROCEDURE bulk_insert(names TEXT[], phones TEXT[])
AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..array_length(names, 1)
    LOOP
        IF length(phones[i]) < 10 THEN
            RAISE NOTICE 'Invalid phone: %', phones[i];
        ELSE
            CALL insert_or_update(names[i], phones[i]);
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

-- -------------------
-- Процедура удаления
CREATE OR REPLACE PROCEDURE delete_user(value TEXT)
AS $$
BEGIN
    DELETE FROM phonebook
    WHERE username = value OR phone = value;
END;
$$ LANGUAGE plpgsql;