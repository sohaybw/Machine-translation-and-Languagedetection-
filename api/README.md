# API Details

we have two Apis 1st one is for translate Arabic to english or english to arabic 
2nd one is for detect if the language is arabic or english or etc depends on your dataset 
every api send in body text and responce as json data the key in every api is Text like

detect language:
{detect: """ {
  "text": "I have a blue car and work in machine learning  "
}

"""
the response is json data like """{
    "Input": "I have a blue car and work in machine learning  ",
    "Output": "English"
}"""  }

Translate:
{detect: """ {
  "text": "I have a blue car and work in machine learning  "
}

"""
the response is json data like """{
    "Input": "I have a blue car and work in machine learning  ",
    "Output": "انا املك سيارة ازرق واعمل في تعلم الالة"
}"""  }

## API Structure

```bash

├── src                          # directory for source code for the whole API logic 
│    ├── routes                  # dir for routes and init fo flask app
│    ├── config                  # dir for any project configuration
│    ├── DS                      # dir to store data science models
│    ├── schemas                 # dir for app types
│    └── main.py                 # runner file : to start the server using it.
├── env                          # directory for virtual env, It's required for docker compose 
├── Dockerfile                   # docker file for production
├── flake8                       # config file for linting
├── Makefile                     # Make file to help create docker images 
├── requirements.txt             # requirements file for all dependencies
└── README.md                    # ...
```
