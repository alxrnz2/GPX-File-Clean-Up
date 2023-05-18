import gpxpy
import gpxpy.gpx

def reverse_points(input_file, output_file):
    # Parse the input GPX file
    with open(input_file, 'r') as gpx_file:
        gpx = gpxpy.parse(gpx_file)

    for track in gpx.tracks:
        for segment in track.segments:
            segment.points.reverse()

    # Write the modified GPX data to the output file
    with open(output_file, 'w') as gpx_file:
        gpx_file.write(gpx.to_xml())

# Run the function; modify file names to desired GPX files in current directory
reverse_points('input.gpx', 'output.gpx')
