
freezing:
	virtualenv freezing
	freezing/bin/pip install -r requirements.in
	freezing/bin/pip freezing requirements.in
	rm -rf freezing

.PHONY: freezing
