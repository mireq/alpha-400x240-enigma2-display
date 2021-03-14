#!/bin/bash
svg_files=`find . -type f -name '*.svg'`
while IFS= read -r file; do
	out_file="${file%.*}.png"
	if [[ $file -nt $out_file ]]; then
		inkscape $file --export-filename=$out_file -d 96
		optipng -o7 $out_file
		advpng -z -4 $out_file
		pngout-static -k0 $out_file
	fi
done <<< "$svg_files"
