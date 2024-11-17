# Quality Assurance Learning Plan
This is a rough guide for learning the QA Role designed to be supplemental to efforts you may be making in a class or job.

## Table of Contents
* [Learning How to Learn](#learning-how-to-learn)
* [Learning Each Technology Individually](#learning-each-technology-individually)
* [Learning QA Concepts](#learning-qa-concepts)
* [Learning about Project Management](#learning-about-project-management)
* [A Word about Burnout](#a-word-about-burnout)

## Learning how to Learn
Learning is a fundamental skill in tech that can be cultivated- the more you develop this skill, the more successful you will become.

One of the foundational pillars of successful learning is breaking complex problems down into simpler problems. This can help when learning a new skill, being presented with a new project at work, or even considering your long term career plans.

As an example, I recommend learning SQL before trying to use SQL in Python scripting to access a database. Python and SQL are two different technologies that are complementary, and yet we can practice them individually so that we don't get overwhelmed. A skilled Engineer might for example make sure their SQL query is thoroughly tested before trying to use it with a programming language they are unfamiliar with.

It is also very helpful to build a 'Network of Mentors'- folks who are themselves continuously learning and publishing what they learn for the benefit of their network.

## Learning each Technology Individually
These are arranged roughly in order of which thing you should learn first before moving on to the next:
1. [Learn Integrated Development Environments (IDE): Setting Up an IDE](https://medium.com/swlh/setting-up-an-ide-94677d12eaa9)
2. [Learn Code Concepts First: Free Codecademy Scripting Course](https://www.codecademy.com/learn/learn-how-to-code)
3. [Learn SQL in Isolation: SQL Zoo](https://sqlzoo.net/wiki/SQL_Tutorial)
4. [Learn Terminal in Isolation: Online Terminal](https://www.tutorialspoint.com/linux_terminal_online.php)
5. [Learn Python in Isolation: Online Python](https://www.online-python.com/)
6. Learn about Databases using Python + SQLite: Try to recreate some of the examples from SQL Zoo using the Python code in this Repo.
7. [Check out the Chrome Dev Tools](https://developer.chrome.com/docs/devtools)
8. [Learn Selenium with Python: python-selenium Tutorial](https://selenium-python.readthedocs.io/) - Also check out the learn_selenium.py script in this Repo.
9. [Learn Selenium IDE: Tutorial by Joe Colantonio (Includes a Podcast Episode)](https://testguild.com/selenium-ide-guide/)
10. [Advanced: Use Selenium to Write Tests for Weather Shopper](https://weathershopper.pythonanywhere.com/)
11. Many Frameworks include the ability to code different levels of testing directly into the Framework. For example, Django/Django REST Framework (A Python Backend Framework) [has a Client](https://docs.djangoproject.com/en/5.1/topics/testing/tools/) that can be used to test backend APIs directly. Flutter (a Frontend Framework) [can simulate button presses in the UI](https://docs.flutter.dev/cookbook/testing/integration/introduction). Consider digging into the Framework the dev team is using and see if you can partner with them to make your job easier.

## Learning QA Concepts
A big list of key concepts and one-liners on them.

### Planning
* **Test Plan:** A document outlining the testing strategy, objectives, schedule, resources, and scope for a project.
* **Test Scenario:** A high-level description of what to test, focusing on the end-to-end functionality of a feature.
* **Priority:** The order in which a defect should be fixed based on business or project needs.
* **Severity:** The impact level of a defect on the application's functionality.
* **Bug Lifecycle:** The process of a bug moving through various states, from identification to closure.
* **Definition of Done (DOD):** A shared understanding within the team of what it means for a task or user story to be considered complete. It typically includes passing all tests, meeting acceptance criteria, and being reviewed by stakeholders.
* **Sprint:** A set period during which specific project work must be completed and made ready for review.
* **Epic:** A large user story that is broken down into smaller, more manageable user stories. Epics often span multiple sprints and are used to track bigger features or requirements.
* **User Story:** A brief description of a feature from the perspective of the end-user, outlining what they need and why.
* **Backlog:** A prioritized list of tasks or features that need to be completed in a project. In Agile, the backlog is maintained by the Product Owner and can contain both user stories and bug fixes.
* **Acceptance Criteria:** Specific conditions that a product or feature must satisfy to be considered complete. These are defined for each user story to ensure the feature works as intended.
* **Burndown Chart:** A visual representation of the work completed versus the work remaining in a sprint. It helps teams track progress and ensure they are on track to complete all planned work within the sprint.
* **Requirement:** 	A detailed description of what a system must do to meet the needs of users or stakeholders.

### CI/CD
* **Continuous Integration/Continuous Testing (CI/CT):** Automated testing integrated into the development pipeline to ensure immediate feedback on code changes.
* **Continuous Integration/Continuous Deployment (CI/CD):** Automated integrationg and deployment of code changes to users.

### Test Types
* **Test Case:** A detailed set of actions, input data, and expected outcomes used to verify specific functionalities of a system.
* Test Suite:** A collection of test cases grouped together to validate a specific module or feature.
* **Defect/Bug:** A flaw or error in software that causes it to produce incorrect or unexpected results.
* **Regression Testing:** A process to verify that changes in the code have not adversely affected existing functionality.
* **Smoke Testing:** A preliminary test to check whether the basic and critical functionalities of the application are working.
* **Sanity Testing:** A quick evaluation to ensure that a specific function or bug fix is working as intended.
* **Unit Testing:** Testing individual components or modules of the software in isolation.
* **Integration Testing:** Testing the interactions between integrated modules or components to ensure they work together.
* **System Testing:** A comprehensive test of the complete system to verify that it meets the specified requirements.
* **User Acceptance Testing (UAT):** The final testing phase where end users validate the software against their requirements.
* **Performance Testing:** Testing to determine the speed, responsiveness, and stability of the software under a given workload.
* **Load Testing:** Assessing how the software behaves under expected user load.
* **Stress Testing:** Evaluating the system's performance under extreme conditions, beyond normal operational capacity.
* **Usability Testing:** Testing to ensure that the software is user-friendly and intuitive for end users.
* **Security Testing:** Identifying vulnerabilities and ensuring the application is protected from malicious attacks.
* **Exploratory Testing:** Ad hoc testing where testers explore the application without predefined test cases.
* **Test Automation:** Using tools and scripts to execute tests automatically, saving time and improving repeatability.
* **Test Coverage:** A metric that measures the extent to which the application is tested, typically expressed as a percentage.
* **Test Environment:** The setup of hardware, software, and configurations where testing is conducted.
* **Static Testing:** Reviewing and analyzing code, documents, or requirements without executing the program.
* **Dynamic Testing:** Validating the software's behavior by executing the application with test cases.
* **White Box Testing:** Testing internal structures or workings of an application, often done by developers.
* **Black Box Testing:** Testing the application without knowledge of its internal code or structures, focusing on inputs and outputs.
* **Grey Box Testing:** A hybrid testing approach that involves partial knowledge of internal structures combined with external testing.

## Learning about Project Management
Every Company will have their own Processes.

It's important to have a surface level understanding of the industry trends so that you know where to look when you encounter them at work.

When you join a Company and work in a Role, you will find that you have Inputs and Outputs. The goal is to be able to translate your Inputs into effective Outputs- sometimes the system works to help you and sometimes the system will hinder you. See the section below on Burnout, as it can sometimes be related.

**Types of Project Management:**
1. [Waterfall (Deprecated, but still used in some Industry)](https://asana.com/resources/waterfall-project-management-methodology)
2. [Agile (Industry Standard)](https://www.davefarley.net/?page_id=16)
    * Check out the original [Agile Manifesto](https://agilemanifesto.org/).
3. [ShapeUp (Good for Startups/Small Companies- my personal Favorite)](https://basecamp.com/shapeup)
4. [Scrum](https://www.scrum.org/resources/what-scrum-module)
5. [Kanban](https://asana.com/resources/what-is-kanban)
6. There are many systems, but the most important thing to take away from this is that the right system is the one that is working for your team.

## A Word about Burnout
It is incredibly easy to burn yourself out in tech, and many, many folks experience this issue. You are not alone if you do experience this.

83% of Developers Suffer From Burnout, according to a [Haystack Analytics study](https://www.usehaystack.io/blog/83-of-developers-suffer-from-burnout-haystack-analytics-study-finds).

This is why it is so important to find balance. The profession is very rewarding, but remember that it is a Marathon, not a Sprint. Our profession is still relatively young compared to many others, with so much change.

When you find yourself getting very frustrated, take a break and shift focus for a bit- make some tea, exercise, take care of yourself. Spend time with family and loved ones. Be social.

**There are many constant sources of pressures in our lives, and so it is up to us to advocate for ourselves.**