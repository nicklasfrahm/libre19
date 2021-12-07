PYTHON	:= venv/bin/python3

# Configure virtual environment.
$(PYTHON):
	python3 -m venv --prompt mcad venv
	$@ -m pip install --upgrade -r requirements.txt

# Transpile Python code to OpenSCAD program.
build/scad/%.scad: $(PYTHON) src/%.py
	./$^

# Generate STL file.
build/stl/%.stl: build/scad/%.scad
	@mkdir -p $(@D)
	openscad -o $@ -D 'quality="production"' $^
