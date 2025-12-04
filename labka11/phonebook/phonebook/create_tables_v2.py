import psycopg2
from config import load_config

SQL_OBJECTS = [

#удаляееем старые процеДУРКИ и ФУнкции
"""
DROP FUNCTION IF EXISTS search_contacts(text) CASCADE;
DROP FUNCTION IF EXISTS paginate_contacts(int, int) CASCADE;
DROP FUNCTION IF EXISTS add_many_users(text[], text[]) CASCADE;
DROP PROCEDURE IF EXISTS add_or_update_user(text, text) CASCADE;
DROP PROCEDURE IF EXISTS delete_contact(text, text) CASCADE;
""",
#тут типикал создаем табличку и даем им дэйта тайп
"""
CREATE TABLE IF NOT EXISTS contacts (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    phone VARCHAR(20) UNIQUE NOT NULL
);
""",
# ФУнкция находим данные по ключевым частям данных
"""
CREATE OR REPLACE FUNCTION search_contacts(pattern TEXT)
RETURNS TABLE (
    id INT,
    first_name TEXT,
    phone TEXT
)
AS $$
BEGIN
    RETURN QUERY
    SELECT 
        c.id,
        c.first_name::TEXT,
        c.phone::TEXT
    FROM contacts c
    WHERE c.first_name ILIKE '%' || pattern || '%'
       OR c.phone      ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;
""",
# процеДУРКА ввод и обновка юзера по имении если существиет
"""
CREATE OR REPLACE PROCEDURE add_or_update_user(
    p_name TEXT,
    p_phone TEXT
)
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE first_name = p_name) THEN
        UPDATE contacts 
        SET phone = p_phone
        WHERE first_name = p_name;
    ELSE
        INSERT INTO contacts(first_name, phone)
        VALUES (p_name, p_phone);
    END IF;
END;
$$ LANGUAGE plpgsql;
""",
#ФУнция ввод всех ОГРомное кол юзеров и возвращяет неправильный номерочек фона
"""
CREATE OR REPLACE FUNCTION add_many_users(
    names TEXT[],
    phones TEXT[]
)
RETURNS TEXT[]
AS $$
DECLARE
    invalid TEXT[] := '{}';
    i INT;
BEGIN
    FOR i IN 1 .. array_length(names, 1) LOOP
        IF phones[i] !~ '^[0-9+()-]+$' THEN
            invalid := array_append(invalid, phones[i]);
            CONTINUE;
        END IF;

        IF EXISTS (SELECT 1 FROM contacts WHERE first_name = names[i]) THEN
            UPDATE contacts
            SET phone = phones[i]
            WHERE first_name = names[i];
        ELSE
            INSERT INTO contacts(first_name, phone)
            VALUES (names[i], phones[i]);
        END IF;
    END LOOP;

    RETURN invalid;
END;
$$ LANGUAGE plpgsql;
""",
#ФУнкция страничек
"""
CREATE OR REPLACE FUNCTION paginate_contacts(p_limit INT, p_offset INT)
RETURNS TABLE(
    contact_id INT,
    first_name TEXT,
    phone TEXT
)
AS $$
BEGIN
    RETURN QUERY
    SELECT 
        c.id AS contact_id,
        c.first_name::TEXT,
        c.phone::TEXT
    FROM contacts c
    ORDER BY c.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;
""",
#процеДУРКА удаляем юзера из группы крутые деффчонки по имени или номеру
"""
CREATE OR REPLACE PROCEDURE delete_contact(p_name TEXT, p_phone TEXT)
AS $$
BEGIN
    IF p_name IS NOT NULL THEN
        DELETE FROM contacts WHERE first_name = p_name;
    END IF;

    IF p_phone IS NOT NULL THEN
        DELETE FROM contacts WHERE phone = p_phone;
    END IF;
END;
$$ LANGUAGE plpgsql;
"""
]

def create_tables():
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for sql in SQL_OBJECTS:
                    cur.execute(sql)
                conn.commit()
                print("All tables, functions, and procedures created successfully.")
    except Exception as e:
        print("Error installing SQL:", e)

if __name__ == "__main__":
    create_tables()
