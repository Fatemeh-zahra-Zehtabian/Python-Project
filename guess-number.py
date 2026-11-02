import random

print("به بازی حدس اعداد خوش آمدید!")

while True:
    secret_number = random.randint(1, 100)
    attempts = 0
    won = False

    print("\nیک عدد بین 1 تا 100 انتخاب شده است.")
    print("شما 5 فرصت برای حدس زدن دارید.")

    while attempts < 5:
        try:
            guess = int(input("\nحدس خود را وارد کنید: "))
        except ValueError:
            print("ورودی نامعتبر است! لطفاً یک عدد صحیح وارد کنید.")
            continue

        if guess < 1 or guess > 100:
            print("عدد باید بین 1 تا 100 باشد.")
            continue

        attempts += 1

        print("\nتلاش", attempts, "از 5")
        print("فرصت باقی‌مانده:", 5 - attempts)

        if guess == secret_number:
            won = True
            print("\nتبریک! عدد را درست حدس زدید.")

            if attempts == 1:
                print("رتبه شما: نمونه ای")
            elif attempts == 2:
                print("رتبه شما: بسیار خوبی")
            elif attempts == 3:
                print("رتبه شما: خوب")
            elif attempts == 4:
                print("رتبه شما: قبول")
            else:
                print("رتبه شما: با شانس بردی!")

            break

        difference = abs(secret_number - guess)

        if guess < secret_number:
            print("بزرگ‌تر وارد کن.")
        else:
            print("کوچک‌تر وارد کن.")

        if difference <= 5:
            print("خیلی نزدیکی!")
        elif difference <= 15:
            print("نزدیکی، ولی هنوز فاصله داری!")
        else:
            print("خیلی دوری!")

    if not won:
        print("\nمتأسفانه شما برنده نشدید!")
        print("عدد مخفی این بود:", secret_number)

    answer = input("\nآیا می‌خواهید دوباره بازی کنید؟ (بله/خیر): ").strip()

    while answer != "بله" and answer != "خیر":
        print("پاسخ نامعتبر است! لطفاً بله یا خیر وارد کنید.")
        answer = input("آیا می‌خواهید دوباره بازی کنید؟ ").strip()

    if answer == "خیر":
        print("\nاز اینکه بازی کردید متشکریم!")
        break