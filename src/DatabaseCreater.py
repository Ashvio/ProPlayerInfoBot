from src.DatabaseManager import DatabaseManager, load_db

if __name__ == "__main__":
    print("Building database...", end = "")
    manager = DatabaseManager()
    print("[DONE]")
    print("Finding videos...")
    manager.find_videos()
    print("[DONE]")

    print("Saving database...", end = "")
    manager.save_db("../Databases/dict-2-25-16.db")
    print("[DONE]")
    print("Exiting...")