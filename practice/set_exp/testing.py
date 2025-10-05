def set_calculator():
    print("=== Set Theory Calculator ===")

    # Take user input for two sets
    A = set(input("Enter elements of Set A (comma separated): ").split(","))
    B = set(input("Enter elements of Set B (comma separated): ").split(","))

    print("\nSet A =", A)
    print("Set B =", B)

    while True:
        print("\nChoose an operation:")
        print("1. Union (A ∪ B)")
        print("2. Intersection (A ∩ B)")
        print("3. Difference (A - B)")
        print("4. Symmetric Difference (A Δ B)")
        print("5. Check Subset (A ⊆ B)")
        print("6. Check Superset (A ⊇ B)")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            print("Union:", A | B)
        elif choice == "2":
            print("Intersection:", A & B)
        elif choice == "3":
            print("Difference (A - B):", A - B)
        elif choice == "4":
            print("Symmetric Difference:", A ^ B)
        elif choice == "5":
            print("Is A a subset of B?", A.issubset(B))
        elif choice == "6":
            print("Is A a superset of B?", A.issuperset(B))
        elif choice == "7":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")
set_calculator()