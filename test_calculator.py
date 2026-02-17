"""
Unit Tests for Calculator Module
Tests basic arithmetic operations to ensure correctness.
"""

from calculator import add

def test_addition():
    """Test that 2 + 2 equals 4"""
    result = add(2, 2)
    assert result == 4, f"Expected 4, but got {result}"
    print("✓ Test passed: 2 + 2 = 4")

def test_addition_negative():
    """Test addition with negative numbers"""
    result = add(-1, 1)
    assert result == 0, f"Expected 0, but got {result}"
    print("✓ Test passed: -1 + 1 = 0")

def test_addition_zero():
    """Test addition with zero"""
    result = add(5, 0)
    assert result == 5, f"Expected 5, but got {result}"
    print("✓ Test passed: 5 + 0 = 5")

def test_addition_large_numbers():
    """Test addition with large numbers"""
    result = add(1000000, 2000000)
    assert result == 3000000, f"Expected 3000000, but got {result}"
    print("✓ Test passed: 1000000 + 2000000 = 3000000")

def test_addition_negative_both():
    """Test addition with two negative numbers"""
    result = add(-5, -3)
    assert result == -8, f"Expected -8, but got {result}"
    print("✓ Test passed: -5 + -3 = -8")

def test_addition_floats():
    """Test addition with floating point numbers"""
    result = add(2.5, 3.7)
    expected = 6.2
    assert abs(result - expected) < 0.0001, f"Expected {expected}, but got {result}"
    print("✓ Test passed: 2.5 + 3.7 = 6.2")

def test_addition_mixed_signs():
    """Test addition with mixed positive and negative"""
    result = add(10, -3)
    assert result == 7, f"Expected 7, but got {result}"
    print("✓ Test passed: 10 + -3 = 7")

def test_addition_zero_both():
    """Test addition with both zeros"""
    result = add(0, 0)
    assert result == 0, f"Expected 0, but got {result}"
    print("✓ Test passed: 0 + 0 = 0")

def test_addition_commutative():
    """Test that addition is commutative (a + b = b + a)"""
    result1 = add(7, 13)
    result2 = add(13, 7)
    assert result1 == result2 == 20, f"Expected both to equal 20, but got {result1} and {result2}"
    print("✓ Test passed: Commutative property (7 + 13 = 13 + 7 = 20)")

def test_addition_multiple():
    """Test multiple additions in sequence"""
    result = add(add(1, 2), 3)
    assert result == 6, f"Expected 6, but got {result}"
    print("✓ Test passed: (1 + 2) + 3 = 6")

if __name__ == "__main__":
    test_addition()
    test_addition_negative()
    test_addition_zero()
    test_addition_large_numbers()
    test_addition_negative_both()
    test_addition_floats()
    test_addition_mixed_signs()
    test_addition_zero_both()
    test_addition_commutative()
    test_addition_multiple()
    print("\n✅ All tests passed!")
