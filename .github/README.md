# buildboquet .github/ directory

Contains configuration files and scripts used to manage the buildbouquet repository.

## .github/terraform

Contains terraform code used to manage the buildbouquet repository. 

## .github/workflows

Contains github actions workflows used to manage the buildbouquet repository.

### .github/workflows/chatgpt-code-revew.yaml

This workflow is triggered when a pull request is opened against the main branch. It runs the following steps:

1. Checkout the code
2. Install dependencies
3. Run the code review script to check for code quality issues using ChatGPT and report them as comments on the pull request.
