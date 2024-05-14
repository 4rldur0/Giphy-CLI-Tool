poetry run black --check giphy_tool_project2/*.py && poetry run isort --check giphy_tool_project2/*.py && poetry run flake8 giphy_tool_project2/*.py && echo "Everything looks good"
