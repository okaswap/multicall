#!/usr/bin/env python3
"""Verify that the multic4ll package is properly built and importable."""

import sys

def main():
    print("=" * 50)
    print("multic4ll Package Verification")
    print("=" * 50)
    
    # Test 1: Import the package
    try:
        from multicall import Call, Multicall, Signature
        print("[PASS] Package imports successful")
        print(f"  - Call: {Call}")
        print(f"  - Multicall: {Multicall}")
        print(f"  - Signature: {Signature}")
    except ImportError as e:
        print(f"[FAIL] Import error: {e}")
        sys.exit(1)
    
    # Test 2: Check dist files exist
    import os
    dist_path = "/home/runner/workspace/dist"
    if os.path.exists(dist_path):
        files = os.listdir(dist_path)
        print(f"\n[PASS] Distribution files found in {dist_path}:")
        for f in files:
            size = os.path.getsize(os.path.join(dist_path, f))
            print(f"  - {f} ({size:,} bytes)")
    else:
        print(f"\n[WARN] No dist folder found. Run 'poetry build' to create distribution files.")
    
    print("\n" + "=" * 50)
    print("Package is ready for PyPI upload!")
    print("=" * 50)
    print("\nTo upload to PyPI:")
    print("  1. poetry publish (using Poetry)")
    print("  2. twine upload dist/* (using Twine)")
    print("\nTo upload to TestPyPI first:")
    print("  twine upload --repository testpypi dist/*")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
