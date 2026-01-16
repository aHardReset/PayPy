"""
Database repository with utility functions to get raw data.
Students will use these functions to build business logic.
"""
import database


def get_user_by_id(user_id: int) -> dict | None:
    """
    Get user information by ID.
    Returns dict with user data or None if not found.

    Example return:
    {
        'id': 1,
        'legal_name': 'John Doe',
        'nickname': 'johnd',
        'country_id': 1
    }
    """
    conn = database.get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, legal_name, nickname, country_id
        FROM users
        WHERE id = ?
    """, (user_id,))

    row = cursor.fetchone()
    conn.close()

    if row is None:
        return None

    return {
        'id': row[0],
        'legal_name': row[1],
        'nickname': row[2],
        'country_id': row[3]
    }


def get_all_transactions_for_user(user_id: int) -> list[dict]:
    """
    Get all transactions for a user.
    Returns list of transaction dicts.

    Example return:
    [
        {
            'id': 1,
            'user_id': 1,
            'sender_id': None,
            'recipient_id': 1,
            'amount': 1000.0,
            'note': 'Depósito inicial',
            'created_at': '2024-01-16 10:00:00'
        },
        ...
    ]
    """
    conn = database.get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, user_id, sender_id, recipient_id, amount, note, created_at
        FROM transactions
        WHERE user_id = ?
        ORDER BY created_at DESC
    """, (user_id,))

    rows = cursor.fetchall()
    conn.close()

    return [
        {
            'id': row[0],
            'user_id': row[1],
            'sender_id': row[2],
            'recipient_id': row[3],
            'amount': row[4],
            'note': row[5],
            'created_at': row[6]
        }
        for row in rows
    ]


def get_country_by_id(country_id: int) -> dict | None:
    """
    Get country information by ID.
    Returns dict with country data or None if not found.

    Example return:
    {
        'id': 1,
        'country_code': 'US',
        'country_name': 'Estados Unidos'
    }
    """
    conn = database.get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, country_code, country_name
        FROM countries
        WHERE id = ?
    """, (country_id,))

    row = cursor.fetchone()
    conn.close()

    if row is None:
        return None

    return {
        'id': row[0],
        'country_code': row[1],
        'country_name': row[2]
    }
