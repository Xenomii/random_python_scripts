def main():
    extract_rockyou = open("../text_files/extracted_rockyou.txt", "w", errors="ignore")
    with open("../text_files/rockyou.txt", "r", errors="ignore") as rockyou_open:
        for line in rockyou_open:
            if len(line) >= 5 and len(line) <= 9:
                extract_rockyou.write(line)


if __name__ == "__main__":
    main()