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
Download latest release and install it using pip:
```py
    # Update the path to the correct path on your os
    # Using the source archieve
    pip install C:\Users\xxx\Downloads\fakerip\fakerip-2.0.tar.gz
    # Or using the wheel file
    pip install C:\Users\xxx\Downloads\fakerip\fakerip-2.0-py3-none-any.whl
```

In your code:
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
    
