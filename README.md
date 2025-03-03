<p align="center">
    <em>Resume Ranker</em>
</p>

<hr>

##  Quick Links

> - [ Overview](#-overview)
> - [ Repository Structure](#-repository-structure)
> - [ Modules](#-modules)
> - [ Getting Started](#-getting-started)
>   - [ Installation](#-installation)
>   - [ Running PRD_to_UserStories](#-running-PRD_to_UserStories)
> - [ Contributing](#-contributing)
> - [ License](#-license)
> - [ Acknowledgments](#-acknowledgments)

---

##  Overview

This project extracts key skills needed for a particular role from the given job description.

The extracted skills can be then used to evaluate potential candidates.

The tool takes the resumes of the candidates and scores the resume on a scale of 0-5 for each skill extracted in the previous step.

The total score for each candidate is calculated and this helps the recruiter identify the potential candidates.

---


##  Repository Structure

```sh
└── PRD_to_UserStories/
    ├── LICENSE
    ├── README.md
    ├── static
    |   └── swagger.json
    ├── app.py
    ├── candidate.py
    ├── extraction.py
    ├── match.py
    ├── utils.py
    └── requirements.txt
```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                                           | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---                                                                                            | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [feature_user.py](https://github.com/sashanksridhar/resume-ranker/blob/master/candidate.py)   | The `candidate.py` script within the `resume-ranker`repository is primarily intended to use an AI agent to extract the candidate's name from their resume.                                                                                                                                                   |
| [extraction.py](https://github.com/sashanksridhar/resume-ranker/blob/master/extraction.py)   | This script, `extraction.py`, is a component of the `resume-ranker` repository that is responsible for AI agents that extract key skill criteria from a given job description. Also summaries a skill point and identifies the key word to define in the output ranked csv.                                                         |
| [match.py](https://github.com/sashanksridhar/resume-ranker/blob/master/match.py)           | The `match.py`, is the main component of the `resume ranker` repository that has an AI agent that evaluates a resume based on the skill criteria and assigns scores between 0 and 5 for each criteria. |
| [requirements.txt](https://github.com/sashanksridhar/resume-ranker/blob/master/requirements.txt) | This codebase is primarily for ranking resumes based on skills extracted from a job description. The `requirements.txt` file lists dependencies that provide functionalities such as OpenAI SDK, PDF processing, docx processing, and other environment properties.               |
| [app.py](https://github.com/sashanksridhar/resume-ranker/blob/master/app.py)                     | This code in `app.py` serves as the core application interface in the `resume-ranker` repository. It contains the API definitions for the two main functionalities - 1. Extraction of skill criteria 2. Ranking of resumes.                  | 
| [utils.py](https://github.com/sashanksridhar/resume-ranker/blob/master/utils.py)                     | This code in `utils.py` provides file related utilities.  | 

</details>

---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version 3.9`

###  Installation

1. Clone the repository:

```sh
git clone https://github.com/sashanksridhar/resume-ranker/
```

2. Change to the project directory:

```sh
cd resume-ranker
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```
### LLM Keys
4. Set base_url and api_key for LLM host in `candidate.py`, `extraction.py` and `match.py`:
```
base_url="https://openrouter.ai/api/v1",
api_key=""
```
###  Running the application

Use the following command to run resume-ranker:

```sh
python app.py
```
---

### Swagger Docs

Access the swagger API docs at:
```
http://localhost:5000/api/docs/
```


##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Join the Discussions](https://github.com/sashanksridhar/resume-ranker/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/sashanksridhar/resume-ranker/issues)**: Submit bugs found or log feature requests for Prd_to_userstories.

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone hhttps://github.com/sashanksridhar/resume-ranker/
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

##  License

This project is protected under the [MIT LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---


[**Return**](#-quick-links)

---
