# `gradesend`
*A basic command-line emailer for Gmail.*

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
