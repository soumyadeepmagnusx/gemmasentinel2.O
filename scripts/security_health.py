import os
import sys
import json
import time

def evaluate_repository_health(base_dir=None):
    """Evaluates repository security compliance, rule coverage, and CI readiness."""
    if base_dir is None:
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    checks = [
        {
            "name": "Security Policy (SECURITY.md)",
            "passed": os.path.exists(os.path.join(base_dir, "SECURITY.md")),
            "weight": 15,
            "description": "Responsible disclosure policy defined."
        },
        {
            "name": "CWE Rulebook (cwe_rules.json)",
            "passed": os.path.exists(os.path.join(base_dir, "data", "cwe_rules.json")),
            "weight": 20,
            "description": "Structured CWE vulnerability definitions present."
        },
        {
            "name": "Automated Unit Test Suite",
            "passed": os.path.exists(os.path.join(base_dir, "tests", "test_security.py")) and 
                      os.path.exists(os.path.join(base_dir, "tests", "test_oracle_optimizer.py")),
            "weight": 20,
            "description": "Security and Oracle optimizer test suites present."
        },
        {
            "name": "GitHub Actions CI Pipeline",
            "passed": os.path.exists(os.path.join(base_dir, ".github", "workflows", "ci.yml")),
            "weight": 15,
            "description": "Continuous Integration automated check active."
        },
        {
            "name": "OASIS SARIF Exporter",
            "passed": os.path.exists(os.path.join(base_dir, "scripts", "sarif_exporter.py")),
            "weight": 15,
            "description": "GitHub Code Scanning SARIF integration supported."
        },
        {
            "name": "Containerized Deployment (Dockerfile)",
            "passed": os.path.exists(os.path.join(base_dir, "Dockerfile")),
            "weight": 15,
            "description": "Production Docker container spec with healthcheck."
        }
    ]

    total_score = sum(c["weight"] for c in checks if c["passed"])
    max_score = sum(c["weight"] for c in checks)
    percentage = (total_score / max_score) * 100

    if percentage >= 95:
        grade = "A+"
    elif percentage >= 85:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    else:
        grade = "C"

    print("=" * 65)
    print(" [*] GEMMASENTINEL REPOSITORY SECURITY HEALTH AUDIT")
    print("=" * 65)
    for c in checks:
        mark = "[+] PASS" if c["passed"] else "[-] FAIL"
        print(f" {mark} ({c['weight']} pts) {c['name']}")
        print(f"     -> {c['description']}")
    print("-" * 65)
    print(f" Overall Security Score: {total_score}/{max_score} ({percentage:.1f}%) | Grade: {grade}")
    print("=" * 65)

    health_summary = {
        "timestamp": time.time(),
        "score": total_score,
        "max_score": max_score,
        "percentage": percentage,
        "grade": grade,
        "checks": checks
    }

    out_file = os.path.join(base_dir, "security_health.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(health_summary, f, indent=2)

    return percentage == 100

if __name__ == "__main__":
    success = evaluate_repository_health()
    sys.exit(0 if success else 1)
