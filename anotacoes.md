No site no Heroku: settings / add buildpack:
        https://github.com/heroku/heroku-buildpack-google-chrome
        https://github.com/heroku/heroku-buildpack-chromedriver
    
No site do Heroku: Settings / Reveal Config Vars:
        KEY: CHROMEDRIVER_PATH    /    VALUE: /app/.chromedriver/bin/chromedriver
        KEY: GOOGLE_CHROME_BIN   /     VALYE: /app/.apt/usr/bin/google-chrome