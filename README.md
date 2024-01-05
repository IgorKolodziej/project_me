# Project Me

## Description

Lecimy nie śpimy

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.11
- Poetry

### Installing

1. **Clone the repository**

```bash
git clone https://github.com/IgorKolodziej/project_me.git
cd your-repo-name
```

2. **Set up Python environment**

You need Python 3.11 installed on your system. You can download it from the official website:

https://www.python.org/downloads/

3. **Install Poetry**

Poetry is a tool for dependency management and packaging in Python. You can install it by running:

```bash
pip install poetry
```

4. **Install dependencies**

With Poetry installed, you can create a virtual environment with all necessary dependencies by running:

```bash
poetry install
```
##### Development
5. **Set up pre-commit**
Set up pre-commit hooks by running:
```bash
poetry run pre-commit install
```
This will install pre-commit hooks for you. Now, every time you commit a change, pre-commit will run the hooks on all files that you have changed.

You can run all pre-commit hooks on all files by running:

```bash
poetry run pre-commit run --all-files
```

## Running the tests

Explain how to run the automated tests for this system.

## Deployment

Add additional notes about how to deploy this on a live system.

## Built With

* Dash - The web framework used
* Plotly
* Pandas
* Poetry - Dependency Management
* Pre-commit - Git hooks manager

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Your Name** - *Initial work* - YourUsername

See also the list of contributors who participated in this project.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
