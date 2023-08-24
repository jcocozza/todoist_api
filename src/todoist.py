from todoist_api_python.api import TodoistAPI
from todoist_api_python.models import Section, Project, Task, Comment
class TodoistApi:
    """
    Class for handling API interactions
    """

    def __init__(self, token: str) -> None:
        """
        :param token: The API token for your todoist account
        """
        self.api = TodoistAPI(token)

    def get_projects(self) -> list[Project]:
        """
        Get all projects

        :returns list of projects:
        """
        try:
            projects = self.api.get_projects()
            return projects
        except Exception as error:
            raise(error)

    def create_project(self, project_name: str) -> None:
        """
        Create a todoist project

        :param project_name: The name of the project
        """
        try:
            project = self.api.add_project(name=project_name)
        except Exception as error:
            raise(error)

    def add_task(self, project_id: str, task_content: str, **kwargs) -> None:
        """
        Add a task to a project

        :param project_id: The id of the project
        :param task_content: Content of the task
        :param kwargs: Other elements of a task
        """
        try:
            task = self.api.add_task(project_id = project_id, content=task_content, **kwargs)
        except Exception as error:
            raise(error)

    def update_task(self, task_id: str, **kwargs) -> bool:
        """
        Update a task

        :param task_id: The id of a task
        :param kwargs: Other elements of a task

        :returns [True, False] based on whether update is successful:
        """
        try:
            is_success = self.api.update_task(task_id=task_id, **kwargs)
            return is_success
        except Exception as error:
            raise(error)

    def complete_task(self, task_id: str) -> bool:
        """
        Complete a task

        :param task_id: The id of a task

        :returns [True, False] based on whether the task completes
        """
        try:
            is_success = self.api.close_task(task_id=task_id)
            return is_success
        except Exception as error:
            raise(error)

    def close_task(self, task_id: str) -> bool:
        """
        Close a task

        :param task_id: The id of a task

        :returns [True, False] if the close is successful or not:
        """
        try:
            is_success = self.api.close_task(task_id=task_id)
            return is_success
        except Exception as error:
            raise(error)

    def delete_task(self, task_id: str) -> bool:
        """
        Delete a task

        :param task_id: The id of a task

        :returns [True, False] if the delete is successful or not:
        """
        try:
            is_success = self.api.delete_task(task_id=task_id)
            return is_success
        except Exception as error:
            raise(error)

    def get_task(self, task_id: str) -> Task:
        """
        Get a task

        :param task_id: The id of task
        :returns A task:
        """
        try:
            task = self.api.get_task(task_id=task_id)
            return task
        except Exception as error:
            raise(error)

    def get_sections(self, project_id) -> list[Section]: # type: ignore
        """
        Get sections of a project

        :param project_id: The id of the project

        :returns A list of sections:
        """
        try:
            sections = self.api.get_sections(project_id=project_id)
            return sections
        except Exception as error:
            raise(error)

    def create_section(self, name: str, project_id: str) -> None:
        """
        Create a new section of a project

        :param name: The name of the section
        :param project_id: The id of the project

        :returns None:
        """
        try:
            section = self.api.add_section(name=name, project_id=project_id)
        except Exception as error:
            raise(error)

    def get_section(self, section_id: str) -> Section:
        """
        Get a section

        :param section_id: The id of a section

        :returns The section:
        """
        try:
            section = self.api.get_section(section_id=section_id)
            return section
        except Exception as error:
            raise(error)

    def update_section(self, section_id: str, new_name: str) -> bool:
        """
        Update the name of a section

        :param section_id: The id of a section
        :param new_name: The new name of the section
        :returns [True, False] if update is successful or not:
        """
        try:
            is_success = self.api.update_section(section_id=section_id, name=new_name)
            return is_success
        except Exception as error:
            raise(error)

    def delete_section(self, section_id: str) -> bool:
        """
        Delete the section

        :param section_id: The id of a section
        :returns [True, False] if the delete is successful or not:
        """
        try:
            is_success = self.api.delete_section(section_id=section_id)
            return is_success
        except Exception as error:
            raise(error)

    def get_task_comments(self, task_id: str) -> list[Comment]:
        """
        Get the comments for a task

        :param task_id: A task id

        :returns A list of comments:
        """
        try:
            comments = self.api.get_comments(task_id=task_id)
            return comments
        except Exception as error:
            raise(error)

    def create_comment(self, task_id: str, content: str, attachment: dict = None) -> None: # type: ignore
        """
        Create a comment

        :param task_id: A task id
        :param content: Content of the comment
        :param attachment: an attachment object
        :returns A list of comments:
        """
        try:
            comments = self.api.add_comment(task_id=task_id, content=content, attachment=attachment)
        except Exception as error:
            raise(error)

    def get_comment(self, comment_id: str) -> Comment:
        """
        Get a comment

        :param comment_id: A comment id

        :returns A comment
        """
        try:
            comment = self.api.get_comment(comment_id=comment_id)
            return comment
        except Exception as error:
            raise(error)

    def update_comment(self, comment_id: str, content: str) -> bool:
        """
        Update a comment

        :param comment_id: A comment id
        :param content: The content of a comment

        :returns [True, False] if the update is successful or not:
        """
        try:
            is_success = self.api.update_comment(comment_id=comment_id, content=content)
            return is_success
        except Exception as error:
            raise(error)

    def delete_comment(self, comment_id: str) -> bool:
        """
        Get a comment

        :param comment_id: A comment id

        :returns [True, False] if the delete is successful or not:
        """
        try:
            is_success = self.api.delete_comment(comment_id=comment_id)
            return is_success
        except Exception as error:
            raise(error)
