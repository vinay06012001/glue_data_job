def process_data():
    data = [10, 20, 30, 40, 50]
    result = [x * 2 for x in data]
    return result


if __name__ == "__main__":
    print("Glue job started")
    print(process_data())
    print("Glue job completed successfully")
    print("new version")