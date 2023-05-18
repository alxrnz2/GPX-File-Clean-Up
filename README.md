# GPX-File-Clean-Up
In this repo, I'm including a few scripts I use to smooth, streamline and reverse GPX files. All Python-based with Bash prompts.

First, install dependencies. These scripts use `gpxpy` to parse GPX files and `geopy` for distance calculations.

`pip install gpxpy geopy`

To run the files, modify the `'input.gpx'` and `'output.gpx'` in the last line for your desired GPX input / output filenames. Place your input GPX file and the script in the current directory (e.g., using `cd` in Bash). Then run the script using a command like the below.

`python smooth_gpx.py`

## Smooth

The `smooth_gpx.py` script removes GPX points within 10 meters of each other to smooth out a route. When breaking or moving slow on segments, GPX routes can become messy.

Distance can be modified to any desired number of meters per file comments.

## Reverse

Sometimes watches die or we forget to start tracking. When you follow the same route on entry / exit, you can use `reverse_gpx.py` to efficiently extend your route.

## Simplify

GPX files from Strava and other trackers can contain unnecessary, clunky metadata. The `simplify_gpx.py` script removes timestamps and extensions.

The script can be modified to remove other metadata by adding `point.[data]...` per the file comments. (Or timestamps / extensions can be left in place.)
