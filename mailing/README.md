# `gradesend`
*A basic command-line emailer for Gmail.*

> Checkout the other mailers for other features and uses:
> - [SMTP](smtp/README.md) *For sending `.txt` and `.pdf` files all collected
>   in one directory.*
> - [mailgun](mailgun/README.md) *For sending out `.pdf` files in a directory
>   per student.*
>
> More commands will eventually be added to this to encapsulate the various
> functionality needs.

**This tool requires additional setup through [Google's Developer Console](https://console.developers.google.com/)**.
The first time you try sending email, it will prompt you for a path of your
credentials from the Google Dev. Console. (More information to come.)

## Usage

```
usage: gradesend assign [-h] --sender SENDER --template-dir TEMPLATE_DIR
                        [--class-file CLASS_FILE]
                        labname prefix duedate duetime

positional arguments:
  labname               formal name of the assignment
  prefix                assignment prefix for submission
  duedate               assignment due date
  duetime               assignment due time

optional arguments:
  -h, --help            show this help message and exit
  --sender SENDER, -S SENDER
                        sender\s email adress
  --template-dir TEMPLATE_DIR, -T TEMPLATE_DIR
                        file path to the template directory
  --class-file CLASS_FILE, -F CLASS_FILE
                        filepath to the class json file
```


## Example `classroom.json`

```json
{
    "coursename": "CS051",
    "students": [
        {
            "email": "example@example.com",
            "fname": "Cecil",
            "lname": "Sagehen"
        },
        {
            "email": "example_2@example.com",
            "fname": "FirstName",
            "lname": "LastName"
        }
    ]
}
```

# Dependencies

This tool has been developed in a Python `v3.4.3` environment. To see a list of
module dependencies, look at [pip_dependencies.txt](pip_dependencies.txt).

# Example Assignment Notification

```
Hi, {{ fname }} {{ lname }}!

This is a reminder that {{ assignment }} is due on {{ duedate }} at {{ duetime }}.

Please follow the standard export procedures to turn in your
submission. We will grade a submission from you with the
following name:

---------
{{ codename }}
---------

If you need to submit another version, please use the following
names in order:

---------
{{ codename }}_V2
{{ codename }}_V3
{{ codename }}_V4
{{ codename }}_V5
---------

In order to help us process your programs efficiently,
we will be using several scripts to collect the code out of the
dropbox and deliver it to the professors. If you do not use the
name(s) above, we will not be able to find your lab and it will
NOT be graded.

Furthermore, before you submit your final version, please keep
the following reminders in mind:
---------
* Each file of code you
submit, MUST contain your name in a comment at the top. For
example:

/**
 * This is some description of a class...
 *
 * @author {{ fname }} {{ lname }}
 * @version November 25, 2015
 */

* Extra credit will only be evaluated if you tell us what you
did! At the top of the main class, please include a comment that
lists the extra credit that you completed.

* If you are using different run configurations than those
specified in the starter code, tell us in your header comment so
that we can run your program in the correct size and
configuration! It's very hard for us to guess!
---------

Please do not hesitate to
reach out to us on Piazza if you have questions regarding
submitting your program.

Happy coding!

Best,
CS051 TAs

This email has been automatically created and sent. If you
have any questions or need to get in contact with the professors
or the TA, please use Piazza ( https://piazza.com/ ). Do NOT
reply directly to this email.
```
