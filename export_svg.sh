#!/bin/bash
for file in *.svg; do
	out_file="`basename $file .svg`.png"
	if [[ $file -nt $out_file ]]; then
		inkscape $file --export-filename=$out_file -d 96
		optipng -o7 $out_file
		advpng -z -4 $out_file
		pngout-static -k0 $out_file
	fi
done
