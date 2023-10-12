# fakerip

who tf pays for their api?


## Features

- small package
- easy to use
- quick web request to fakeit's website
- information gathering
- own email generation, based on received data
- easy to maintain code


## Usage

```py
    from fakerip import ripper

    # Initialize fakeit ripper instance
    ripstance = ripper.Ripstance()
    # Gather info
    ripstance.get_info()

    # Examples:
    print(ripstance.forename)
    print(ripstance.user_agent)
    print(ripstance.generate_random_email())
```
    
