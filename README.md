# instagram-bot
An instagram bot using the Selenium framework, automating various tasks on instagram. Developed as part of the Advanced Secure Systems course of the Technical University of Crete.

## Getting Started

### Prerequisites

The bot depends on the selenium web driver framework. To install the dependencies of the project, simply run:

```sh
pip install -r requirements.txt
```

Please note that the bot has been developed to be used on Firefox/Gecko-based browsers. Future plans include implementing the bot functionality for Chromium-based browsers.

### Usage

```sh
python3 socialMediaLikeBot.py [username] [password] [profile] [posts]
```

To use the bot, you need to setup an account beforehand for the bot to use, in order for it to perform the "likes" on the target public profile. The "posts" parameter is the number of posts of the public profile to be "liked" by the bot. If a number greater than the number of total posts on the user profile is provided, the bot "likes" all of the public profile's posts.

Should the target profile not be public, the bot will stop at the private profile's page.

### Implementation Details

The action targets for the bot are set with classes, tags and XPATH parameters. The bot locates the necessary buttons to perform the login process using the supplied user credentials, passes the cookie prompt, and after that, using the target profile parameter, the web driver follows the profile URL to perform the number of "likes" the user wants.

 
