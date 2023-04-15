## Game Mechanics

* The game state include current calendar date, player's skill levels, and the list of available jobs
* The player skill levels is a set of technologies. Every technology has a name and a level: number of months user has been working with this technology
* Player selects a job from the list of available jobs and applies for it
* Every job has a list of required skills with the minimum level
* The chance of being accepted for a job is based on the player's skill levels. 
  - If the player has a skill levels higher than the required levels, the chance of being accepted is 100%. If the player has a skill levels lower than the required level, the chance of being accepted is 0%. If the player has a skill level equal to the required level, the chance of being accepted is 50%.
* As soon as the player is accepted for a job, the player's skill levels increase each month.
* Every month the player can select a job to apply or skip this month.

### Job
Every job has 
* a name
* a description, what user does in this job, what skills will be increased during this job
* a list of required skills with the minimum level
* a list of skills that will be increased if the player is accepted for this job
* A basic probablility of being accepted for this job

### Job Required skills
Each required skill has the following properties:
* The ID of the skill (e.g. "python")
* The minimum level of the skill
* Priority (0..1)

### Applying for a job, chance of being accepted
If a player applies for a job, the chance of being accepted is calculated as follows:
* The chance of being accepted is the basic probability of being accepted for this job.
* For every skill that the player has a level lower than the required level, the chance of being accepted is multiplied by 0.9 multiplied by number of missing months multiplied by priority
* For every skill that the player has a level higher than the required level, the chance of being accepted is multiplied by 1.05 multiplied by number of extra months divided by priority

### List of available jobs
The list of available jobs is generated from the pull of all jobs available in the game, based on the player's skill levels. The list of available jobs is generated as follows:
* For every job in the game, the chance of being accepted is calculated as described above
* The list of available jobs is generated from the list of all jobs in the game, where the chance of being accepted is greater than 0.05

### Displaying a job
The job is displayed as follows:
* The job name
* The job description
* The list of required skills with the minimum level. For each skill, display:
  - The skill name
  - The minimum level (number of months required)
  - The priority
* The chance of being accepted for this job

### Applying for a job
The player selects a job from the list of available jobs and applies for it. The chance of being accepted is calculated as described above. If the player is accepted for the job, the player's skill levels increase each month. If the player is not accepted for the job, the player skips this month.

### Skipping a month
The player skips this month. The player's skill levels increase based on the current job.
If the player has no current job, the player's skill levels do not increase.

### Displaying the game state
The game state is displayed as a player CV. The CV includes:
* The current calendar date
* The player's skill levels
* The list of jobs player had in the past

## UI
The game is a Telegram bot. The bot has the following commands:
* /start - start the game
* /help - display help
* /cv - display the game state
* /jobs - display the list of available jobs
* /apply - apply for a job
* /skip - skip this month

## Technical details

### Game state
The game state is stored in Dynamo DB table. The key is the Telegram user ID. The value is a JSON document with the following structure:
* The current calendar date
* The player's skill levels
* The list of jobs player had in the past

`pynamodb` Python library is used to access Dynamo DB.

### Jobs storage
The list of all jobs in the game is stored in a YAML file. The file is parsed and stored in memory. The file is reloaded every time the game is started.
Each job has the following properties:
* The ID of the job (e.g. "google-python-developer")
* The name of the company (e.g. "Google")
* The name of the job (e.g. "Python Developer")
* The job description, what the person has to do in this job.
* The company description, what company is doing.
* The list of required skills with the minimum level. For each skill:
  - The skill ID
  - The minimum level (number of months required)

### Skills storage
The list of all skills in the game is stored in a YAML file. The file is parsed and stored in memory. The file is reloaded every time the game is started.
Each skill has the following properties:
* The ID of the skill (e.g. "python")
* The name of the skill (e.g. "Python")
* The description of the skill (e.g. "Python is a programming language")

### Application

The application is a Python Flask application.

#### Directory structure

Here's a possible directory structure for the app:

```
app/
├── bot/
│   ├── __init__.py
│   ├── bot.py
│   ├── commands.py
│   └── handlers.py
├── data/
│   ├── jobs.yaml
│   ├── skills.yaml
│   └── ...
├── models/
│   ├── __init__.py
│   └── player.py
├── services/
│   ├── __init__.py
│   ├── job_service.py
│   ├── skill_service.py
│   └── player_service.py
├── utils/
│   ├── __init__.py
│   ├── database.py
│   └── parser.py
├── __init__.py
├── config.py
├── requirements.txt
└── app.py
```

- `bot/`: Contains modules related to the Telegram bot.
  - `bot.py`: Initializes the bot and starts the polling process.
  - `commands.py`: Defines the bot commands and their callbacks.
  - `handlers.py`: Contains the handlers for the bot's messages.
- `data/`: Contains YAML files with data for the game.
  - `jobs.yaml`: Contains the list of all jobs in the game.
  - `skills.yaml`: Contains the list of all skills in the game.
- `models/`: Contains the data models used by the app.
  - `player.py`: Defines the `Player` model.
- `services/`: Contains the business logic services of the app.
  - `job_service.py`: Defines the `JobService` class.
  - `skill_service.py`: Defines the `SkillService` class.
  - `player_service.py`: Defines the `PlayerService` class.
- `utils/`: Contains utility modules.
  - `database.py`: Defines the `Database` class for interacting with DynamoDB.
  - `parser.py`: Defines functions for parsing the data YAML files.
- `config.py`: Defines the app configuration variables.
- `requirements.txt`: Contains the app dependencies.
- `app.py`: Runs the Flask app.
