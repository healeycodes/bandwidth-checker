# ⚡ Bandwidth Checker ⚡

![preview image](https://github.com/healeycodes/bandwidth-checker/raw/master/graphexample.png "Image of scatter graph bandwidth results")

&nbsp;

Some ISPs promise money back if your bandwidth goes below a certain level.

This project runs a headless Chrome browser to test bandwidth speed on the client via Netflix's fast.com.

Also included is a Node server that displays a scatter graph of the recent bandwidth results via Chart.js.

&nbsp;

## Install

#### Client

`cd client`

`pip install selenium`

#### Server

`cd server`

`npm install`

&nbsp;

## Run

#### Client

Setup a cron job to run:

`python bandwidthchecker.py './chromedriver' 'https://server-location/save' 'password'`

Where the arguments are:
- Path to the correct ChromeDriver version.
- Path to the endpoint to save the results.
- Password for that endpoint.

#### Server

Setup password:
```
Unix Bash (Linux, Mac, etc.):
$ export PASSWORD=hello

Windows CMD:
> set PASSWORD=hello

Windows PowerShell:
> $env:PASSWORD = "hello"
```

`npm start`

Visit the root path `/` to view bandwidth results.
