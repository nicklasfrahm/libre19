PROJECT		:= cremini
MCAD_DIR	:= mcad

.PHONY: watch

# Define shorthands for mechanical design targets.
%.scad:
	make --no-print-directory -C $(MCAD_DIR) build/scad/$@

%.stl:
	make --no-print-directory -C $(MCAD_DIR) build/stl/$@

%.png:
	make --no-print-directory -C $(MCAD_DIR) build/png/$@

# Rerun target every time a file change is detected in the current directory.
watch:
	while true; do \
		clear; \
        make --no-print-directory $(TARGET); \
        inotifywait -qre close_write .; \
    done

# Clean up build outputs.
clean:
	-rm -rf $(MCAD_DIR)/build
