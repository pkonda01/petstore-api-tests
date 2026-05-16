"""
pytest configuration and fixtures for LCF tests.
This file automatically imports user-defined assertions to ensure they're
available during test execution.
"""

# Import user-defined custom assertions to register them with LCF framework
# This ensures they're available when the LCF test runner executes
try:
    from assertion.user_defined_assertion import *
    print("✅ Custom assertions loaded successfully")
except ImportError as e:
    print(f"⚠️  Custom assertions not found: {e}")
    # Don't fail if custom assertions aren't available
    pass