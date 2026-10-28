import json
import os
import sys
import time

def generate_sarif_report(findings, output_path="results.sarif"):
    """
    Exports GemmaSentinel security findings into standard OASIS SARIF v2.1.0 format
    compatible with GitHub Code Scanning & Advanced Security tabs.
    """
    sarif_data = {
        "$schema": "https://raw.githubusercontent.com/oasis-tcs/sarif-spec/master/Schemata/sarif-schema-2.1.0.json",
        "version": "2.1.0",
        "runs": [
            {
                "tool": {
                    "driver": {
                        "name": "GemmaSentinel",
                        "version": "1.2.0",
                        "informationUri": "https://github.com/soumyadeepmagnusx/gemmasentinel2.O",
                        "rules": [
                            {
                                "id": "CWE-89",
                                "name": "SqlInjection",
                                "shortDescription": {
                                    "text": "SQL Injection Flaw in Database Query"
                                },
                                "defaultConfiguration": {
                                    "level": "error"
                                }
                            },
                            {
                                "id": "CWE-798",
                                "name": "HardcodedSecret",
                                "shortDescription": {
                                    "text": "Hardcoded Secret / API Token Detected"
                                },
                                "defaultConfiguration": {
                                    "level": "warning"
                                }
                            },
                            {
                                "id": "CWE-502",
                                "name": "InsecureDeserialization",
                                "shortDescription": {
                                    "text": "Insecure Deserialization (RCE Flaw)"
                                },
                                "defaultConfiguration": {
                                    "level": "error"
                                }
                            }
                        ]
                    }
                },
                "results": []
            }
        ]
    }
    
    for item in findings:
        sarif_result = {
            "ruleId": item.get("cwe", "CWE-89"),
            "level": "error" if item.get("severity") == "CRITICAL" else "warning",
            "message": {
                "text": f"[{item.get('cwe')}] {item.get('title')}: {item.get('remediation')}"
            },
            "locations": [
                {
                    "physicalLocation": {
                        "artifactLocation": {
                            "uri": item.get("file", "app.py")
                        },
                        "region": {
                            "startLine": item.get("line", 1)
                        }
                    }
                }
            ]
        }
        sarif_data["runs"][0]["results"].append(sarif_result)
        
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(sarif_data, f, indent=2)
        
    print(f"[+] Successfully exported {len(findings)} finding(s) to SARIF: {output_path}")

if __name__ == "__main__":
    sample_findings = [
        {
            "cwe": "CWE-89",
            "title": "SQL Injection via string concatenation",
            "severity": "CRITICAL",
            "remediation": "Use parameterized queries with Oracle/Postgres bind variables.",
            "file": "app.py",
            "line": 223
        },
        {
            "cwe": "CWE-798",
            "title": "Exposed API key token",
            "severity": "HIGH",
            "remediation": "Extract secret key to .env file.",
            "file": "app.py",
            "line": 196
        }
    ]
    out_file = sys.argv[1] if len(sys.argv) > 1 else "results.sarif"
    generate_sarif_report(sample_findings, out_file)
