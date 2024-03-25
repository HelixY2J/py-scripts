# Skippy

This Python script checks the weather for a given location and sends an email reminder if the weather is sunny, hazy or partly cloudy. It serves as a handy tool to remind users to bring their umbrellas when needed.

### Installation

Install the required libraries:

```python
    pip install -r requirements.txt
```

After running the script , provide these information : 

-  Enter your location , email address and password as prompted
-  The script will check the weather and send a reminder email if necessary

## Security

As of now, Google has changed access to less secure apps as it has flagged this sort of login as "less secure".
But we can get access to the gmail account by the solution proposed by Google

- Head over to security option in your google account 
- Active two step verification 
- Create an app password which will be of 16 digits
- Use the app password instead of your google password for your smtp login
- Make sure to remove any whitespaces in your password
- The username argument should only include the part before the '@gmail.com' domain. 