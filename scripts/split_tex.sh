#!/bin/bash
SOURCE="/home/aficio/Documents/DevelopmentV2/02-odd-zeta/tmp/odd_zeta_pcf_v1.tex"
DEST="src/chapters"

mkdir -p $DEST

# Using sed to extract ranges
sed -n '52,73p' "$SOURCE" > "$DEST/abstract.tex"
sed -n '81,256p' "$SOURCE" > "$DEST/01-introduction.tex"
sed -n '257,517p' "$SOURCE" > "$DEST/02-foundations.tex"
sed -n '518,1155p' "$SOURCE" > "$DEST/03-mechanisms.tex"
sed -n '1156,1921p' "$SOURCE" > "$DEST/04-bridges.tex"
sed -n '1922,2613p' "$SOURCE" > "$DEST/05-categorical.tex"
sed -n '2614,3184p' "$SOURCE" > "$DEST/06-discussion.tex"
sed -n '3185,3325p' "$SOURCE" > "$DEST/references.tex"

echo "Split complete with reorganized files."
