from app.database import create_table

def main():
    create_table()
    print("Table created or already exists.")

if __name__ == "__main__":
    main()