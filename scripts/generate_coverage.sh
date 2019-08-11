
#!/bin/bash -e

# generate_coverage.sh
# It generates an lcov.info and coverage report in ./coverage.

DIR=${1-'.'}

cd $DIR
rm -rf htmlcov
pip3 install -r requirements.txt
pytest
pytest tests/scraper_test.py --cov=newsdatascraper --cov-report html 
coverage report -m