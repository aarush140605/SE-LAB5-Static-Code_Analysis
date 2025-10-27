1.	Which issues were the easiest to fix, and which were the hardest? Why?
ANS) The easiest issues to fix were issues whitespace, blank lines, line length which didnt need much work just deleting and formatting. The hardest was fixing the mutable default argument (logs=[]) because it required understanding Python's default argument evaluation behavior and restructuring the function logic.

2.	Did the static analysis tools report any false positives? If so, describe one example.
ANS) no false positives

3.	How would you integrate static analysis tools into your actual software development workflow? Consider continuous integration (CI) or local development practices.
ANS) integrate flake8/pylint/bandit into GitHub Actions and my development workflow to automatically check for errors and fix it.

4.	What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
ANS) The code became significantly more readable with proper naming conventions and proper exception handling. Security improved by removing eval() and adding specific exception handling, while maintainability increased through context managers for file operations.