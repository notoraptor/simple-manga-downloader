# simple-manga-downloader
Simple manga downloader written in python.
Currently supports mangadex.org and mangaseeonline.us.


Allows you to download manga in 5 ways:

- all chapters of a series
- a range of chapters (from 5 to 15)
- a selection of chapters (5, 7, 10, 20)
- only the newest chapter
- check for new chapters for the tracked manga

Additional features of the downloader:

- It will check if a chapter on mangadex.org has multiple uploads by different groups and ask which one to download
- You can change the directory where the manga is saved
- You can add ongoing manga to the tracked list for a easy way to check for new chapters
- Config is saved as a .json for readability and easy modification
- The downloader has a config "mode" that allows the modification of the config file without having to edit the .json manually

# Requirements
- BeautifulSoup 4
- cfscrape

**IMPORTANT!**

[cfscrape requires Node.js to be installed](https://github.com/Anorov/cloudflare-scrape#nodejs-dependency)


# USAGE

## Download mode
This mode will download the manga from the link based on your selection, accepts multiple links.

Download all of the chapters:

```
SMD.py down link_to_manga [more_links]
```

Download a range of chapters (both ends are inclusive):

```
SMD.py down link_to_manga [more_links] -r 1 20
SMD.py down link_to_manga [more_links] --range 1 20
```

Download specific chapters (works if numbers are not in order):

```
SMD.py down link_to_manga [more_links] -s 1 10 5 15
SMD.py down link_to_manga [more_links] --selection 1 10 5 15
```

Download the newest chapter (based on chapter number not time of upload):

```
SMD.py down link_to_manga [more_links] -l
SMD.py down link_to_manga [more_links] --latest
```

## Update mode
This mode will go over every manga tracked in the config and download every missing chapter

```
SMD.py update
```

## Config mode
This mode allows the modification of the config file.

Adding a manga to the tracked list:
```
SMD.py conf -a link_to_manga [more_links]
SMD.py conf --add-tracked link_to_manga [more_links]
```

Removing a manga from the tracked list using links:
```
SMD.py conf -r link_to_manga [more_links]
SMD.py conf --remove-tracked link_to_manga [more_links]
```

Removing a manga from the tracked list by index:
```
SMD.py conf -r 5 1 3
SMD.py conf --remove-tracked 5 1 3
```

Removing a manga from the tracked list by title:
```
SMD.py conf -r title "title with spaces"
SMD.py conf --remove-tracked title "title with spaces"
```

Removal by index, title and link can be used together (works if multiple point to the same manga):
```
SMD.py conf -r link_to_manga 5 "sample title" link_to_manga 2
```

Clearing the tracked list:
```
SMD.py conf -c
SMD.py conf --clear-tracked
```

Changing the save directory:
```
SMD.py conf -s path_to_directory
SMD.py conf --save-directory path_to_directory
```

Reset the config to the default:
```
SMD.py conf -d
SMD.py conf --default
```

Listing all of the tracked manga(add -v/--verbose flag to also print the links):
```
SMD.py conf -l (-v)
SMD.py conf --list-tracked (--verbose)
```

Change the position of a manga:
```
SMD.py conf -m
SMD.py conf --modify-position
```

