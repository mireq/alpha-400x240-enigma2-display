# -*- coding: utf-8 -*-
TUNER_COUNT = 16
TUNERS_PER_ROW = 8
WIDTH = 14
HEIGHT = 15


standby_off_template = '<widget source="session.TunerInfo" render="Pixmap" position="{x},{y}" pixmap="tuner/tuner_{tuner}_off.png" size="14,15" alphatest="blend"><convert type="TunerInfo">TunerUseMask</convert><convert type="ValueBitTest">65535</convert><convert type="ConditionalShowHide" /></widget>'
standby_on_template = '<widget source="session.TunerInfo" render="Pixmap" position="{x},{y}" size="14,15" alphatest="blend" pixmap="tuner/tuner_{tuner}_on.png"><convert type="TunerInfo">TunerUseMask</convert><convert type="ValueBitTest">{mask}</convert><convert type="ConditionalShowHide" /></widget>'

active_off_template = '<widget source="session.TunerInfo" render="Pixmap" position="{x},{y}" size="14,15" alphatest="blend" pixmap="tuner/tuner_{tuner}_off.png"><convert type="TunerInfo">TunerAvailable</convert><convert type="ValueRange">{tuner},100</convert><convert type="ConditionalShowHide" /></widget>'
active_on_template = '<widget source="session.TunerInfo" render="Pixmap" position="{x},{y}" size="14,15" alphatest="blend" pixmap="tuner/tuner_{tuner}_on.png"><convert type="TunerInfo">TunerUseMask</convert><convert type="ValueBitTest">{mask}</convert><convert type="ConditionalShowHide" /></widget>'
active_frontend_template = '<widget source="session.FrontendInfo" render="Pixmap" position="{x},{y}" size="14,15" alphatest="blend" pixmap="tuner/tuner_{tuner}_active.png"><convert type="FrontendInfo">NUMBER</convert><convert type="ValueRange">{tuner_value},{tuner_value}</convert><convert type="ConditionalShowHide" /></widget>'


def main():
	with open('standby.xml', 'w') as fp:
		for tuner in range(1, TUNER_COUNT + 1):
			col = (tuner - 1) % TUNERS_PER_ROW
			row = (tuner - 1) // TUNERS_PER_ROW
			ctx = {
				'tuner': tuner,
				'x': 5 + (col * WIDTH),
				'y': 4 + (row * HEIGHT),
			}
			fp.write(standby_off_template.format(**ctx) + '\n')
		fp.write('\n\n')

		for tuner in range(1, TUNER_COUNT + 1):
			col = (tuner - 1) % TUNERS_PER_ROW
			row = (tuner - 1) // TUNERS_PER_ROW
			ctx = {
				'tuner': tuner,
				'x': 5 + (col * WIDTH),
				'y': 4 + (row * HEIGHT),
				'mask': 2 ** (tuner - 1),
			}
			fp.write(standby_on_template.format(**ctx) + '\n')

	with open('active.xml', 'w') as fp:
		for tuner in range(1, TUNER_COUNT + 1):
			col = (tuner - 1) % TUNERS_PER_ROW
			row = (tuner - 1) // TUNERS_PER_ROW
			ctx = {
				'tuner': tuner,
				'x': 10 + (col * WIDTH),
				'y': 206 + (row * HEIGHT),
			}
			fp.write(active_off_template.format(**ctx) + '\n')
		fp.write('\n\n')

		for tuner in range(1, TUNER_COUNT + 1):
			col = (tuner - 1) % TUNERS_PER_ROW
			row = (tuner - 1) // TUNERS_PER_ROW
			ctx = {
				'tuner': tuner,
				'x': 10 + (col * WIDTH),
				'y': 206 + (row * HEIGHT),
				'mask': 2 ** (tuner - 1),
			}
			fp.write(active_on_template.format(**ctx) + '\n')
		fp.write('\n\n')

		for tuner in range(1, TUNER_COUNT + 1):
			col = (tuner - 1) % TUNERS_PER_ROW
			row = (tuner - 1) // TUNERS_PER_ROW
			ctx = {
				'tuner': tuner,
				'x': 10 + (col * WIDTH),
				'y': 206 + (row * HEIGHT),
				'tuner_value': tuner - 1,
			}
			fp.write(active_frontend_template.format(**ctx) + '\n')


if __name__ == "__main__":
	main()
