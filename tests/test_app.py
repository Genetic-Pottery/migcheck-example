import app


def test_create_and_get_user(conn):
    user_id = app.create_user(conn, "Ada O'Brien", "ada@example.com")
    assert app.get_user(conn, user_id)[1] == "Ada O'Brien"


def test_rename_user(conn):
    user_id = app.create_user(conn, "Grace", "grace@example.com")
    app.rename_user(conn, user_id, "Grace Hopper")
    assert app.get_user(conn, user_id)[1] == "Grace Hopper"


def test_order_history(conn):
    user_id = app.create_user(conn, "Alan", "alan@example.com")
    app.place_order(conn, user_id, 1200)
    app.place_order(conn, user_id, 450)
    assert [row[1] for row in app.order_history(conn, user_id)] == [1200, 450]
