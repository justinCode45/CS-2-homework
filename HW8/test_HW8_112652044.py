from HW8_112652044 import rail_Encrypt, rail_Decrypt
def test_rail_Decrypt():
    # Test case 1
    num = 3
    plain = "Hello, World!"
    assert rail_Decrypt(rail_Encrypt(plain, num), num) == plain
    # Test case 2
    num = 4
    plain = "Hello, World!"
    assert rail_Decrypt(rail_Encrypt(plain, num), num) == plain
    # Test case 3
    num = 5
    plain = "Hello, World!"
    assert rail_Decrypt(rail_Encrypt(plain, num), num) == plain

    # Test case 4
    num = 3
    plain = "Hello, World! This is a test."
    assert rail_Decrypt(rail_Encrypt(plain, num), num) == plain

    print("all test cases passed!")
    
test_rail_Decrypt()