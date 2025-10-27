from db import insert_user, get_users, update_user, delete_user, create_table

def run_tests():
    create_table()
    insert_user("Taras", 7)
    insert_user("Yehor", 39)

    users = get_users()
    assert len(users) >= 2
    print("Insert test passed.")

    user_id = users[0][0]
    update_user(user_id, "Taras Updated", 8)

    updated_users = get_users()
    updated_user = next((u for u in updated_users if u[0] == user_id), None)
    assert updated_user is not None, "Updated user not found"
    assert updated_user[1] == "Taras Updated"
    print("Update test passed.")

    delete_user(user_id)
    users_after_delete = get_users()
    assert not any(user[0] == user_id for user in users_after_delete)
    print("Delete test passed.")

if __name__ == "__main__":
    print("Running database tests...")
    run_tests()
    print("All tests passed successfully")