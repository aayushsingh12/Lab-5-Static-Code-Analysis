reflection.md

1. Which issues were the easiest to fix, and which were the hardest? Why?

    The easiest issue to fix was the bare except clause — it only required specifying the exact exception type (KeyError), which improved clarity and prevented silent error handling.

    The hardest issue was the global variable usage, since it required refactoring the function structure to pass variables explicitly (like stock_data) rather than relying on implicit global state. This change needed careful adjustment across all function calls.

2. Did the static analysis tools report any false positives? If so, describe one example.

    Yes, there was a minor false positive where the tool flagged a blank line warning between function definitions, even though it adhered to acceptable PEP 8 formatting. This didn’t affect functionality or readability but still appeared in the analysis results.

3. How would you integrate static analysis tools into your actual software development workflow?

    I would integrate static analysis tools like pylint or flake8 into a Continuous Integration (CI) pipeline, so every commit is automatically checked before merging.

    Additionally, I’d configure these tools to run locally via pre-commit hooks, ensuring style and logic errors are caught before pushing code to the repository.

4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

    The code became more modular and testable after removing global variables. Adding explicit exception handling made the system more robust and predictable. The inclusion of type checks and docstrings enhanced readability and maintainability.

    Overall, the code is now cleaner, less error-prone, and easier for another developer to understand or extend.
