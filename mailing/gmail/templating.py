from jinja2 import Environment, FileSystemLoader


class MailTemplater(object):
    """A simple wrapper around jinja2 to make for easy templating of common
       ta emails.
    """

    def __init__(self, template_dir):
        # build a jinja templating environment; if you plan to send HTML emails
        # it is highly advised that you enable the autoescaper, but for now we
        # will stick to plain text emails.
        self._env = Environment(autoescape=True,
                                loader=FileSystemLoader(template_dir))

    def new_assignment(self, fname, lname, codename,
                       assignment, duedate, duetime):
        """Basic templater of an assignment email.

        :param fname: first name of student
        :param lname: last name of student
        :param codename: submission name to be used by the student
        :param assignment: human-readable assignment name.
        :param duedate: due date
        :param duetime: due time
        :return: message if successful, None otherwise
        """
        return self._env.get_template('new_assignment.txt').render(
            fname=fname,
            lname=lname,
            codename=codename,
            assignment=assignment,
            duedate=duedate,
            duetime=duetime
        )
