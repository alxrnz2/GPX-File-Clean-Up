# GPX-File-Clean-Up
In this repo, I'm including a few dependencies I use to smooth, streamline and reverse GPX files. All scripts are Python-based.

First, install dependencies. These scripts use `gpxpy` to parse GPX files and `geopy` for distance calculations.

`pip install gpxpy geopy`

## Smooth

The `smooth_gpx.py` script removes GPX points within 5 meters of each other to smooth out a route. When breaking or moving slow on segments, GPX routes can become messy.

Distance can be modified to any desired number of meters per file comments.

## Reverse

Sometimes watches die or we forget to start tracking. When you follow the same route on entry / exit, you can use `reverse_gpx.py` to efficiently extend your route.

## Simplify

GPX files out of Strava and other trackers can contain more metadata than necessary. The `simplify_gpx.py` script removes timestamps and extensions.

It can be modified to remove other metadata by adding `point.[data]...` per the file comments. (Or timestamps / extensions can be left.)
