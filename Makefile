.PHONY: install run scan sarif benchmark test clean

install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

run:
	streamlit run app.py

scan:
	python cli.py scan --file app.py

sarif:
	python scripts/sarif_exporter.py results.sarif

benchmark:
	python scripts/benchmark_eval.py

test:
	python -m unittest discover -s tests -v

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	rm -f results.sarif
