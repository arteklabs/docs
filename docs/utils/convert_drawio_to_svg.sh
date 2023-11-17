# Convert a draw.io file into a svg file.

# The convertion requires the installation of the draw.io CLI, which is perhaps not a valid production
# dependency. The diagrams will be committed as svg files, althought this is not ideal. Draw.io could
# be perhaps a CICD dependency.

# Find all drawio files recursively
find "../sphinx/src" -type f -name "*.drawio" | while read -r source; do
    target="../sphinx/static/img/$(basename "$source" .drawio).svg"
    # convert from drawio to svg
    draw -x -f svg -o $target $source
done

# Find all drawio files recursively
find "../sphinx/_static" -type f -name "*.drawio" | while read -r source; do
    target="../sphinx/_static/$(basename "$source" .drawio).svg"
    draw -x -f svg -o $target $source
done