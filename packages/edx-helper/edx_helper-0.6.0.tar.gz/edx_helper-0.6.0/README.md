# edx-helper

`edx-helper` is forked from [edx-dl](https://github.com/coursera-dl/edx-dl) which is no longer maintained.

<!-- TOC -->

- [Introduction](##introduction)
- [Installation instructions](##installation-instructions)
    - [Installation (recommended)](###Installation (recommended))
    - [Docker container](###Docker container)
    - [Optional: update youtube-dl](###Optional: update youtube-dl)
- [Quick Start](##Quick Start)
    - [Examples](###Examples)
- [Troubleshooting](##Troubleshooting)
    - [China issues](###china-issues)
- [Reporting issues](#reporting-issues)
- [Disclaimer](#disclaimer)
    <!-- /TOC -->



## Introduction

`edx-helper` is a simple tool to download videos and lecture materials from Open
edX-based sites.  

It is platform independent, and should work fine under Unix (Linux, BSDs etc.), Windows or Mac OS X.

## Installation instructions

`edx-helper` requires Python 3 and very few other dependencies. (As of October 2023, `edx-helper` passed the test of Python versions 3.7, 3.8, 3.9, 3.10, and 3.11).

**Note:** We *strongly* recommend that you use a Python 3 interpreter (3.9
or later).

### Installation (recommended)

Opening a terminal and typing the command If you have installed Python:

    python -m pip install edx-helper

### Manual Installation

To install all the dependencies please do:

    pip install -r requirements.txt
    pip install -r requirements-dev.txt

### Docker container

You can run this application via [Docker](https://docker.com) if you want. Just install docker and run

```
docker run --rm -it \
       -v "$(pwd)/edx/:/Downloaded" \
       strm/edx-helper -u <USER> -p <PASSWORD>
```

### Optional: update youtube-dl

One of the most important dependencies of `edx-helper` is `youtube-dl`. The
installation step listed above already pulls in the most recent version of
`youtube-dl` for you.

Unfortunately, since many Open edX sites store their videos on Youtube and
Youtube changes their layout from time to time, it may be necessary to
upgrade your copy of `youtube-dl`.  There are many ways to proceed here, but
the simplest is to simply use:

    pip install --upgrade youtube-dl

## Quick Start

Run the following command to query the usage and usage options:

```
edx-helper --help
```

Run the following command to query the courses in which you are enrolled:

    edx-helper -u <email or username> --list-courses

From there, choose the course you are interested in, copy its URL and use it
in the following command:

    edx-helper -u <email or username> COURSE_URL

Your downloaded videos will be placed in a new directory called
`Downloaded`, inside your current directory, but you can also choose another
destination with the `-o` argument.

To see all available options and a brief description of what they do, simply
execute:

    edx-helper --help

*Important Note:* To use sites other than <edx.org>, you **have** to specify the
site along with the `-x` option. For example, `-x stanford`, if the course
that you want to get is hosted on Stanford's site.

### Examples

Normal download:

```
edx-helper -u <user> https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS158x+1T2022/home
```

Download with subtitles:

```
edx-helper -u <user> --with-subtitles https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS158x+1T2022/home
```

Specify download directory：

```
edx-helper -u <user> -o ~/courses/ https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS158x+1T2022/home
```

Specify additional downloads by extension:

```
edx-helper -u <user> --file-formats "png,jpg" https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS158x+1T2022/home
```

Download CDN videos, do not download youtube videos:

```
edx-helper -u <user> --prefer-cdn-videos https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS158x+1T2022/home
```

## Troubleshooting

### china-issues

China cannot access YouTube. Please use the  `--prefer-cdn-videos`  option first, or use the `--ignore-errors` option. If you want to download YouTube videos, please use a proxy.

## Reporting issues

Before reporting any issue please follow the steps below:

1. Verify that you are running the latest version of all the programs (both of `edx-helper` and of `youtube-dl`).  Use the following command if in doubt:

        pip install --upgrade edx-helper
   
2. If you get an error like `"YouTube said: Please sign in to view this video."`, then we can't do much about it. You can try to pass your credentials to `youtube-dl` (see https://github.com/rg3/youtube-dl#authentication-options) with the use of `edx-helper`'s option `--youtube-dl-options`. If it doesn't work, then you will have to tell `edx-helper` to ignore the download of that particular video with the option `--ignore-errors`.
   
3. If the problem persists, feel free to [open an issue][https://github.com/csyezheng/edx-helper/issues] in our bug tracker, please fill the issue template with *as much information as
possible*.

## Supported sites

Except for edx, they have not been tested and are not supported yet. They may be supported in the future.

These are the current supported sites:

- [edX](http://edx.org)
- ~~[Stanford](http://lagunita.stanford.edu/)~~
- ~~[University of Sydney](http://online.it.usyd.edu.au)~~
- ~~[France Université Numérique](https://www.france-universite-numerique-mooc.fr/)~~
- ~~[GW Online SEAS](http://openedx.seas.gwu.edu/) - George Washington University~~
- ~~[GW Online Open](http://mooc.online.gwu.edu/) - George Washington University~~

This is the full [list of sites powered by Open edX][https://github.com/edx/edx-platform/wiki/Sites-powered-by-Open-edX]. Not all of them are supported at the moment, we welcome you to contribute support for them
and send a pull request also via our [issue tracker][https://github.com/csyezheng/edx-helper/issues].

## Disclaimer

`edx-helper` is meant to be used only for your material that edX gives you access to download. We do not encourage any use that violates their Terms Of Use.
