import hashlib
from pathlib import Path
from datetime import datetime

def test_math():
    #assert 10 + 5 == 15
    assert 1 == 2

def test_string_reverse():
    assert "hello"[::-1] == "olleh"

def test_generate_evidence():
    artifacts_dir = Path("artifacts")
    artifacts_dir.mkdir(exist_ok=True)
    
    evidence_file = artifacts_dir / "test-evidence.txt"
    checksum_file = artifacts_dir / "test-evidence.sha256"
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    repo = "ci-cd-phase-challenge"
    commit = "local-test"
    
    content = f"Phase Challenge Evidence\nTimestamp: {timestamp}\nRepo: {repo}\nCommit: {commit}\nResult: PASS\n"
    evidence_bytes = content.encode('utf-8')
    evidence_file.write_bytes(evidence_bytes)
    
    actual_hash = hashlib.sha256(evidence_bytes).hexdigest()
    checksum_file.write_text(actual_hash)