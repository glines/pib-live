class DerivationGenerator():

    """ Constructor for a DerivationGenerator object, which generates .nix
	derivations given a template and various sources.
	
	The template argument is simply a python format string with the
	following named fields:
	    {src} - The RHS of the src attribute in the derivation
	    {patches} - A space separated list of patches to apply (with
		        absolute paths)
    """
    def __init__(self, template):
	self._template = template

    def generate_derivation(self):
	# Build a derivation file in .nix format from templates and other
	# parameters
	pass
