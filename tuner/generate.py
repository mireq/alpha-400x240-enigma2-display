# -*- coding: utf-8 -*-
TUNER_COUNT = 16
TUNER_COLORS = [
	'#ec2019', '#f1732c', '#fdd332', '#a4e543', '#45de9b', '#2fbeeb', '#3e51e0', '#d636ec',
	'#00c169', '#00d2b7', '#009ce0', '#0014da', '#d700c9', '#d00035', '#d35200', '#84d600',
]


def main():
	start_char = ord('A')
	with open('tuner_off.svg', 'r') as fp:
		tunner_template = fp.read()
	for tuner in range(TUNER_COUNT):
		tuner_code = tunner_template.replace('{tuner_name}', chr(start_char + tuner))
		with open(f'tuner_{tuner+1}_off.svg', 'w') as fp:
			fp.write(tuner_code)

	with open('tuner_on.svg', 'r') as fp:
		tunner_template = fp.read()
	for tuner in range(TUNER_COUNT):
		tuner_code = tunner_template.replace('{tuner_name}', chr(start_char + tuner)).replace('{tuner_color}', TUNER_COLORS[tuner])
		with open(f'tuner_{tuner+1}_on.svg', 'w') as fp:
			fp.write(tuner_code)

	with open('tuner_active.svg', 'r') as fp:
		tunner_template = fp.read()
	for tuner in range(TUNER_COUNT):
		tuner_code = tunner_template.replace('{tuner_name}', chr(start_char + tuner)).replace('{tuner_color}', TUNER_COLORS[tuner])
		with open(f'tuner_{tuner+1}_active.svg', 'w') as fp:
			fp.write(tuner_code)


if __name__ == "__main__":
	main()
