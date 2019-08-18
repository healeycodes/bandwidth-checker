# ⚡ Bandwidth Checker ⚡

![preview image](https://github.com/healeycodes/bandwidth-checker/raw/master/graphexample.png "Image of scatter graph bandwidth results")

&nbsp;

Some ISPs promise money back if your bandwidth goes below a certain level.

This project includes two automated methods of testing download speed.
  - Speedtest's CLI.
  - Headless Chromium browser via Netflix's fast.com.

A Node server displays a scatter graph of the recent bandwidth results via Chart.js.

I run my own setup on a Raspberry Pi connected to my router via ethernet.

&nbsp;

## Install

### Client

`cd client`

`pip install requests`

**Speedtest CLI**:

`pip install speedtest-cli`

**Headless browser**:

`pip install selenium`

### Server

`cd server`

`npm install`

&nbsp;

## Run

### Client

Setup a cron job to run either version.

**Speedtest CLI**:

`python clitest.py 'https://server-location/save' 'password'`

Where the arguments are:
- Path to the endpoint to save the results.
- Password for that endpoint.

**Headless browser**:

`python browsertest.py '/usr/lib/chromium-browser/chromedriver' 'https://server-location/save' 'password'`

Where the arguments are:
- Path to the ChromeDriver executable (watch out for version clashes).
- Path to the endpoint to save the results.
- Password for that endpoint.

### Server

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

Bandwidth results are stored by the client via `/save`
