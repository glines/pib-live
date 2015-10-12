piglits = mesa_arb_shader_subroutine mesa_r600g-tess mesa_nir-cse-hash-v2
piglit_builds = $(patsubst %,piglits/%,$(piglits))
piglit_results = $(patsubst %,results/%,$(piglits))

all: $(piglit_results)

$(piglit_builds):
	nix-build -A piglits.$(@F) ./piglits.nix -o $@

.SECONDEXPANSION:
$(piglit_results): piglits/$$(shell basename $$@)
	mkdir $@
	./piglits/$(@F)/bin/piglit run ./piglits/$(@F)/lib/piglit/tests/quick.py ./results/$(@F)/
