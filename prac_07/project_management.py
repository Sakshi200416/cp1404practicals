# project_management.py

import datetime
from project import Project

FILENAME = "projects.txt"


def main():
    """Main function to manage project menu and functionality."""
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    while True:
        print("\n- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")

        choice = input(">>> ").lower()
        if choice == 'l':
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == 's':
            filename = input("Enter filename to save projects to: ")
            save_projects(filename, projects)
            print(f"Projects saved to {filename}")
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            if input("Would you like to save to projects.txt? (yes/no): ").lower() == 'yes':
                save_projects(FILENAME, projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid option, please choose again.")


def load_projects(filename):
    """Load projects from a given filename and return a list of Project objects."""
    projects = []
    with open(filename, "r") as file:
        file.readline()  # Skip header
        for line in file:
            name, start_date, priority, cost_estimate, completion_percentage = line.strip().split("\t")
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    return projects


def save_projects(filename, projects):
    """Save a list of Project objects to a given filename."""
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    """Display completed and incomplete projects sorted by priority."""
    incomplete_projects = sorted([p for p in projects if not p.is_completed()])
    completed_projects = sorted([p for p in projects if p.is_completed()])

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")
    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Filter projects by start date entered by the user."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()

    filtered_projects = sorted([p for p in projects if p.start_date > filter_date], key=lambda p: p.start_date)
    for project in filtered_projects:
        print(project)


def add_project(projects):
    """Add a new project by asking user input for project details."""
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: ")
    completion_percentage = input("Percent complete: ")

    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)


def update_project(projects):
    """Update an existing project's completion percentage or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = int(input("Project choice: "))

    project = projects[project_choice]
    print(f"Updating {project}")

    new_completion = input("New Percentage: ")
    new_priority = input("New Priority: ")

    if new_completion:
        project.completion_percentage = int(new_completion)
    if new_priority:
        project.priority = int(new_priority)


if __name__ == "__main__":
    main()
