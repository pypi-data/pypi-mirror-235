# Translator UI Test Runner
This testing framework performs UI Pass/Fail analysis on queries it receives from the Translator Test Harness.

## Installation
`pip install ui-test-runner`

## Usage
```python
from ui_test_runner import run_ui_test
report = run_ui_test(<env>, <query_type>, <expected_output>, <input_curie>, <output_curie>)
```

**Arguements**:
- env: the environment to run the queries against. (dev, ci, test, prod)
- query_type: type of query to test. (treats(creative), upregulates, downregulates)
- expected_output: whether the output curie is good or bad. (TopAnswer, Acceptable, BadButForgivable, NeverShow)
- input_curie: curie used in the initial query.
- output_curie: curie checked for in the results
