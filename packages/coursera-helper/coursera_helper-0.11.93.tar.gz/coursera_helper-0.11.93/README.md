[![Build Status](https://github.com/csyezheng/coursera-helper/workflows/Run%20Unit%20Tests/badge.svg)](https://github.com/csyezheng/coursera-helper/actions/workflows/)
[![Coverage Status](https://coveralls.io/repos/csyezheng/coursera-helper/badge.svg)](https://coveralls.io/r/coursera-helper/coursera-helper)
[![Code Climate](https://codeclimate.com/github/csyezheng/coursera-helper/badges/gpa.svg)](https://codeclimate.com/github/csyezheng/coursera-helper)
[![Latest version on PyPI](https://img.shields.io/pypi/v/coursera-helper.svg)](https://pypi.python.org/pypi/coursera-helper)

# coursera-helper

`coursera-helper` is forked from [coursera-dl](https://github.com/coursera-dl/coursera-dl) which is no longer maintained.

<!-- TOC -->

  * [Introduction](#introduction)
  * [Installation instructions](#installation-instructions)
    + [Installation (recommended)](#installation-recommended)
    + [Manual Installation](#manual-installation)
    + [Docker container](#docker-container)
  * [Quick Start](#quick-start)
    + [Examples](#examples)
  * [Troubleshooting](#troubleshooting)
    + [china-issues](#china-issues)
  * [Reporting issues](#reporting-issues)
  * [Disclaimer](#disclaimer)

  <!-- /TOC -->

## Introduction

`coursera-helper` is a tool for downloading Coursera.org videos and naming them..  

It is platform independent, and should work fine under Unix (Linux, BSDs etc.), Windows or Mac OS X.

## Installation instructions

`coursera-helper` requires Python 3 and very few other dependencies. (As of October 2023, `coursera-helper` passed the test of Python versions 3.8, 3.9, 3.10, and 3.11).

### Installation (recommended)

Opening a terminal and typing the command If you have installed Python:

    python -m pip install coursera-helper

### Manual Installation

To install all the dependencies please do:

    pip install -r requirements.txt

### Docker container

You can run this application via [Docker](https://docker.com) if you want. Just install docker and run

```
docker run --rm -it -v \
    "$(pwd):/courses" \
    coursera-helper/coursera_helper -u <USER> -p <PASSWORD>
```

## Quick Start

Run the following command to query the usage and options:

```
coursera-helper --help
```

Run the following command to query the courses in which you are enrolled:

    coursera-helper -u <email or username> --list-courses

From there, choose the course you are interested in, copy its course name and use it
in the following command:

    coursera-helper -u <email or username> <COURSE NAME>

Your downloaded videos will be placed in current directory, but you can also choose another destination with the `--path` argument.

To see all available options and a brief description of what they do, simply
execute:

    coursera-helper --help


### Examples

General download:

```
coursera-helper -u <user> data-analysis-with-python
```

Download with subtitles:

```
coursera-helper -u <user> --subtitle-language en,zh-CN|zh-TW data-analysis-with-python
```

Specify video resolution：

```
coursera-helper -u <user> --video-resolution 720p data-analysis-with-python
```

Download with quizzes:

```
coursera-helper -u <user> --download-quizzes data-analysis-with-python
```

Download with notebooks:

```
coursera-helper -u <user> --download-notebooks data-analysis-with-python
```

Alternatively, if you want to store your preferred parameters (which might also include your username and password), create a file named `coursera-dl.conf` where the script is supposed to be executed, with the following format:

```
--username <user>
--password <pass>
--subtitle-language en,zh-CN|zh-TW
--download-quizzes
--download-notebooks
--video-resolution 720p
--download-delay 10
-cauth <cauth value>
```

If you have created a file named `coursera-dl.conf`, you just download course with command:

```
coursera-helper data-analysis-with-python
```

## Troubleshooting

### china-issues

If you are from China and you're having problems downloading videos, adding 

```
52.84.167.78   d3c33hcgiwev3.cloudfront.net
```

in the hosts file (`/etc/hosts` or `C:\Windows\System32\drivers\etc`) 

Refresh DNS with this command in the terminal.

```
ipconfig /flushdns
```

## Reporting issues

Before reporting any issue please follow the steps below:

1. Verify that you are running the latest version of all the programs.  Use the following command if in doubt:

        pip install --upgrade coursera-helper
   
3. If the problem persists, feel free to [open an issue](https://github.com/csyezheng/coursera-helper/issues) in our bug tracker, please fill the issue template with *as much information as
possible*.

## Disclaimer

`coursera-helper` is meant to be used only for your material that coursera gives you access to download. We do not encourage any use that violates their Terms Of Use.

