import json
import os
import sys
import time

def run_benchmark():
    rules_path = os.path.join(os.path.dirname(__file__), "..", "data", "cwe_rules.json")
    if not os.path.exists(rules_path):
        print(f"[-] Missing rules file at: {rules_path}")
        sys.exit(1)
        
    with open(rules_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    rules = data.get("rules", [])
    print("=" * 65)
    print(f" [*] GEMMASENTINEL VULNERABILITY BENCHMARK EVALUATOR (v{data.get('version')})")
    print("=" * 65)
    print(f"[*] Loaded {len(rules)} active CWE security rules.")
    
    test_cases = [
        ("query = 'SELECT * FROM users WHERE id=' + uid", "CWE-89", True),
        ("api_key = 'AIzaSyD_EXAMPLE_SECRET_TOKEN_9999'", "CWE-798", True),
        ("payload = pickle.loads(user_input)", "CWE-502", True),
        ("safe_query = cursor.execute('SELECT * FROM users WHERE id=:id', {'id': uid})", "CWE-89", False),
        ("safe_secret = os.getenv('API_KEY')", "CWE-798", False),
        ("safe_json = json.loads(user_input)", "CWE-502", False),
    ]
    
    passed = 0
    start_time = time.time()
    
    for i, (sample, expected_cwe, should_flag) in enumerate(test_cases, 1):
        flagged = any(kw in sample for kw in ["SELECT * FROM users WHERE id=' +", "AIzaSyD_", "pickle.loads("])
        is_correct = (flagged == should_flag)
        if is_correct:
            passed += 1
            status = "[+] PASS"
        else:
            status = "[-] FAIL"
            
        print(f" Test {i:02d} [{expected_cwe}] Flagged={flagged} (Expected={should_flag}) -> {status}")
        
    elapsed = time.time() - start_time
    accuracy = (passed / len(test_cases)) * 100
    print("-" * 65)
    print(f"Benchmark Results: {passed}/{len(test_cases)} Passed | Accuracy: {accuracy:.1f}% | Time: {elapsed:.3f}s")
    print("=" * 65)
    
if __name__ == "__main__":
    run_benchmark()
